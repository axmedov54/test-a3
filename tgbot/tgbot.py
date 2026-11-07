import asyncio
from os import getenv
from aiogram import Bot, Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from button import *
BOT_TOKEN = "8567535122:AAFgsVvNjkmeHiovrAvmTuzsu6_CCeWiSDQ"
TOKEN = BOT_TOKEN
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp =Dispatcher()


@dp.message(Command("start"))
async def camanda (message:Message):
    await message.answer("Salom Kino turini tallang",reply_markup=menu)
    

@dp.message(F.text == "Janggovar")
async def jang (message:Message):
    await message.answer("Kinolar royxati",reply_markup=jang_button)

@dp.message(F.text == "Alfa")
async def jang (message:Message):
    await message.answer_video(video="https://t.me/Kinolark/9472",reply_markup=jang_button)


@dp.message(F.text == "Qasoskorlar")
async def jang (message:Message):
    await message.answer("Kinolar royxati",reply_markup=qasos_button)


@dp.message(F.text == "Qasoskorlar-1")
async def jang (message:Message):
    await message.answer_video(video="https://t.me/qasoskorlar_kinol/22",caption="""
    Nomi: BIRINCHI QASOSKOR / KAPITAN AMERIKA
    Mamlakat: AQSH
    Janr: боевик, триллер, Fantastika
    Chiqarilgan yili: 2011 yil""",reply_markup=qasos_button)



@dp.message(F.text == "Qasoskorlar-2")
async def jang (message:Message):
    await message.answer_video(video="https://t.me/qasoskorlar_kinol/26",caption="""
Fantastik to'rtlik 2: Kumush Surfer bosqini
Yili: 2007
Mamlakat: AQSH, Германия
Yosh: 13+
Janr: Tarjima kino / Sarguzashtlar / Boevik / Fantastika / Fentezy""",reply_markup=qasos_button)



@dp.message(F.text == "Qasoskorlar-3")
async def jang (message:Message):
    await message.answer_video(video="https://t.me/qasoskorlar_kinol/24",caption="""
Nomi: BIRINCHI QASOSKOR 3 / KAPITAN AMERIKA 3
Mamlakat: AQSH
Janr: боевик, триллер, Fantastika
Chiqarilgan yili: 2016 yil""",reply_markup=qasos_button)


@dp.message(F.text == "Qasoskorlar-4")
async def jang (message:Message):
    await message.answer_video(video="https://t.me/qasoskorlar_kinol/17",caption=""""
    Qasoskorlar 4: Intiho 
Davlati: AQSH
Yili: 2019
Jangari Fantastika""",reply_markup=qasos_button)


@dp.message(F.text == "Qasoskorlar-5")
async def jang (message:Message):
    await message.answer_video(video="https://t.me/qasoskorlar_kinol/18",caption="""
Nomi: Ovchi Kreyven / Kraven
Mamlakat: AQSH
Janr: боевик, триллер, Fantastika
Chiqarilgan yili: 2024 yil""",reply_markup=qasos_button)


@dp.message(F.text == "Qasoskorlar-6")
async def jang (message:Message):
    await message.answer_video(video="https://t.me/qasoskorlar_kinol/28",caption="""
Fantastik to'rtlik: Ilk qadamlar
Yili: 2025
Mamlakat: AQSH, Германия
Yosh: 13+
Janr: Tarjima kino / Sarguzashtlar / Boevik / Fantastika / Fentezy""",reply_markup=qasos_button)



    
    
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())





