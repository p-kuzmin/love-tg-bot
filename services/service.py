from openai import AsyncOpenAI
from config.settings import ROUTER_API_KEY, ROUTER_MODEL


client = AsyncOpenAI(
    api_key=ROUTER_API_KEY,
    base_url="https://routerai.ru/api/v1"
)


async def generate_message(prompt: str) -> str:
    try:
        response = await client.chat.completions.create(
            model=ROUTER_MODEL,
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
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Generate error: {str(e)}")
