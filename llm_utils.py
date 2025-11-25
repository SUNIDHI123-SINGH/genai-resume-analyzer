# llm_utils.py
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# OPENAI_API_KEY env se hi uth jayega automatically
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def call_llm(prompt: str) -> str:
    """
    Sends a prompt to the LLM and returns the text response.
    """
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert resume and job-fit evaluator.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM error: {e}"
