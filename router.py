from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from config import TOKEN
from bot_utils import handlers as hs
from state import TVShowState


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


#Router
#commands
dp.register_message_handler(hs.welcome_message, commands=['start'])
dp.register_message_handler(hs.get_tv_shows_c, commands=['get_tv_shows'])
dp.register_message_handler(hs.set_tv_shows_c, commands=['set_tv_shows'])
dp.register_message_handler(hs.delete_show_c, commands=['delete_show'])
dp.register_message_handler(hs.show_shows_c, commands=['check_dates'])
dp.register_message_handler(hs.user_shows_list_c, commands=['my_shows'])


#text messages
dp.register_message_handler(
    hs.add_tv_shows,
    content_types=['text'],
    state=TVShowState.add_tv_shows)

dp.register_message_handler(
    hs.remove_tv_shows,
    content_types=['text'],
    state=TVShowState.remove_tv_shows
)

#callbacks
dp.register_callback_query_handler(
    hs.get_tv_shows,
    lambda c: c.data == 'tv_shows'
)

dp.register_callback_query_handler(
    hs.set_tv_shows,
    lambda c: c.data == 'add_show'
)

dp.register_callback_query_handler(
    hs.show_shows,
    lambda c: c.data == 'my_shows'
)

dp.register_callback_query_handler(
    hs.delete_show,
    lambda c: c.data == 'delete_show'
)

dp.register_callback_query_handler(
    hs.user_shows_list,
    lambda c: c.data == 'my_shows_list'
)