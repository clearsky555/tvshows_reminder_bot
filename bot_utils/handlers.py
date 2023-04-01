from aiogram import types
from aiogram.dispatcher import FSMContext

from database import UsersManager, engine
from parser.parser import manager, get_show_data
from .keybords import get_menu_button
from state import TVShowState

users_manager = UsersManager(engine=engine)

async def welcome_message(message: types.Message):
    text = 'Здравствуйте, я бот для отслеживания выхода новых серий ваших любимых сериалов. Когда выйдет новый эпизод, я отправлю вам сообщение'
    markup = get_menu_button()
    await message.answer(text, reply_markup=markup)


async def get_tv_shows(callback: types.CallbackQuery):
    await callback.message.answer('выдаем список сериалов...')
    shows = manager.get_shows()
    text = ''
    for show in shows:
        text += f'{show[1]}) <a href="{show[5]}">{show[2]}</a>, {show[3]}, rating: {show[4]}\n\n'

    await callback.message.answer(text, parse_mode='HTML')


async def set_tv_shows(callback: types.CallbackQuery):
    text = f'пожалуйста, вставьте ссылку сериала на <a href="https://www.toramp.com/">toramp</a>'
    await callback.message.answer(text, parse_mode='HTML')
    await TVShowState.add_tv_shows.set()


async def add_tv_shows(message: types.Message, state: FSMContext):
    print(message)
    print(message.text)
    users_manager.create_table()
    await message.answer('запись данных...')

    if 'toramp.com/' in message.text:
        user_id = message.from_user.id

        link = message.text

        show_title = get_show_data(message.text)[2]
        show_title = show_title.replace('\t\t\t', ' ')
        show_title = show_title.replace('\nсериал', '')

        show_date = get_show_data(message.text)[1]

        data = {'user_id': user_id, 'link': link, 'show_title': show_title, 'show_date': show_date}
        users_manager.insert_user_show(data)

        await message.answer('успешно!')
    else:
        await message.answer('Что-то не так... Нажмите снова "Добавить сериал для отслеживания" и введите, пожалуйста, ссылку с toramp')
    await state.finish()


async def delete_show(callback: types.CallbackQuery):
    await callback.message.answer('вставьте ссылку на сериал, который хотите удалить')
    await TVShowState.remove_tv_shows.set()


async def remove_tv_shows(message: types.Message, state: FSMContext):
    print(message)
    print(message.text)
    if 'toramp.com/' in message.text:
        user_id = message.from_user.id
        link = message.text.strip()
        users_manager.delete_show_from_db(user_id, link)

        await message.answer(f'{message.text} успешно удалён из базы данных')
    else:
        await message.answer('Что-то не так... Нажмите снова "Удалить сериал из отслеживаемого" и введите, пожалуйста, ссылку с toramp')
    await state.finish()

async def show_shows(callback: types.CallbackQuery):
    await callback.message.answer(f'{callback.from_user.first_name}, проверяем выход новых серий...')
    print(callback)
    shows = users_manager.search_by_id(callback.from_user.id)
    print(shows)
    for show in shows:
        title = users_manager.get_show_title_from_db(show)
        date = get_show_data(show)[1]
        try:
            formatted_date = date.strftime('%d %B %Y')
            await callback.message.answer(f'{title} - дата выхода новой серии: {formatted_date}')
        except AttributeError:
            await callback.message.answer(f'{title} - {date}')


async def user_shows_list(callback: types.CallbackQuery):
    await callback.message.answer(f'{callback.from_user.first_name}, ваш список сериалов')
    all_shows = users_manager.get_all_shows_by_id(callback.from_user.id)
    message = ''
    for i, show in enumerate(all_shows):
        message += f'{i + 1}. {show}\n'
    await callback.message.answer(message)


# ФУНКЦИИ ДЛЯ КОМАНД

async def get_tv_shows_c(message: types.Message):
    await message.answer('выдаем список сериалов...')
    shows = manager.get_shows()
    text = ''
    for show in shows:
        text += f'{show[1]}) <a href="{show[5]}">{show[2]}</a>, {show[3]}, rating: {show[4]}\n\n'

    await message.answer(text, parse_mode='HTML')

async def set_tv_shows_c(message: types.Message):
    text = f'пожалуйста, вставьте ссылку сериала на <a href="https://www.toramp.com/">toramp</a>'
    await message.answer(text, parse_mode='HTML')
    await TVShowState.add_tv_shows.set()

async def delete_show_c(message: types.Message):
    await message.answer('вставьте ссылку на сериал, который хотите удалить')
    await TVShowState.remove_tv_shows.set()

async def show_shows_c(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, проверяем выход новых серий...')
    shows = users_manager.search_by_id(message.from_user.id)
    # print(shows)
    for show in shows:
        title = users_manager.get_show_title_from_db(show)
        date = get_show_data(show)[1]
        try:
            formatted_date = date.strftime('%d %B %Y')
            await message.answer(f'{title} - дата выхода новой серии: {formatted_date}')
        except AttributeError:
            await message.answer(f'{title} - {date}')

async def user_shows_list_c(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, ваш список сериалов')
    all_shows = users_manager.get_all_shows_by_id(message.from_user.id)
    shows_list = ''
    for i, show in enumerate(all_shows):
        shows_list += f'{i + 1}. {show}\n'
    await message.answer(shows_list)