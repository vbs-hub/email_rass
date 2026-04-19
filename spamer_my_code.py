import os
import random
import smtplib
import time
from cmath import e
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.policy import SMTP
from tkinter.constants import W

from colorama import Fore, Style, init

init()


OS = "\033[38;2;181;145;227m"
OS3 = "\033[38;2;136;109;171m"
OS2 = "\033[38;2;130;153;196m"
YELLOW = "\033[38;2;245;229;153m"  # Цвет для Premium
DIM = "\033[38;2;150;150;150m"
WHITE = "\033[38;2;240;240;240m"
RESET = "\033[0m"

baner_1 = f"""
{OS}╭──────────────────────────╮
│{DIM} ✦ VBS - hub  [{WHITE}by {OS3}uiting{DIM}] {OS}│
╰──────────────────────────╯{RESET}

{OS}██╗   ██╗██████╗ ███████╗      ██╗  ██╗██╗   ██╗██████╗
██║   ██║██╔══██╗██╔════╝      ██║  ██║██║   ██║██╔══██╗
██║   ██║██████╔╝███████╗█████╗███████║██║   ██║██████╔╝
╚██╗ ██╔╝██╔══██╗╚════██║╚════╝██╔══██║██║   ██║██╔══██╗
 ╚████╔╝ ██████╔╝███████║      ██║  ██║╚██████╔╝██████╔╝
  ╚═══╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝ ╚═════╝ ╚═════╝{DIM} ✹ Corporetion ✹

                  {OS2}✦ {WHITE}Main menu {OS2}✦{RESET}
"""

baner_2 = f"""
{OS}╭──────────────────────────╮
│{DIM} ✦ VBS - hub  [{WHITE}by {OS3}uiting{DIM}] {OS}│
╰──────────────────────────╯{RESET}

{OS}██╗   ██╗██████╗ ███████╗      ██╗  ██╗██╗   ██╗██████╗
██║   ██║██╔══██╗██╔════╝      ██║  ██║██║   ██║██╔══██╗
██║   ██║██████╔╝███████╗█████╗███████║██║   ██║██████╔╝
╚██╗ ██╔╝██╔══██╗╚════██║╚════╝██╔══██║██║   ██║██╔══██╗
 ╚████╔╝ ██████╔╝███████║      ██║  ██║╚██████╔╝██████╔╝
  ╚═══╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝ ╚═════╝ ╚═════╝{DIM}  Corporetion

                  {OS2}✹ {WHITE}Spam menu {OS2}✹{RESET}
"""

baner_3 = f"""
{OS}╭──────────────────────────╮
│{DIM} ✦ VBS - hub  [{WHITE}by {OS3}uiting{DIM}] {OS}│
╰──────────────────────────╯{RESET}

{OS}██╗   ██╗██████╗ ███████╗      ██╗  ██╗██╗   ██╗██████╗
██║   ██║██╔══██╗██╔════╝      ██║  ██║██║   ██║██╔══██╗
██║   ██║██████╔╝███████╗█████╗███████║██║   ██║██████╔╝
╚██╗ ██╔╝██╔══██╗╚════██║╚════╝██╔══██║██║   ██║██╔══██╗
 ╚████╔╝ ██████╔╝███████║      ██║  ██║╚██████╔╝██████╔╝
  ╚═══╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝ ╚═════╝ ╚═════╝{DIM}  Corporetion

                  {OS2}✹ {WHITE}Profile menu {OS2}✹{RESET}
"""


email_user = "не задана"


