from google import genai

from app.config import GEMINI_API_KEY
from app.prompts.prompts import build_email_prompt
from app.utils.logger import logger

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_email_reply(email: str, tone: str) -> str:

    logger.info("Generating reply | Tone=%s", tone)

    try:

        prompt = build_email_prompt(email, tone)

        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt,
        )

        if response.text:
            return response.text

        return "No response generated."

    except Exception:

        logger.exception("Gemini API Error")

        return "Sorry, something went wrong while generating the reply."