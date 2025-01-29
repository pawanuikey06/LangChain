from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")  # Make sure the .env file has the correct key
llm = ChatMistralAI(api_key=api_key, model="mistral-large-latest")
result =llm.invoke("what is the square root of 49")
print(result.content)

