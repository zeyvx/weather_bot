# Weather Bot

Telegram-бот на aiogram для получения текущей погоды по названию города.

## Возможности

- Получение погоды по команде `/weather <город>`
- Температура и ощущаемая температура
- Описание погоды на русском языке
- Обработка ошибок (город не найден, неверный API-ключ)

## Технологии

- Python 3.11+
- aiogram 3.x
- aiohttp
- OpenWeatherMap API
- python-dotenv

## Установка

1. Клонируй репозиторий:

```bash
git clone https://github.com/zeyvx/weather_bot.git
cd weather_bot
```

2. Создай виртуальное окружение и установи зависимости:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Создай файл `.env` в корне проекта:

```env
BOT_TOKEN=твой_токен_от_BotFather
API=твой_ключ_от_OpenWeatherMap
```

4. Запусти бота:

```bash
python bot.py
```

## Использование

- `/start` — приветствие и инструкция
- `/weather Moscow` — получить погоду в Москве
- `/weather Namangan,UZ` — можно указывать код страны для точности
