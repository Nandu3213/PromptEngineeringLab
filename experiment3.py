import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ API key not found in .env file.")
    exit()

# Connect to Gemini through OpenAI-compatible API
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def ask_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="gemini-3.7-flash",
            temperature=0.5,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


# Iteration 0 - Baseline
prompt0 = "Explain photosynthesis to a 10-year-old."


# Iteration 1 - Add analogy and length constraint
prompt1 = (
    "You are a friendly science teacher. "
    "Explain photosynthesis to a 10-year-old using a simple analogy. "
    "Keep the explanation to 3 short sentences and avoid technical jargon."
)


# Iteration 2 - Add mnemonic and diagram description
prompt2 = (
    "You are a friendly science teacher. "
    "Explain photosynthesis to a 10-year-old using a simple analogy. "
    "Keep it to 3 short sentences, avoid technical jargon, "
    "include a memory trick and describe a simple diagram."
)


prompts = [prompt0, prompt1, prompt2]


# Run all iterations
for i, prompt in enumerate(prompts):

    print("\n" + "=" * 50)
    print(f"ITERATION {i}")
    print("=" * 50)

    print("Prompt:")
    print(prompt)

    response = ask_llm(prompt)

    print("\nResponse:")
    print(response)

    if i == 0:
        print("\nAnalysis:")
        print("The baseline gives a basic explanation but may be lengthy or technical.")

    elif i == 1:
        print("\nAnalysis:")
        print("The analogy, simple language, and length limit make the explanation easier for children.")

    else:
        print("\nAnalysis:")
        print("The mnemonic and diagram description improve memory and visualization.")


# Final summary
print("\n" + "=" * 50)
print("FINAL SUMMARY")
print("=" * 50)

print("- Iteration 0 provided a basic explanation.")
print("- Iteration 1 improved clarity through analogy and brevity.")
print("- Iteration 2 improved engagement with a mnemonic and visual description.")