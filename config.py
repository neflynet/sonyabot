from os import getenv
from aiogram import Bot
from dotenv import load_dotenv
from aiogram import Bot
# В config.py добавьте:
PROXY_LIST = [
    "http://45.76.132.94:8080",
    "http://103.152.112.162:80",
    "socks5://185.32.6.128:8080",
]
BOT_TOKEN = "8679512061:AAEMnEnLYcOTe8CuOyNVyD_dUY1N3JxA260"# Токен бота от @BotFather

# Ваши ссылки
CHANNEL_LINK = "https://t.me/+XxT8muj5E_sxZjUy"  # Ваш канал
REVIEWS_LINK = "t.me/girlsotz"  # Отзывы
PREVIEW_LINK = "t.me/+QX_CI_OfXu4wNGZh"  # Превью привата
CONTACT_USERNAME = "@ill_sonyaxxx"  # Личка

# Цены в Telegram Stars
PRIVATE_PRICE_STARS = 4000  # 4000 звезд (примерно 4000 RUB)
VIRTUAL_GIRLFRIEND_PRICE = 5000  # 5000 звезд

bot = Bot(token=BOT_TOKEN)