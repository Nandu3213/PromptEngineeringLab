# WEEK 15: MULTIMODAL PROMPTING EXPLORATION
# Install:
# pip install openai
 
from openai import OpenAI
import base64
 
print("===== WEEK 15: MULTIMODAL PROMPTING =====")
 
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
 
image_path = "sample.jpg"
 
with open(image_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")
 
try:
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Describe this image in simple words and list the important objects visible."
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}"
                    }
                ]
            }
        ]
    )
 
    print("\n--- MULTIMODAL RESPONSE ---")
    print(response.output_text)
 
except Exception as e:
    print("\nError:", e)

