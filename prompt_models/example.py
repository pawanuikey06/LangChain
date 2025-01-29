from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
import os

load_dotenv()
api_key =os.getenv("MISTRAL_API_KEY")
model =ChatMistralAI(api_key=api_key ,model="mistral-large-latest")

template ="write a {tone} email to {company} expressiong  interest in the {position} position , mentioning {skill} as a key strength. Keep it to 4 lines max"

prompt_template =ChatPromptTemplate.from_template(template)

prompt=prompt_template.invoke({
    "tone":"energetic",
    "company":"amazon",
    "position":"AI Engineer",
    "skill":"AI"
})
# print(prompt)
# print(prompt_template)

result =model.invoke(prompt)
print(result)
