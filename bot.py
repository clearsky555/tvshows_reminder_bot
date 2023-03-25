import asyncio

from aiogram import executor

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


sch.every().day.at('18:39').do(job)
thread = threading.Thread(target=run_schedule)
thread.start()



if __name__ == '__main__':
    print('проверка')
    loop = asyncio.get_event_loop()
    loop.create_task(job())
    executor.start_polling(dp, skip_updates=True)
    print('код исполняется дальше...')
