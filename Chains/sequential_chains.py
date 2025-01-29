from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
import os
load_dotenv()

api_key =os.getenv("MISTRAL_API_KEY")

model =ChatMistralAI(api_key=api_key,model="mistral-large-latest")

animal_facts_template =ChatPromptTemplate([
    ("system","you love facts and you tell fatcts about {animal}"),
    ("human","tell me {count} facts.")
])