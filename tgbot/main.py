import asyncio
from os import getenv
from aiogram import Bot, Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message,CallbackQuery,InputMediaPhoto

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from buttons import *
BOT_TOKEN = "8767350211:AAHCQ7vzR1IN1GP0xjLYJfoB63l03SnSdd4"
TOKEN = BOT_TOKEN
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp =Dispatcher()

@dp.message(Command("start"))
async def camanda (message:Message):
    await message.answer_photo(photo="https://play-lh.googleusercontent.com/71p-UfRjVorazYBsery8O0O6K3bXArmLXrcd7H6jFBs2IStH88UNbbXfAhDhmUobGIrndMC12xfRNCKbX1Ls9w",caption="Salom ovqat tallang",reply_markup=menu)
    
    
@dp.callback_query(F.data == "milliytaomlar")
async def osh(call: CallbackQuery):
    await call.message.edit_media(
        media=InputMediaPhoto(media="https://uzbekistan.travel/storage/app/media/wepb/gastro_turizm/cropped-images/%D0%94%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD%20%D0%B1%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-0-0-0-0-1740051502.webp"),reply_markup=milliy_button)
    await call.answer("Milliy taomlar tanlandi ✅")
    
    
@dp.callback_query(F.data == "osh")
async def osh(call: CallbackQuery):
    await call.message.edit_media(
        media=InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXXs1g3ojp0bcfL3ywZyV6Da9Zw-KMpZkIZlbO_H15dCVAoRkwrmzfLtRB&s=10"),reply_markup=milliy_button)
    await call.answer("osh tanlandi ✅")
    
    
@dp.callback_query(F.data == "somsa")
async def osh(call: CallbackQuery):
    await call.message.edit_media(
        media=InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoorRTz5rqj5r5Vo_xpRLGFF4yanWI6-VYj8IZOYhpxefNdSE0xTRlNP8&s=10"),reply_markup=milliy_button)
    await call.answer("somsa tanlandi ✅")
       

@dp.callback_query(F.data == "shashlik")
async def osh(call: CallbackQuery):
    await call.message.edit_media(
        media=InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyllyeheUvsg0zm3ABBi0r2yEx3iYiipWwF7D9sIt1Jw&s=10"),reply_markup=milliy_button)
    await call.answer("Shashlik tanlandi ✅")
       


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())