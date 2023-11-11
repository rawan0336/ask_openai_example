#from openai import OpenAI
import openai
import os
from dotenv import load_dotenv
api_key = os.environ.get("OPENAI_API_KEY")

openai.api_key = api_key
load_dotenv()
if not api_key:
    raise Exception("API key is missing. Set the OPENAI_API_KEY environment variable.")
api_key = os.environ.get("OPENAI_API_KEY")

def main():
    x= input("Enetr your message: ")
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
    prompt=x,max_tokens=150
        
        )
    print(response["choices"][0]["text"])




if __name__=="__main__":
    main()