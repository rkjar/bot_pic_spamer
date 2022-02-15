from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline import main_menu
from loader import dp, bot


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    # img = open(f'./data/img/test.jpg', 'rb')
    # await bot.send_photo(chat_id=message.from_user.id,
    #                      photo=img,
    #                      reply_markup=main_menu
    #                      )
    await message.answer(f"Для создания <u>открытки</u> введите любой <u>текст</u>")