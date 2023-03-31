import asyncio

from aiogram import executor

from parser.parser import launching_parser
from router import dp
from send_m import job

import schedule as sch
import time
import threading
import tracemalloc
tracemalloc.start()


def run_schedule():
    while True:
        sch.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    print('проверка')
    sch.every().tuesday.at('13:25').do(launching_parser)
    sch.every().day.at('22:10').do(job)
    thread = threading.Thread(target=run_schedule)
    thread.start()
    loop = asyncio.get_event_loop()
    loop.create_task(job())
    executor.start_polling(dp, skip_updates=True)
    thread.join()
    print('код исполняется дальше...')
