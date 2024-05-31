from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Telefon nomeringizni jonating", request_contact=True),
        ]
    ]
)

