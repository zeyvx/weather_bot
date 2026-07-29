from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import aiohttp
from os import getenv
from dotenv import load_dotenv

load_dotenv()
API = getenv('API')

router = Router()

def get_weather_emoji(description):
    description = description.lower()
    if "ясно" in description:
        return "☀️"
    elif "облач" in description or "пасмурно" in description:
        return "☁️"
    elif "дожд" in description:
        return "🌧"
    elif "снег" in description:
        return "❄️"
    elif "гроза" in description:
        return "⛈"
    elif "туман" in description:
        return "🌫"
    else:
        return "🌤"


async def get_weather(city, api):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api, "units": "metric", "lang": "ru"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            data = await resp.json()

            if resp.status != 200:
                return f"Не нашёл город {city}"

            name = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            desc = data["weather"][0]["description"]
            emoji = get_weather_emoji(desc)

            return (
                f"📍 <b>{name}, {country}</b>\n\n"
                f"🌡 Температура: <b>{round(temp)}°C</b>\n"
                f"🤔 Ощущается как: <b>{round(feels_like)}°C</b>\n"
                f"{emoji} {desc.capitalize()}"
            )
        
@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Добро пожаловать! Для получение информации о погоде напишите:\n\n/weather (Название города)")

@router.message(F.text.startswith('/weather'))
async def weather(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.answer("Правильный формат: /weather (название города)")
        return
    city = parts[1]
    await message.answer(f"Ищу погоду для города: {city}")

    answer = await get_weather(city, API)
    await message.answer(answer, parse_mode='HTML')
