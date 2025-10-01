from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import timezone
from config.settings import CHAT_ID
from services.grok_service import generate_message
import logging


async def send_daily_message(bot):
    try:
        prompt = """
            Сгенерируй сообщение о признании в любви на день, 
            не длиннее 100 слов, в позитивном тоне, по возможности используй имя Настя
        """
        message_text = await generate_message(prompt)
        await bot.send_message(chat_id=CHAT_ID, text=message_text)
    except Exception as e:
        await bot.send_message(chat_id=CHAT_ID, text=f"Ошибка при отправке: {str(e)}")
        logging.error(f"Scheduler error: {e}")


def setup_scheduler(bot):
    scheduler = AsyncIOScheduler(timezone=timezone.utc)
    scheduler.add_job(send_daily_message, "cron", hour=5, minute=0, args=(bot,))
    scheduler.start()
    return scheduler
