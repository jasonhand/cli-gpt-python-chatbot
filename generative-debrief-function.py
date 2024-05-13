import openai
from dotenv import load_dotenv
import os
import azure.functions as func
import json

# Load the .env file
load_dotenv()

# Set the OpenAI API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a function to generate text using gpt-3.5-turbo
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.8
    )
    return response.choices[0].text.strip()

# Azure Function entry point
def main(req: func.HttpRequest) -> func.HttpResponse:
    # Parse the request body for the "prompt" field
    try:
        req_body = req.get_json()
        prompt = req_body['prompt']
    except (ValueError, KeyError):
        return func.HttpResponse(
            "Please pass a prompt in the request body as JSON.",
            status_code=400
        )

    generated_text = generate_text(prompt)

    # Return the generated text as JSON
    return func.HttpResponse(json.dumps({"generated_text": generated_text}), mimetype="application/json")
