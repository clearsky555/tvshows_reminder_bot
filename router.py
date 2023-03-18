from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from config import TOKEN
from bot_utils import handlers as hs


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


#Router
#commands
dp.register_message_handler(hs.welcome_message, commands=['start'])


#callbacks
dp.register_callback_query_handler(
    hs.get_tv_shows,
    lambda c: c.data == 'tv_shows'
)