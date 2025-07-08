import os 
import sys
from dotenv import load_dotenv
from google import genai

# check if prompt is provided 
prompt = ""
if len(sys.argv) > 1:
    prompt = sys.argv[1]
else:
    print("Erorr, prompt cannot be empty. Please provide a prompt after the script")
    sys.exit(1)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

prompt_answer = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)

def main():
    print("Hello from agent-41!")
    print(prompt_answer.text)
    print(f"Prompt tokens: {prompt_answer.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {prompt_answer.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
