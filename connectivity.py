import os
from dotenv import load_dotenv
from openai import OpenAI

try:
    # Load environment variables
    load_dotenv()

    # Read Gemini API key
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI API key not found in .env file.")

    print("✅ Environment ready. Sending prompt...")

    # Connect to Gemini through OpenAI-compatible API
    client = OpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    prompt = "What is prompt engineering? Answer in one sentence."

    print(f"\nPrompt: {prompt}")

    response = client.chat.completions.create(
        model="gemini-3.7-flash",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    print("\nResponse:")
    print(answer)

except ValueError as e:
    print(f"❌ Error: {e}")

except Exception as e:
    print(f"❌ API/Network Error: {e}")