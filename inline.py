from aiogram.utils.keyboard import InlineKeyboardBuilder

def start_keyboard():
    """Главное меню"""
    builder = InlineKeyboardBuilder()
    builder.button(text="📢 Наш канал", url="https://t.me/+IBE6ZzScE7BmMDM1")
    builder.button(text="⭐ Отзывы", url="https://t.me/girlsotz")
    builder.button(text="💎 Купить приват", callback_data="buy_privat")
    builder.button(text="👤 Виртуальная девушка", callback_data="virtual_girl")
    builder.adjust(1, 1, 2, 1)
    return builder.as_markup()

def privates_menu_keyboard():
    """Меню приватов"""
    builder = InlineKeyboardBuilder()
    builder.button(text="🔥 Наш приватик (4000⭐)", callback_data="show_privat_4000")
    builder.button(text="💕 Виртуальная девушка (5000⭐)", callback_data="virtual_girl")
    builder.button(text="🔙 Назад", callback_data="back_to_menu")
    builder.adjust(1, 1, 1)
    return builder.as_markup()

def privat_4000_keyboard():
    """Клавиатура для привата за 4000"""
    builder = InlineKeyboardBuilder()
    builder.button(text="👁 Превью привата", url="https://t.me/+QX_CI_OfXu4wNGZh")
    builder.button(text="⭐ Оплатить 4000⭐", pay=True)
    builder.button(text="🔙 Назад", callback_data="back_to_menu")
    builder.adjust(1, 1, 1)
    return builder.as_markup()

def virtual_girl_keyboard():
    """Клавиатура для виртуальной девушки"""
    builder = InlineKeyboardBuilder()
    builder.button(text="⭐ Оплатить 5000⭐", pay=True)
    builder.button(text="🔙 Назад", callback_data="back_to_menu")
    builder.adjust(1, 1)
    return builder.as_markup()