def profile_menu():
    global email_user
    print(baner_3)

    print("Настройка профиля")

    print(
        f"{OS}[1] {DIM}Сменить почту {OS}[2] {DIM}Посмотреть данные {OS3}[0] {DIM}Выход в главное меню"
    )
    choice = input(f"{OS}✦ {WHITE}Выбор: {RESET}")
    if choice == "1":
        email_user = input(f"{OS}✦ {WHITE}Введите почту: {RESET}")
        print(f"Почта изменена на {email_user}")
        time.sleep(2)
        os.system("cls")
        print(baner_1)
        start_program()
    elif choice == "2":
        print("✦ Данные аккаунта")
        print(f"Почта: {email_user}")
        exit_menu = input(f"{OS}✦ {DIM}Нажмите Enter для выхода{RESET}")
        if exit_menu == "":
            time.sleep(2)
            os.system("cls")
            print(baner_1)
            start_program()
        else:
            print(f"{OS3}✹ {DIM}Нажмите Enter для выхода{RESET}")
    elif choice == "0":
        print(f"{OS}✹ {DIM}Выход в главное меню{RESET}")
        time.sleep(1)
        os.system("cls")
        print(baner_1)
        start_program()
    else:
        print(f"{OS}✹ {WHITE}Неверный выбор{RESET}")
        start_program()


def start_program():
    print(f"{OS3}✹ {DIM}Выберете {OS3}✹")
    print(f"{OS}[1] {DIM}Начять спам {OS3}[2] {DIM}Профиль {OS}[0] {DIM}Выход")
    choice = input(f"{OS}✦ {WHITE}Выбор: {RESET}")
    if choice == "1":
        send_email()
    elif choice == "2":
        profile_menu()
    elif choice == "0":
        print(f"{OS}✹ {DIM}Выход{RESET}")
        time.sleep(1)
        exit()
    else:
        print(f"{OS}✹ {WHITE}Неверный выбор{RESET}")
        start_program()


def send_email():
    print(f"{OS}Введите {DIM}email {OS}для атаки{RESET}")
    email = input(f"{OS}✦ {WHITE}Почта: {RESET}")

    print(f"{OS}Введите {DIM}количество вызовов{OS}")
    call = int(input(f"{OS}✦ {WHITE}Количество: {RESET}"))

    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")
    print(baner_2)

    SMTP_SERVER = "smtp.mail.ru"
    SMTP_PORT = 587
    EMAIL_ADDRESS = "ghost.he@mail.ru"
    EMAIL_PASSWORD = "LOaKbxVfsPDeKheBdOeE"
    ATAKA_EMAIL = email
    ADMIN_EMAIL = "cftctcfcfcu@mail.ru"

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Включаем шифрование
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = ADMIN_EMAIL
    msg["Subject"] = "✦ Admin Message - новый спам"
    msg.attach(
        MIMEText(f"""
╭{"─" * 5}╮
 │  ✦ Заказ на спам аккаунта:
 │    {ATAKA_EMAIL}
 │
 │  ✹ Количество вызовов: {call}
╰{"─" * 5}╯
            """)
    )
    server.send_message(msg)

    num_messeg = 1

    for _ in range(call):
        timer = random.randint(3, 10)

        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = ATAKA_EMAIL
        msg["Subject"] = f"✦ VBS: #{random.randint(1000, 9999)}"
        msg.attach(MIMEText(f"Это тестовый спам #{random.randint(1000, 9999)}"))
        server.send_message(msg)

        print(f"{OS}╭────╮{RESET}")
        print(
            f"{OS}│{DIM}[{OS}#{num_messeg}{DIM}]{OS}│ {WHITE}Отправленно: {OS}{email}{RESET}"
        )
        print(
            f"{OS}│ {DIM}-  {OS}│ {WHITE}Шлюз{DIM}: {OS}{EMAIL_ADDRESS} {WHITE}| {OS}{num_messeg}{DIM}/{call}{RESET}"
        )
        print(f"{OS}╰────╯{RESET}")

        num_messeg += 1
        print(f"{WHITE}Ждать: {OS}{timer} {DIM}секунд")
        time.sleep(timer)

    server.quit()
    print(f"{OS}✹ {DIM}Спам отправлен")

    time.sleep(2)

    clear_on = input(f"{OS}✦ {DIM}Нажмите Enter для очистки экрана")
    if clear_on == "":
        os.system("cls")
        print(baner_1)
        start_program()
    else:
        print(f"{OS}✹ {DIM}Нажмите Enter для выхода в главное меню")


if __name__ == "__main__":
    os.system("cls")
    print(baner_1)
    start_program()
