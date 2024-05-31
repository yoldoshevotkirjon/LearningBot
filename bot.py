import logging
import asyncio
from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InputMediaPhoto
from Keyboards.inline import button
from Keyboards.default import phone
from aiogram.types import ReplyKeyboardRemove

# ---------------STATE---------------#
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Shogirdchalar(StatesGroup):
    name = State()
    surename = State()


class User(StatesGroup):
    loc = State()
    phone = State()


API_TOKEN = "7183171518:AAF3U7nVBvjqDCOtXcVIjtP2044oW_UwpmM"

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


image = [
    'game.jpg',
    'strike.jpg',
    'telegram.jpg'
]

son = 0


@dp.message_handler(commands=["start"])
async def startt(message: types.Message):
    await message.answer("Ismingizn kiriting")
    await Shogirdchalar.name.set()


@dp.message_handler(state=Shogirdchalar.name)
async def names(message: types.Message, state: FSMContext):
    print(message.text)
    await message.answer("Familyangizni kiriting")
    await state.finish()
    await Shogirdchalar.surename.set()


@dp.message_handler(state=Shogirdchalar.surename)
async def finishh(message: types.Message, state: FSMContext):
    print(message.text)
    await message.answer("Registratsiyadan otdingiz")
    await state.finish()


# location = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton("Locatsiya jonating", request_location=True),
#         ]
#     ],
#     resize_keyboard=True,
# )
# @dp.message_handler(commands=["loc"])
# async def loc(message: types.Message):
#     await message.answer("Locatsiyangizni yuboring" , reply_markup=location)
#     await User.loc.set()
#
# @dp.message_handler(content_types='location', state=User.loc)
# async def loc(message: types.Message, state: FSMContext):
#     await message.answer("Locatsiyangiz qabul qilindi")
#     await state.finish()
#
# @dp.message_handler(content_types='location')
# async def loc(message: types.Message, state: FSMContext):
#     await message.answer(" qabul qilindi")
#

# phone_number = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton("Telefon nomeringizni jonating", request_contact=True),
#         ]
#     ],
#     resize_keyboard=True,
# )
#
#
# @dp.message_handler(commands='phone')
# async def phone(message: types.Message):
#     await message.answer("Telefon nomeringizni jonating", reply_markup=phone_number)
#     await User.phone.set()
#
#
# @dp.message_handler(content_types='contact', state=User.phone)
# async def phone(message: types.Message, state: FSMContext):
#     await message.answer("Telefon nomeringiz qabul qilindi ")
#     await state.finish()
#
#
# @dp.message_handler(content_types='contact')
# async def phone(message: types.Message):
#     await message.answer("nomeringiz qabul qilindi ")


# @dp.message_handler(content_types=types.ContentType.CONTACT, state=Shogirdchalar.phone)
# async def contactt(message: types.Message, state: FSMContext):
#     await message.answer("Siz kontaktingizni jonatingiz", reply_markup=ReplyKeyboardRemove())
#     await state.finish()


# @dp.message_handler(commands=["start"])
# async def start(message: types.Message):
#     message1 = await message.answer("Assalomu aleykum")
#
#     await asyncio.sleep(0.5)
#     #asyncio 0.5 sekund kutib keyin ozgartiradi
#
#     await message1.edit_text("Volekum Assalom")
#
#     await asyncio.sleep(0.5)
#
#     await message1.edit_text("Yaxshimisiz")


# @dp.message_handler(commands=['start'])
# async def welcome(message: types.Message):
#     global son
#     print(son)
#     await message.answer_photo(photo=open(image[son], "rb"), reply_markup=button)
#
#
# @dp.callback_query_handler(text="next")
# async def nextt(call: types.CallbackQuery):
#     try:
#         global son
#         print(son)
#         son += 1
#         await call.message.edit_media(media=InputMediaPhoto(open(image[son], "rb")), reply_markup=button)
#     except:
#         await call.answer("Boshqa rasm qolmadi")
#
# @dp.callback_query_handler(text="back")
# async def backk(call: types.CallbackQuery):
#     try:
#         global son
#         print(son)
#         son -= 1
#         await call.message.edit_media(media=InputMediaPhoto(open(image[son], "rb")), reply_markup=button)
#     except:
#         await call.answer("Boshqa rasm qolmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
