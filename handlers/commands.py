from aiogram import Router, types
from aiogram.filters import Command
from services.grok_service import generate_message

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("""
        Привет! Я бот, который отправляет признания в любви!
    """)

@router.message(Command("help"))
async def help(message: types.Message):
    await message.answer("""
        Я отправляю признания в любви ежедневно в 10:00 ЕКБ. Напиши /generate, чтобы получить новое!
    """)

@router.message(Command("generate"))
async def generate(message: types.Message):
    try:
        prompt = """
            Сгенерируй сообщение о признании в любви на день, 
            не длиннее 100 слов, в позитивном тоне, по возможности используй имя Настя, 
            не приписывай в конце отправителя, отправь только сообщение.
        """
        message_text = await generate_message(prompt)
        await message.answer(message_text)
    except Exception as e:
        await message.answer(f"Ошибка при генерации: {str(e)}")