from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")
# NEVER hardcode keys — use environment variable
client = OpenAI(api_key=config["api_key"])

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        reply = chat_with_gpt(user_input)
        print("Chatbot:", reply)
