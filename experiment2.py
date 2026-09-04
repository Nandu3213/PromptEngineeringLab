import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found in .env file.")

# Create Gemini client
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def send_prompt(prompt):
    response = client.chat.completions.create(
        model="gemini-3.7-flash",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# Baseline prompt
baseline_prompt = "Explain what is a prime number."

# Enhanced prompt
enhanced_prompt = """
You are a math tutor for 5th graders.
Explain what a prime number is using simple language.
Give the definition plus two examples.
Keep the total explanation under 50 words.
"""


print("=" * 60)
print("BASELINE PROMPT")
print("=" * 60)

print("Prompt:", baseline_prompt)

baseline_response = send_prompt(baseline_prompt)

print("\nResponse:")
print(baseline_response)


print("\n" + "=" * 60)
print("ENHANCED PROMPT")
print("=" * 60)

print("Prompt:", enhanced_prompt)

enhanced_response = send_prompt(enhanced_prompt)

print("\nResponse:")
print(enhanced_response)


print("\n" + "=" * 60)
print("ANALYSIS")
print("=" * 60)

print("The baseline prompt gives a general explanation.")
print("The enhanced prompt provides a more specific and structured answer")
print("because it defines a role, uses simple language, requests examples,")
print("and specifies a word limit.")