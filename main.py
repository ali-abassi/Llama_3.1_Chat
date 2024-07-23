from groq import Groq
import os
from colorama import Fore, Style, init
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize colorama for cross-platform color support
init()

# Use environment variable for API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(messages):
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    print(f"{Fore.GREEN}AI: ", end="", flush=True)
    for chunk in completion:
        content = chunk.choices[0].delta.content or ""
        print(content, end="", flush=True)
        response += content
    print(Style.RESET_ALL)
    return response

def chat():
    messages = []
    print(f"{Fore.YELLOW}Welcome to the AI chat! Type 'exit' to end the conversation.{Style.RESET_ALL}\n")
    
    while True:
        user_input = input(f"{Fore.CYAN}You: {Style.RESET_ALL}")
        if user_input.lower() == 'exit':
            break
        
        messages.append({"role": "user", "content": user_input})
        print()  # Add a newline for better spacing
        
        ai_response = get_ai_response(messages)
        messages.append({"role": "assistant", "content": ai_response})
        print()  # Add a newline for better spacing

    print(f"\n{Fore.YELLOW}Thank you for chatting! Goodbye!{Style.RESET_ALL}")

if __name__ == "__main__":
    chat()
