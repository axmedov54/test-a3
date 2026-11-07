import asyncio
from aiogram import Bot,Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

BOT_TOKEN ="8767350211:AAFhNnWamcbG4tl1RyXFSuoW6t1YTiUwGlE"
TOKEN = BOT_TOKEN
dp= Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

@dp.message(Command("start"))
async def start (message:Message):
    await message.answer("Salom Xushkelipsiz Kinolar Olami")





async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())