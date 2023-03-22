from aiogram import types
from aiogram.dispatcher import FSMContext

from parser.parser import manager, check_new_episode
from .keybords import get_menu_button
from state import TVShowState


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
    print(message.text)
    if 'toramp.com/' in message.text:
        with open('shows.txt', 'a') as file:
            file.write(f'{message.text}\n')
        await message.answer('успешно!')
    else:
        await message.answer('введите, пожалуйста, ссылку с toramp')
    await state.finish()


async def show_shows(callback: types.CallbackQuery):
    await callback.message.answer('ваш список сериалов')
    with open('shows.txt', 'r') as file:
        shows = file.readlines()
        for show in shows:
            # check_new_episode(show)
            await callback.message.answer(f'{show} - дата выхода: {check_new_episode(show)}')