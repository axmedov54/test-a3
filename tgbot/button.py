from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Janggovar"),KeyboardButton(text="Ramantic")],
        [KeyboardButton(text="Serial"),KeyboardButton(text="Ujis")],
    ],resize_keyboard=True
)

jang_button =  ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Alfa"),KeyboardButton(text="Qasoskorlar"),KeyboardButton(text="Forjas")],
        [KeyboardButton(text="Jon Uik"),KeyboardButton(text="Transformerla"),KeyboardButton(text="Boyka")],
    ],resize_keyboard=True
)

qasos_button =  ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Qasoskorlar-1"),KeyboardButton(text="Qasoskorlar-2"),KeyboardButton(text="Qasoskorlar-3")],
        [KeyboardButton(text="Qasoskorlar-4"),KeyboardButton(text="Qasoskorlar-5"),KeyboardButton(text="Qasoskorlar-6")],
    ],resize_keyboard=True
)