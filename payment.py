from aiogram import Router, F
from aiogram.types import Message, PreCheckoutQuery
from aiogram.filters import Command

router = Router()

@router.pre_checkout_query()
async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)

@router.message(F.successful_payment)
async def success_payment_handler(message: Message):
    payment = message.successful_payment
    await message.answer(
        "🥳 **Оплата прошла успешно!**\n\n"
        "🔗 Ваша ссылка: t.me/+IBE6ZzScE7BmMDM1\n"
        "💌 ЛС: @ill_sonyaxxx",
        parse_mode="Markdown"
    )

@router.message(Command("paysupport"))
async def pay_support_handler(message: Message):
    await message.answer("💳 **Поддержка по платежам:** @ill_sonyaxxx")
