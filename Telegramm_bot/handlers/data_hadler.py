from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters import Command

from Telegramm_bot.Filters.chat_type import ChatTypeFilter

router = Router()


@router.message(
    ChatTypeFilter(chat_type=['group', 'supergroup']),
    Command('dice')
)
async def dice(message):
    await message.answer_dice(emoji=DiceEmoji.DICE)


@router.message(
    ChatTypeFilter(chat_type=['group', 'supergroup']),
    Command('sport')
)
async def sport(message):
    await message.answer_dice(emoji=DiceEmoji.FOOTBALL)
