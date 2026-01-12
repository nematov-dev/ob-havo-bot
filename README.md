# 🌤️ Weather City Telegram Bot

This Telegram bot allows users to check the weather for any city and save their favorite cities for quick access.  
Users can view weather data, save cities, and manage their saved city list.  
The bot is built using **Python, Aiogram, and MySQL (`pymysql`)**.

---

## 📌 Features

### User Features
* Start the bot with `/start` and register automatically
* Request weather information for any city
* Save favorite cities for later reference
* Clear saved cities list
* Access developer info using `/dev`
* Help command `/help` provides guidance on usage

### Admin / Developer Info
* Developer info accessible via `/dev` command
* Telegram contact and TapLink link included

---

## 📁 Repository Structure

```
├── bot.py               # Main bot script
├── database.py          # Database class and methods
├── weather_data.py      # Functions to fetch weather information
├── keyboards.py         # Inline and reply keyboards
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Technologies & Tools

* Python 3.11+
* [Aiogram](https://docs.aiogram.dev/) – Telegram bot framework
* [pymysql](https://pymysql.readthedocs.io/) – MySQL database connector
* [python-decouple](https://github.com/henriquebastos/python-decouple) – Manage environment variables
* MySQL – Database for users and saved cities
* Asyncio – Asynchronous message handling

---

## 🛠 Installation & Setup

1. **Clone the repository:**

```bash
git clone <repository-url>
cd Weather-City-Bot
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file in the project root and set your variables:**

```
TOKEN=<your_telegram_bot_token>
DB_NAME=<your_database_name>
DB_USER=<your_db_user>
DB_PASSWORD=<your_db_password>
DB_HOST=<your_database_host>
DB_PORT=3306
```

---

## 🚀 Running the Bot

```bash
python bot.py
```

The bot will:

* Connect to the MySQL database
* Create `users` and `cities` tables if they do not exist
* Start polling Telegram messages asynchronously

---

## 📋 Usage Guide

### For Users:

1. Start the bot with `/start` – this registers your Telegram account in the database.
2. Enter any city name to fetch weather data.
3. Save the city using the **✅ Save City** button.
4. View your saved cities list or clear it with **Clear Cities List 🗑**.
5. Access developer info using `/dev`.
6. Use `/help` for instructions and guidance.

### Example Workflow:

* `/start` → Bot greets you and registers your account  
* Type `Tashkent` → Bot shows current weather  
* Press **✅ Save City** → City is saved  
* Press **Shaharlar ro'yxatini tozalash 🗑** → Clear saved cities  

---

## 👨‍💻 Developer

**[Saidakbar Ne'matov](https://nematov.uz)**

---

## 📄 License

This project is open-source and intended for **educational and demonstration purposes**.

---
