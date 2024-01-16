from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def answer_questions_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text='Enter')
    kb.button(text='Exit')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
