# # РАБОТА НАД ОТПРАВКОЙ СООБЩЕНИЙ ВЕДЕТСЯ ЗДЕСЬ
from datetime import datetime as dt
import datetime

import aiogram

from parser.parser import get_show_data
from router import bot
from database import users_manager




# all_dates = ['данных о выходе новых серий нет', datetime.datetime(2023, 3, 26, 0, 0), 'данных о выходе новых серий нет']




async def job():
    all_data = users_manager.get_all_data()
    # print(all_data)
    current_date = dt.now().date()
    # all_data = [
    # (1, '5782005645', 'Новобранец (2018 — ...)', '2023-08-27 00:00:00', 'https://www.toramp.com/schedule.php?id=3551'),
    # (2, '5782005645', 'Одни из нас (2023 — ...)', 'данных о выходе новых серий нет', 'https://www.toramp.com/schedule.php?id=4458'),
    # (3, '5697579498', 'Призрак и Молли Макги (2021 — ...)', '2023-04-08 00:00:00', 'https://www.toramp.com/schedule.php?id=5691'),
    # (4, '5782005645', 'Призрак и Молли Макги (2021 — ...)', '2023-04-08 00:00:00', 'https://www.toramp.com/schedule.php?id=5691')]
    for row in all_data:
        if row[3] != 'данных о выходе новых серий нет' and datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S').date() == current_date:
            text = f'сегодня выходит новая серия {row[2]}'
            users_manager.delete_row_by_id(row[0])
            show_date = get_show_data(row[4])[1]
            data = {'user_id': row[1], 'link': row[4], 'show_title': row[2], 'show_date': show_date}
            users_manager.insert_user_show(data)
            try:
                await bot.send_message(text=text, chat_id=row[1])
            except aiogram.utils.exceptions.BotBlocked as e:
                print(f'пользователь {row[1]} заблокировал бота, ошибка {e}')

    # all_dates = []
    # all_shows = users_manager.select_all_shows()
    # all_shows = set(all_shows)
    # for show in list(all_shows):
    #     all_dates.append(check_new_episode(show))
    # for date in all_dates:
    #     print(date)
    # print(all_dates)
    # all_dates = [['https://www.toramp.com/schedule.php?id=4458', 'данных о выходе новых серий нет'], ['https://www.toramp.com/schedule.php?id=5509', datetime.datetime(2023, 3, 28, 0, 0)], ['https://www.toramp.com/schedule.php?id=3463', datetime.datetime(2023, 3, 28, 0, 0)]]
    all_dates = [['https://www.toramp.com/schedule.php?id=6496', 'данных о выходе новых серий нет'], ['https://www.toramp.com/schedule.php?id=4390', datetime.datetime(2023, 3, 30, 0, 0)], ['https://www.toramp.com/schedule.php?id=5694', 'данных о выходе новых серий нет'], ['https://www.toramp.com/schedule.php?id=3463', datetime.datetime(2023, 4, 2, 0, 0)], ['https://www.toramp.com/schedule.php?id=4458', 'данных о выходе новых серий нет']]



    print("job working...")
    # current_date = dt.now().date()
    # all_id = []
    # for d in all_dates:
    #     if type(d[1]) == datetime.datetime and current_date == d[1].date():
    #         # print(d[1].date())
    #         # print(d[0])
    #         users_id = users_manager.get_users_id(d[0])
    #         for id in users_id:
    #             print(id)
    #             all_id.append(id)
    all_id = [[['5782005645'], 'https://www.toramp.com/schedule.php?id=5509'], [['186070350', '5782005645'], 'https://www.toramp.com/schedule.php?id=3463']]
    # for row in all_id:
    #     print(row)
    #     for id in row[0]:
    #         text = f'сегодня выходит новая серия {row[1]}'
    #         try:
    #             await bot.send_message(text=text, chat_id=id)
    #         except aiogram.utils.exceptions.BotBlocked as e:
    #             print(f'пользователь {id} заблокировал бота, ошибка {e}')