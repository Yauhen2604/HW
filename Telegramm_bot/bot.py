import asyncio
import logging
from datetime import datetime
from random import randint

from Telegramm_bot.Filters import chat_type
from handlers import questions, witch_types, data_hadler
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from Less26_Telegram.config import token as my_token
from aiogram import F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.formatting import Bold, as_list, as_marked_list, as_marked_section, as_key_value, HashTag
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardButton
logging.basicConfig(level=logging.INFO)


# create object bota
# bot = Bot(token=my_token)
#
# # create object dispecther
# dp = Dispatcher()


async def main():
    bot = Bot(token=my_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(data_hadler.router)
    dp.include_routers(questions.router, witch_types.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
