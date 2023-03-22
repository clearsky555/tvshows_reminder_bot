# РАБОТА НАД ОТПРАВКОЙ СООБЩЕНИЙ ВЕДЕТСЯ ЗДЕСЬ
# from datetime import datetime
#
# from aiogram import Bot
# import schedule
#
# from config import TOKEN
# from parser.parser import check_new_episode
#
# bot = Bot(token=TOKEN)
#
#
#
# all_dates = []
# with open('shows.txt', 'r') as file:
#     shows = file.readlines()
#     for show in shows:
#         all_dates.append(check_new_episode(show))
# print(all_dates)
# def send_message():
#     current_date = datetime.now().date()
#     for date in all_dates:
#         if current_date == date.date():
#             chat_id = 'USER_CHAT_ID_HERE'
#             bot.send_message(chat_id=chat_id, text='Сообщение для пользователя')
#         else:
#             chat_id = 'USER_CHAT_ID_HERE'
#
#             bot.send_message(chat_id=chat_id, text='данных по сериалам пока нет')
#
#
#
# # Запускаем функцию send_message каждый день в 12:00
# schedule.every().day.at("18:07").do(send_message)
#
# # Запускаем бесконечный цикл, чтобы функция send_message могла выполняться периодически
# while True:
#     schedule.run_pending()
