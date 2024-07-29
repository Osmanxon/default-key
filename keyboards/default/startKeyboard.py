from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart=ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Contact', request_contact=True),
            KeyboardButton(text='Location', request_contact=True),
        ],
    ],
    resize_keyboard=True
)