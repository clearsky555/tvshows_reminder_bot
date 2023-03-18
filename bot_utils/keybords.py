from aiogram import types


def get_menu_button():
    #настройки кнопок
    markup = types.InlineKeyboardMarkup(row_width=1)
    # Кнопки
    tv_shows = types.InlineKeyboardButton(
        'Самые популярные сериалы по версии IMDB', callback_data='tv_shows')
    add_show = types.InlineKeyboardButton(
        'Добавить сериал для отслеживания', callback_data='add_show')
    my_shows = types.InlineKeyboardButton(
        'Мои сериалы', callback_data='my_shows')
    markup.add(tv_shows, add_show, my_shows)
    return markup