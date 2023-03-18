from aiogram import types

from parser.parser import manager
from .keybords import get_menu_button


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