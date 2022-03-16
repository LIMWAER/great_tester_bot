import platform
from datetime import datetime

from aiogram import types
from asyncpg import Connection
from asyncpg.exceptions import UniqueViolationError

from load_all import dp, db


class DBCommands:
    pool: Connection = db
    ADD_NEW_USER = f"insert into users(chat_id, username, full_name)" \
                   f"values ($1, $2, $3)"
    CHECK_LOG = f"select log_id, users.username, info, date from log " \
                f"join users on users.chat_id=log.chat_id"
    ADD_ACTIVITY_INTO_LOG = f"insert into log(chat_id, info, date)" \
                            f"values ($1, $2, $3)"


async def add_new_user(self):
    user = types.User.get_current()
    chat_id = user.id
    username = user.username
    fullname = user.full_name
    args = chat_id, username, fullname
    command = self.ADD_NEW_USER
    try:
        record_id = await self.pool.fetchval(command, *args)
    except UniqueViolationError:
        pass


async def check_log(self):
    command = self.CHECK_LOG
    rows = await self.pool.fetch(command)
    data = [list(row) for row in rows]
    return data


async def add_activity(self, message: types.Message, date=None):
    user = types.User.get_current()
    chat_id = user.id
    command = self.ADD_ACTIVITY_INTO_LOG
    text = message
    await self.pool.fetchval(command, chat_id, text, date)


database = DBCommands()


@dp.message_handler(commands=['start'])
async def register_user(message: types.Message):
    user = types.User.get_current().username
    text = f"Привет, {user}!\n" \
           f"Я слежу за тобой."
    await add_new_user(database)
    await message.answer(text)


@dp.message_handler(commands=['check'])
async def check_os(message: types.Message):
    await message.answer(f'Current os: {platform.system()} {platform.release()}')


@dp.message_handler(commands=['log'])
async def show_log(message: types.Message):
    logs = await check_log(database)
    text ='Лог:\n'+'\n'.join([', '.join(map(str, row)) for row in logs])
    await message.answer(text)


@dp.message_handler(content_types=['text'])
async def add_to_log(message: types.Message):
    text = f"Понятно.\nЗапишу в свою тетрадочку."
    await add_activity(database, message.text, date=datetime.now())
    await message.answer(text)