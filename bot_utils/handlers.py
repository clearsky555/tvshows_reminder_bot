from aiogram import types
from aiogram.dispatcher import FSMContext

from database import UsersManager, engine
from parser.parser import manager, check_new_episode
from .keybords import get_menu_button
from state import TVShowState

users_manager = UsersManager(engine=engine)

async def welcome_message(message: types.Message):
    text = 'Привет, я бот для отслеживания выхода новых серий ваших любимых сериалов'
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
    await callback.message.answer('пожалуйста, вставьте ссылку сериала на toramp')
    await TVShowState.add_tv_shows.set()


async def add_tv_shows(message: types.Message, state: FSMContext):
    print(message)
    print(message.text)
    if 'toramp.com/' in message.text:
        user_id = message.from_user.id
        link = message.text
        data = {'user_id': user_id, 'link': link}
        users_manager.insert_user_show(data)

        await message.answer('успешно!')
    else:
        await message.answer('введите, пожалуйста, ссылку с toramp')
    await state.finish()


async def show_shows(callback: types.CallbackQuery):
    await callback.message.answer(f'{callback.from_user.first_name}, ваш список сериалов')
    print(callback)
    shows = users_manager.search_by_id(callback.from_user.id)
    print(shows)
    for show in shows:
        await callback.message.answer(f'{show} - дата выхода новой серии: {check_new_episode(show)}')
    # with open('shows.txt', 'r') as file:
    #     shows = file.readlines()
    #     for show in shows:
    #         # check_new_episode(show)
    #         await callback.message.answer(f'{show} - дата выхода новой серии: {check_new_episode(show)}')