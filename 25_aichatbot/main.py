import os
from openai import Openai
API_KEY = "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"

messages = []

client = Openai(api_key=API_KEY)

def completion(user_message):
    messages.append({
        "role": "user",
        "content": user_message
    })
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o"
    )
    assistant_message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(assistant_message)
    return assistant_message["content"]

if __name__ == "__main__":
    print("Jarvis: Hi, I am Jarvis. How may I help you?\n")
    while True:
        user_question = input("User: ")
        response = completion(user_question)
        print(f"Jarvis: {response}\n")

