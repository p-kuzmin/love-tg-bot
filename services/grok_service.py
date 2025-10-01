from openai import AsyncOpenAI
from config.settings import OPENROUTER_API_KEY, OPENROUTER_MODEL


grok_client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


async def generate_message(prompt: str) -> str:
    try:
        response = await grok_client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Ты помощник, который генерирует сообщения о признании в любви.",
                },
                {
                    "role": "user",
                    "content": prompt
                },
            ],
            max_tokens=100,
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Generate error: {str(e)}")
