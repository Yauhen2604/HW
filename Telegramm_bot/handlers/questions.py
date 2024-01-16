from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
import random
from Telegramm_bot.keyboards.start_questions import answer_questions_kb

router = Router()


@router.message(Command('start'))
async def start(message):
    await message.answer(
        'What are you doing?',
        reply_markup=answer_questions_kb()
    )


@router.message(F.text.lower() == 'enter')
async def answer_enter(message):
    await message.answer(
        'You are invite',
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text.lower() == 'exit')
async def answer_exit(message):
    await message.answer(
        'You are dont invite',
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text)
async def hello_text(message):
    phrase = [
        'Hello',
        'Good luck',
        'Ha-Ha lol'
    ]
    if message.from_user.id in (1, 2):
        await message.answer(random.choice(phrase))
    else:
        await message.answer('Im sleep')


@router.message(F.text)
async def person_text(message):
    phrase = [
        'Hello {} name',
        'Good luck {name}',
        'Ha-Ha lol {name}'
    ]
    if message.from_user.id == 1:
        await message.answer(
            random.choice(phrase).format(name='Evgeniy')
        )
    elif message.from_user.id == 2:
        await message.answer(
            random.choice(phrase).format(name='Dmitriy')
        )
    else:
        await message.answer(
            'im sleep'
        )
