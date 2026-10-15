import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm(model: str = "openai/gpt-oss-20b", temperature: float = 0.1):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file.")
    
    return ChatGroq(
        model=model,
        temperature=temperature,
        api_key=api_key
    )