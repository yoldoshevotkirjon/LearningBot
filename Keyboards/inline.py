from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Oldinga", callback_data="next"),
            InlineKeyboardButton("Orqaga", callback_data="back"),
        ]
    ]
)
