from datetime import datetime

import requests


API_TOKEN = "5b1e520468c63477c4e4cdac50e31ab9"

def get_weather_data(city_name: str) -> str:
    URL = f"https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {
        "appid": API_TOKEN,
        "q": city_name,
        "units": "metric",
    }
    weather_data = requests.get(url=URL, params=PARAMS)
    data = weather_data.json()

    if data["cod"] == 200:
        sunrise = str(datetime.fromtimestamp(data['sys']['sunrise']))[-8:]
        sunset = str(datetime.fromtimestamp(data['sys']['sunset']))[-8:]
        if data['main']['temp'] < 10:
            text = f"🌆 Bugun <b>{data['name']}</b> da\n\n"
            text += f"🌡 Harorat: <b>{data['main']['temp']} В°C</b>\n"
            text += f"🔻 Maks. harorat: <b>{data['main']['temp_max']} В°C</b>\n\n"
            text += f"🔺 Min. harorat: <b>{data['main']['temp_min']} В°C</b>\n"
            text += f"❗ Bosim: <b>{data['main']['pressure']} Pa</b>\n"
            text += f"💧 Namlik: <b>{data['main']['humidity']} %</b>\n"
            text += f"🌬 Shamol tezligi: <b>{data['wind']['speed']} m/s</b>\n\n"
            text += f"☀️ Quyosh chiqish vaqti: <b>{sunrise}</b>\n"
            text += f"🌥 Quyosh botish vaqti: <b>{sunset}</b>\n"
            text += f"\n\nPS: Issiqroq kiyinishingizni maslahat beraman 😊!"
        else:
            text = f"🌆 Bugun <b>{data['name']}</b> da\n\n"
            text += f"🌡 Harorat: <b>{data['main']['temp']} В°C</b>\n"
            text += f"🔻 Maks. harorat: <b>{data['main']['temp_max']} В°C</b>\n\n"
            text += f"🔺 Min. harorat: <b>{data['main']['temp_min']} В°C</b>\n"
            text += f"❗ Bosim: <b>{data['main']['pressure']} Pa</b>\n"
            text += f"💧 Namlik: <b>{data['main']['humidity']} %</b>\n"
            text += f"🌬 Shamol tezligi: <b>{data['wind']['speed']} m/s</b>\n\n"
            text += f"☀️ Quyosh chiqish vaqti: <b>{sunrise}</b>\n"
            text += f"🌥 Quyosh botish vaqti: <b>{sunset}</b>\n"

        return text
    else:
        return None
    

