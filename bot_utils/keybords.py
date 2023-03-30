from aiogram import types


def get_menu_button():
    #настройки кнопок
    markup = types.InlineKeyboardMarkup(row_width=1)
    # Кнопки
    tv_shows = types.InlineKeyboardButton(
        'Самые популярные сериалы по версии IMDB', callback_data='tv_shows')
    add_show = types.InlineKeyboardButton(
        'Добавить сериал для отслеживания', callback_data='add_show')
    delete_show = types.InlineKeyboardButton(
        'Удалить сериал из отслеживаемого', callback_data='delete_show')
    my_shows = types.InlineKeyboardButton(
        'Проверить дату выхода следующих серий', callback_data='my_shows')
    my_shows_list = types.InlineKeyboardButton(
        'Мои сериалы', callback_data='my_shows_list'
    )
    markup.add(tv_shows, add_show, delete_show, my_shows, my_shows_list)
    return markup