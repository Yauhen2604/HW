import asyncio
import logging
from datetime import datetime
from random import randint

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

# vkl logi dlya otslegh, chtoby ne propystit vaznoe soobshenie
logging.basicConfig(level=logging.INFO)

# create object bota
bot = Bot(token=my_token)

# create object dispecther
dp = Dispatcher()

dp['started_at'] = datetime.now().strftime("%Y-%m-%d %H:%m")


# @dp.message(F.text)
# async def func():
#     pass


@dp.message(F.text, Command('text'))
async def text(message):
    await message.answer('Hello, <i>world</i>!', parse_mode=ParseMode.HTML)
    await message.answer('Hello, *world*!', parse_mode=ParseMode.MARKDOWN_V2)
    await message.answer('Hello, <i>world</i>!', parse_mode=ParseMode.MARKDOWN)


@dp.message(Command('marker', prefix='!'))
async def marker(message):
    content = as_list(as_marked_section(
        Bold('True:'),
        'Test1', 'Test2',
        marker='✅'
    ),
        as_marked_section(
            Bold('False:'),
            'Test3', 'Test4',
            marker='❌'
        ),
        as_marked_section(
            Bold('Total:'),
            as_key_value('ok', 1),
            as_key_value('true', 2),
            as_key_value('false', 3),
            marker='-'
        ),
        HashTag('#poll'))
    await message.answer(**content.as_kwargs())


@dp.message(F.animation)
async def some_gif(message):
    await message.reply_animation(message.animation.file_id)


@dp.message(Command('img'))
async def upl_img(message):
    file_ids = []
    with open('bernard-hermant-nD9yL9ukVlk-unsplash.jpg', 'rb') as img_from_buffer:
        result = await message.answer_photo(
            BufferedInputFile(
                img_from_buffer.read(),
                filename='img from buf.jpg'
            ),
            caption='izobr iz bufera'
        )
        file_ids.append(result.photo[-1].file_id)

        img_from_pc = FSInputFile('img_from_pc.jpg')
        result = await message.answer_photo(
            img_from_pc,
            caption='izobr iz pc')
        file_ids.append(result.photo[-1].file_id)

        img_from_url = URLInputFile('https://picsum.photos/seed/groosha/400/300')
        result = await message.answer_photo(
            img_from_url,
            caption='izobr po url')
        file_ids.append(result.photo[-1].file_id)
        await message.answer('send file')


@dp.message(Command('add_to_list'))
async def add_to_list(message, my_list):
    my_list.append(4)
    await message.answer('Append num 4')


dp.message(Command('img'))


@dp.message(Command('show_list'))
async def show_list(message, my_list):
    await message.answer(f'Your list: {my_list}')


@dp.message(Command('info'))
async def info(message, started_at):
    await message.answer(f'bot started: {started_at}')


# handler /start
@dp.message(Command('start'))
async def cmnd_start(message):
    key_buttom = [[types.KeyboardButton(text="privet nastya")],
                  [types.KeyboardButton(text="gotov' uzhin")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=key_buttom, resize_keyboard=True,
                                         input_field_placeholder='Enter property')
    await message.answer('Kogda kushat?', reply_markup=keyboard)


@dp.message(F.text.lower() == 'privet nastya')
async def func_openfrigle(message):
    await message.reply('Gotov bedra Nastya!!!')


@dp.message(F.text.lower() == "gotov' uzhin")
async def func_kushat(message):
    await message.reply('Vkusno', reply_markup=types.ReplyKeyboardRemove())


@dp.message(Command('rkb'))
async def rkb(message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 17):
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(4)
    await message.answer('Choise number:',
                         reply_markup=builder.as_markup(resize_keyboard=True))


@dp.message(Command('custom_kb'))
async def custom_kb(message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text='Get geolocation', request_location=True),
        types.KeyboardButton(text='Get contact', request_contact=True),
    )
    builder.row(
        types.KeyboardButton(text='Create quiz', request_poll=types.KeyboardButtonPollType(type='quiz'))
    )
    builder.row(
        types.KeyboardButton(text='Get VIP user',
                             request_user=types.KeyboardButtonRequestUser(request_id=1, user_is_premium=True)))
    builder.row(
        types.KeyboardButton(text='Get VIP chat',
                             request_user=types.KeyboardButtonRequestUser(request_id=2, chat_is_chanenel=True)))
    await message.answer('Choise some', reply_markup=builder.as_markup(resize_keyboard=True))


@dp.message(F.user_shared)
async def on_shared_user(message):
    print(f'request {message.user_shared.request_id}, '
          f'{message.user_shared.chat_id}, ')


@dp.message(Command('inline_url'))
async def inline_url(message, bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text='Onliner', url='https://onliner.by')
    )
    builder.row(types.InlineKeyboardButton(
        text='21vek', url='21vek.by')
    )

    user_id = 763915458
    chat_info = await bot.get_chat(user_id)
    if not chat_info.has_private_forwards:
        builder.row(types.InlineKeyboardButton(
            text='Some user',
            url=f'tg://user?id={user_id}'
        ))
    await message.answer('Choose', reply_markup=builder.as_markup())


@dp.message(Command('inline_callback_1'))
async def inline_callback_1(message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='Tap me',
        callback_data='random_value'
    ))
    await message.answer('Tap button, send number',
                         reply_markup=builder.as_markup())


@dp.callback_query(F.data == 'random_value')
async def send_random_value(callback):
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer(
        text='IDI DOMOY!!!',
        show_alert=True
    )


user_data = {}


def get_kb():
    buttons = [
        [
            types.InlineKeyboardButton(text='-1', callback_data='num_1'),
            types.InlineKeyboardButton(text='+1', callback_data='num_2'),
        ],
        [types.InlineKeyboardButton(text='confirm', callback_data='num_stop')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def update(message, new_val):
    await message.edit_text(
        f'say num {new_val}',
        reply_markup=get_kb()
    )


@dp.message(Command('num'))
async def num(message):
    user_data[message.from_user.id] = 0
    await message.answer('Set num 0', reply_markup=get_kb())


@dp.callback_query(F.data.startswith("num"))
async def call_num(callback):
    user_val = user_data.get(callback.from_user.id, 0)
    action = callback.data.split('_')[1]
    if action == '1':
        user_data[callback.from_user.id] = user_val - 1
        await update(callback.message, user_val - 1)
    elif action == '2':
        user_data[callback.from_user.id] = user_val + 1
        await update(callback.message, user_val + 1)
    if action == 'stop':
        await callback.message.edit_text('finish: ' + str(user_val))
    await callback.answer


@dp.message(Command('Test'))
async def cmnd_test(message):
    await message.answer('test')


@dp.message(Command('answer'))
async def cmnd_answer(message):
    await message.answer('simple answer')


@dp.message(Command('reply'))
async def cmnd_reply(message):
    await message.reply('answer with reply')


@dp.message(Command('dice'))
async def dice(message):
    await message.answer_dice(emoji=DiceEmoji.DICE)



# create polling for new update
async def main():
    await dp.start_polling(bot, my_list=[1, 2, 3])


if __name__ == '__main__':
    asyncio.run(main())


