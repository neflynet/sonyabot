from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards.inline import start_keyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    text = """
💕 **БОТИК ПОДРУЖЕК** 💕

Привет, котёнок! 
Здесь ты можешь приобрести наш приватик

📢 **Наш канал:** t.me/+IBE6ZzScE7BmMDM1

💌 **Написать в ЛС:** @ill_sonyaxxx

⭐ **Отзывы:** t.me/girlsotz

━━━━━━━━━━━━━
"""
    await message.answer(text, reply_markup=start_keyboard(), parse_mode="Markdown")

@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback: CallbackQuery):
    text = """
💕 **БОТИК ПОДРУЖЕК** 💕

Выберите раздел:
"""
    await callback.message.edit_text(text, reply_markup=start_keyboard(), parse_mode="Markdown")
    await callback.answer()
