const openai = require('openai');
const dotenv = require('dotenv');
const readline = require('readline');

// Load environment variables from the .env file
dotenv.config();

// Set the OpenAI API key from the .env file
const apiKey = process.env.OPENAI_API_KEY;

// Initialize the OpenAI client
const client = new openai({ key: apiKey });

// Function to generate text using gpt-3.5-turbo
function generateText(prompt) {
    return client.completions.create({
      model: 'text-davinci-003',
      prompt: prompt,
      max_tokens: 100,
      temperature: 0.8
    });
  }

// Function to handle user input and generate text
async function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  while (true) {
    const prompt = await askQuestion(rl, 'Enter a prompt (or type "exit" to quit): ');
    if (prompt.toLowerCase() === 'exit') {
      rl.close();
      break;
    }

    const response = await generateText(prompt);
    console.log(' ');
    console.log('--------- ChatGPT Begin ---------');
    console.log(' ');
    console.log(response.choices[0].text.trim());
    console.log(' ');
    console.log('+++++++++ ChatGPT End +++++++++++');
    console.log('=================================');
    console.log(' ');
  }
}

function askQuestion(rl, question) {
  return new Promise((resolve) => {
    rl.question(question, resolve);
  });
}

// Start the main loop
main();
