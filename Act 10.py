import sys
from openai import OpenAI

# Connect to LM Studio local server
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # dummy key, required but not used
)

def chat():
    print("🤖 Local Chatbot (LM Studio)")
    print("Type 'quit' to exit.\n")

    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        try:
            user_input = input("You: ")

            if user_input.lower() == "quit":
                print("Goodbye!")
                break

            # Add user message
            messages.append({"role": "user", "content": user_input})

            # Send request to LM Studio
            response = client.chat.completions.create(
                model="local-model",  # LM Studio ignores name but requires it
                messages=messages,
                temperature=0.7
            )

            reply = response.choices[0].message.content

            print("Bot:", reply)

            # Save assistant reply
            messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            print("⚠️ Error:", e)
            print("Make sure LM Studio server is running at http://localhost:1234")
            continue

if __name__ == "__main__":
    chat()