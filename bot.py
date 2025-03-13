from asyncio import run
from logging import basicConfig, INFO

from aiogram.filters.command import CommandStart
from aiogram.types import Message, CallbackQuery,ReplyKeyboardRemove
from aiogram import Bot, Dispatcher
from aiogram import F
from decouple import config

from weather_data import get_weather_data
from keyboards import generate_save_city_menu, generate_cities_menu,generate_dev_menu
from database import db

TOKEN = config("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    telegram_id = message.from_user.id
    username = message.from_user.username
    fullname = message.from_user.full_name

    try:
        db.register_user(telegram_id, username, fullname)
        await message.answer(text=f"<b>Assalomu alaykum {message.from_user.full_name} 🙌🏻\n\n Marxamat o'zingizga kerakli biror shahar nomini kiriting ⤵️ </b>",
                            parse_mode="HTML")
    except:
        await message.answer(text="<b>Marxamat o'zingizga kerakli biror shahar nomini kiriting ⤵️ </b>", parse_mode="HTML")

@dp.message(F.text == "/help")
async def help(message: Message):
    await message.answer("<b>1. Botni ishga tushurish uchun /start buyrug'ini kiriting.\n\n2. Biror shahar nomini kiriting.\n\n3. Shaharni saqlash uchun '✅ Shaharni saqlash' tugmasidan foydalaning.\n\n4. Xato va kamchiliklar bo'lsa @n_saidakbar bilan bog'laning!</b>", parse_mode="HTML")

@dp.message(F.text == "/dev")
async def help(message: Message):
    await message.answer("<b>👨🏻‍💻 Bot yaratuvchisi: Ne'matov Saidakbar\n\n🔵 Telegram: @N_Saidakbar\n🔗 TapLink: taplink.cc/Nematov.dev</b>", parse_mode="HTML",reply_markup=generate_dev_menu())


@dp.message(F.text == "Shaharlar ro'yxatini tozalash 🗑")
async def clear_cities_list(message: Message):
    telegram_id = message.from_user.id
    user_id = db.get_user(telegram_id)

    db.clear_cities_list(user_id.get("id"))
    await message.answer(text="<b>Shaharlar ro'yxati tozalandi ✅</b>",reply_markup=ReplyKeyboardRemove(),parse_mode="HTML")
    await message.answer(text="<b>Marxamat o'zingizga kerakli biror shahar nomini kiriting: </b>", parse_mode="HTML")

    

@dp.message()
async def answer_weather_data(message: Message):

    city_name = message.text
    data = get_weather_data(city_name=city_name)

    if data:
        await message.answer(text=data, parse_mode="HTML", reply_markup=generate_save_city_menu(city_name=city_name))
    else:
        await message.answer(text="<b>🤷🏻‍♂️ Bunday shahar mavjud emas</b>",
                             parse_mode="HTML")



@dp.callback_query()
async def save_city(call: CallbackQuery):
    city_name = call.data.split(":")[-1]
    telegram_id = call.from_user.id

    try:
        db.register_city(telegram_id, city_name.title())
        await call.message.answer(text="Shahar saqlandi ✅", reply_markup=generate_cities_menu(telegram_id=call.from_user.id))
    except:
        await call.answer(text="Shahar allaqachon saqlangan 😉", show_alert=True)


async def main():
    # basicConfig(level=INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())