#Created by Jason Hand - testing Datadog's OpenAI Monitoring integration 
import openai
from dotenv import load_dotenv
import os

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

# Main loop
while True:
    # Get user input and generate text
    prompt = input("Enter a prompt (or 'exit' to quit): ")
    if prompt.lower() == 'exit':
        break
    
    generated_text = generate_text(prompt)
    print (" ")
    print ("--------- ChatGPT Begin ---------")
    print (" ")
    print(generated_text)
    print (" ")
    print ("+++++++++ ChatGPT End +++++++++++")
    print ("=================================")
    print (" ")