from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#00 Kirish"),
            KeyboardButton(text="#01 Pycharmni o'rnatish"),
            KeyboardButton(text="#02 Hello World"),
        ],
        [
            KeyboardButton(text="Orqaga"),
            KeyboardButton(text="Boshiga"),
        ],
    ],
    resize_keyboard=True
)