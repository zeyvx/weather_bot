# Weather Bot 🌤

Telegram-бот на aiogram для получения текущей погоды по названию города.

## Возможности
- Погода по команде /weather <город>
- Температура, ощущаемая температура, описание погоды
- Обработка ошибок (город не найден, проблемы с API)

## Технологии
- Python 3.11+
- aiogram 3.x
- aiohttp
- OpenWeatherMap API

## Установка

1. Клонируй репозиторий:
git clone https://github.com/zeyvx/weather_bot.git
cd weather_bot

2. Создай виртуальное окружение и установи зависимости:
python -m venv .venv
source .venv/bin/activate  (Windows: .venv\Scripts\activate)
pip install -r requirements.txt

3. Создай файл .env в корне проекта:
BOT_TOKEN=твой_токен_от_BotFather
API=твой_ключ_от_OpenWeatherMap

4. Запусти бота:
python bot.py

## Использование
/start          — приветствие и инструкция
/weather Moscow — получить погоду в Москве
