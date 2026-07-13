from google import genai
from google.genai.types import GenerateContentConfig

from app.agent.prompts import SYSTEM_PROMPT
from app.config.settings import get_settings

settings = get_settings()

client = genai.Client(
    api_key=settings.gemini_api_key,
)


async def generate(prompt: str) -> str:
    """
    Send a prompt to Gemini and return the response text.
    """

    response = await client.aio.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config=GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
        ),
    )

    return response.text
