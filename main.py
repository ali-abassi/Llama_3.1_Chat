from groq import Groq
import os
from colorama import Fore, Style, init
from dotenv import load_dotenv

load_dotenv()
init()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(messages):
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
        stream=True,
    )

    print(f"{Fore.GREEN}AI: ", end="", flush=True)
    response = "".join(chunk.choices[0].delta.content or "" for chunk in completion)
    print(response, end="", flush=True)
    print(Style.RESET_ALL)
    return response

def chat():
    messages = []
    print(f"{Fore.YELLOW}Welcome to the AI chat! Type 'exit' to end the conversation.{Style.RESET_ALL}\n")
    
    while (user_input := input(f"{Fore.CYAN}You: {Style.RESET_ALL}").lower()) != 'exit':
        messages.append({"role": "user", "content": user_input})
        messages.append({"role": "assistant", "content": get_ai_response(messages)})
        print()

    print(f"\n{Fore.YELLOW}Thank you for chatting! Goodbye!{Style.RESET_ALL}")

if __name__ == "__main__":
    chat()
