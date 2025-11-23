from langchain_groq import ChatGroq
import os
from prompts import CAPTION_PROMPT
from utils import clean_text
from dotenv import load_dotenv

# Load API key
load_dotenv()

class CaptionAgent:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )

    def generate(self, topic, category, tone):
        prompt = CAPTION_PROMPT.format(
            topic=topic,
            category=category,
            tone=tone
        )
        response = self.llm.invoke(prompt)
        return clean_text(response.content)
