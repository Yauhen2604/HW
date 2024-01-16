from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text)
async def answer_text(message):
    await message.answer(
        'This is text type'
    )


@router.message(F.sticker)
async def answer_stickers(message):
    await message.answer(
        'This is sticker type'
    )


@router.message(F.animation)
async def answer_animation(message):
    await message.answer(
        'This is animation type'
    )


