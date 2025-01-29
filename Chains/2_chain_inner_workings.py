from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain.schema.runnable import RunnableLambda,RunnableSequence
from langchain.prompts import ChatPromptTemplate
import os

load_dotenv()

api_key =os.getenv("MISTRAL_API_KEY")

model =ChatMistralAI(api_key=api_key,model="mistral-large-latest")

prompt_template =ChatPromptTemplate([
    ("system","you love facts and you tell fatcts about {animal}"),
    ("human","tell me {count} facts.")
])

format_prompt =RunnableLambda(lambda x:prompt_template.format_prompt(**x))

invoke_model =RunnableLambda(lambda x: model.invoke(x.to_messages()))

parse_output =RunnableLambda(lambda x:x.content)

chain =RunnableSequence(first=format_prompt,middle=[invoke_model],last=parse_output)

response =chain.invoke({"animal":"cat","count":2})

print(response)




