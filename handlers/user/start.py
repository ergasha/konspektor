from aiogram import types
from filters.admins import AdminFilter
from loader import bot, dp
from utils.db_api.sqlite import db
from loader import dp
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    web_app_url = "https://osonyoz-web.vercel.app/"
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Ilovani ochish", web_app=WebAppInfo(url=web_app_url))
    )
    await message.answer_photo(photo='https://t.me/yuzkashop/1153',caption=f"Salom *{message.from_user.full_name}* botimizga xush kelibsiz\n\nUshbu mini ilova yordamida siz endi telegramdan chiqmay turib konspekt qila olasiz !\n\nMuhimi hech qanday dastur yuklab olmasdan turib !",parse_mode='markdown', reply_markup=keyboard)



