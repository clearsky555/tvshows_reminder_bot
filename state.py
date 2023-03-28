from aiogram.dispatcher.filters.state import StatesGroup, State


class TVShowState(StatesGroup):
    add_tv_shows = State()
    remove_tv_shows = State()