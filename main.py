import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt

from call_function import available_functions, call_function

def main():
    load_dotenv()

    args = sys.argv[1:]
    verbose_flag = False
    if not args:
        print("No prompt given. Please provide a prompt.")
        sys.exit(1)
   
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    if args[-1] == "--verbose":
        verbose_flag = True
        args = args[:-1]
    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt),
    )

    if response.function_calls:
        function_call_part = response.function_calls[0] 

    call_function(function_call_part, verbose=verbose_flag)
    '''
    if verbose_flag:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
       
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(response.text)
    '''

if __name__ == "__main__":
    main()
