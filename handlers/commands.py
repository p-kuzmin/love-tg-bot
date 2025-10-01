from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from services.grok_service import generate_message

router = Router()

def get_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Помощь", callback_data="help"),
                InlineKeyboardButton(text="Сгенерировать", callback_data="generate"),
            ]
        ]
    )
    return keyboard


@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        """
        Привет! Теперь я буду отправлять тебе каждый день признания в любви!
        """,
        reply_markup=get_keyboard(),
    )


@router.message(Command("help"))
async def help(message: types.Message):
    await message.answer(
        """
        Я отправляю признания в любви ежедневно в 10:00 ЕКБ. Напиши /generate, чтобы получить новое немедленно!
        """,
        reply_markup=get_keyboard(),
    )

@router.message(Command("generate"))
async def generate(message: types.Message):
    try:
        prompt = """
            Сгенерируй сообщение о признании в любви на день, 
            не длиннее 100 слов, в позитивном тоне, по возможности используй имя Настя, 
            не приписывай в конце отправителя, отправь только сообщение.
        """
        message_text = await generate_message(prompt)
        await message.answer(
            message_text,
            reply_markup=get_keyboard()
        )
    except Exception as e:
        await message.answer(
            f"Ошибка при генерации: {str(e)}",
            reply_markup=get_keyboard()
        )

@router.callback_query(
    lambda c: c.data in [
        "help",
        "generate"
    ]
)
async def process_callback(callback_query: types.CallbackQuery):
    if callback_query.data == "help":
        await help(callback_query.message)
    elif callback_query.data == "generate":
        await generate(callback_query.message)
    await callback_query.answer()