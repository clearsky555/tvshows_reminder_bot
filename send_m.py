# # РАБОТА НАД ОТПРАВКОЙ СООБЩЕНИЙ ВЕДЕТСЯ ЗДЕСЬ
from datetime import datetime as dt
import datetime

from router import bot

# all_dates = ['данных о выходе новых серий нет', datetime.datetime(2023, 3, 26, 0, 0), 'данных о выходе новых серий нет']




async def job():
    # all_dates = []
    # with open('shows.txt', 'r') as file:
    #     shows = file.readlines()
    #     for show in shows:
    #         all_dates.append(check_new_episode(show))
    all_dates = ['данных о выходе новых серий нет', datetime.datetime(2023, 3, 26, 0, 0), datetime.datetime(2023, 3, 23, 0, 0)]

    print("I'm working...")
    current_date = dt.now().date()
    for date in all_dates:
        # print(type(date))
        if type(date) == datetime.datetime and current_date == date.date():
            text = 'сегодня выходит новая серия'
            await bot.send_message(text=text, chat_id='5782005645')
