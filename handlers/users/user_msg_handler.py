from aiogram import types
from loader import dp, bot
from keyboards.inline import main_menu
from utils import add_user_text
import os, sys


@dp.message_handler()
async def user_message(message: types.Message):
    # Get abs path
    if getattr(sys, 'frozen', False):
        path = os.path.dirname(sys.executable)
    elif __file__:
        path = os.path.dirname(__file__)
    path = "\\".join(path.split('\\')[:-2])

    #Set users text into txt-file
    try:
        last_text = open(f"{path}\\data\\img\\{message.from_user.id}\\last_text.txt", 'w+')
    except FileNotFoundError as e:
        os.mkdir(f"{path}\\data\\img\\{message.from_user.id}")
        last_text = open(f"{path}\\data\\img\\{message.from_user.id}\\last_text.txt", 'w+')
    finally:
        last_text.write(f"{message.text}\n")
        last_text.close()

    add_user_text(photo_name="doge.jpg",
                  user_text=message.text,
                  user_id=int(message.from_user.id),
                  user_name=message.from_user.username)
    img = open(f'{path}\\data\\img\\{message.from_user.id}\\doge_{message.text}.jpg', 'rb')

    await bot.send_photo(chat_id=message.from_user.id,
                         caption=message.text,
                         photo=img,
                         reply_markup=main_menu
                         )