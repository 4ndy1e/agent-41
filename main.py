import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    print("Hello from agent-41!")
    
    # check if prompt is provided 
    user_prompt = ""
    containsVerbose = "--verbose" in sys.argv
    
    if len(sys.argv) > 1:
        user_prompt = sys.argv[1]
    else:
        print("Prompt cannot be empty. Please provide a prompt after the script")
        print("Example: How can I improve my skills in python")
        sys.exit(1)
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    
    if containsVerbose:
        print(f"User prompt: {user_prompt}")
    
    # load api key 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    generate_content(client, messages, containsVerbose)

def generate_content(client, messages, containsVerbose):
    prompt_answer = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages
    )
    
    if containsVerbose:
        print(f"Prompt tokens: {prompt_answer.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {prompt_answer.usage_metadata.candidates_token_count}")
    
    print("Response: ")
    print(prompt_answer.text)


if __name__ == "__main__":
    main()
