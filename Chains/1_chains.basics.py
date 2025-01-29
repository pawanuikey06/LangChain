from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_mistralai import ChatMistralAI
import os

load_dotenv()
api_key=os.getenv("MISTRAL_API_KEY")
model =ChatMistralAI(api_key=api_key,model="mistral-large-latest")

prompt_template =ChatPromptTemplate.from_messages([
    ("system","You are facts expert who knows facts about {animal}."),
    ("human","Tell me {fact_count} facts."),
])


chain =prompt_template | model | StrOutputParser()


result =chain.invoke({"animal":"bhaloo","fact_count":"2"})

print(result)