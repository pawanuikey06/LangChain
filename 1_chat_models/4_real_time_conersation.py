from dotenv import load_dotenv
import os
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage ,HumanMessage,SystemMessage

api_key =os.getenv("MISTRAL_API_KEY")

model =ChatMistralAI(api_key=api_key ,model="mistral-large-latest")


chat_history =[]

system_message =SystemMessage(content="you are Helpful AI assistant")
chat_history.append(system_message)

while True:
    query=input("You: ")
    if query.lower() =="exit":
        print("Exiting the chat...")
        break


    chat_history.append(HumanMessage(content=query))
    result =model.invoke(chat_history)
    response =result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI : {response}")


print("____Message History")
print(chat_history)




