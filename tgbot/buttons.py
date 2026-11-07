from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,WebAppData

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Milliy Taomlar 🥧",callback_data="milliytaomlar"),InlineKeyboardButton(text="Fast-Food 🍔",callback_data="fastfood")],
        [InlineKeyboardButton(text="Disert 🍰",callback_data="milliytaomlar"),InlineKeyboardButton(text="Ichimliklar 🍷",callback_data="ichimliklar")],
    ]
)



milliy_button =  InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Osh",callback_data="osh"),InlineKeyboardButton(text="Shashlik",callback_data="shashlik")],
        [InlineKeyboardButton(text="Somsa",callback_data="somsa")],
    ]
)

