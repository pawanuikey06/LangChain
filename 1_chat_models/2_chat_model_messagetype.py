from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os


load_dotenv()


api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    print("API Key not found in .env file")
else:
    print(f"API Key: {api_key}")


llm = ChatMistralAI(api_key=api_key, model="mistral-large-latest")


message = [
    SystemMessage("You are an Expert in Social media Content Strategy"),
    HumanMessage("Give a Short tip to create engaging posts on Instagram"),
    AIMessage("Here's a short tip to create engaging posts on Instagram **Focus on 'The 3 E's' – Educate, Entertain, or Engage**\n\n1. **Educate**: Share informative content that teaches your audience something new. This could be tips, tricks, how-to's, or interesting facts related to your niche. Examples include:\n   - Infographics\n   - Carousel posts with step-by-step guides\n   - Short tutorial videos or Reels\n\n2. **Entertain**: Post content that amuses or inspires your audience. This can be funny memes, inspiring quotes, or visually appealing images and videos. Examples include:\n   - Humorous skits or memes\n   - Aesthetically pleasing photos\n   - Inspirational stories or quotes\n\n3. **Engage**: Encourage your audience to interact with your posts. Ask questions, run polls, or create content that prompts users to tag friends or share their own experiences. Examples include:\n   - 'This or That' posts\n   - 'Caption This' photos\n   - 'Share your story' prompts\n\n**Bonus Tip**: Use relevant hashtags, engaging captions, and call-to-action statements to increase the reach and engagement of your posts.\n\nBy focusing on at least one of 'The 3 E's' for each post, you'll create engaging content that resonates with your Instagram audience. Good luck!"),
    HumanMessage("Hello there")
]

# Invoke the model with the message
result = llm.invoke(message)

# Print the AI response
print(result.content)
