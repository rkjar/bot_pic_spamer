from aiogram import types
from keyboards.inline import main_menu
from loader import dp, bot
from utils import add_user_text
import os, sys


@dp.callback_query_handler(text_contains="btn")
async def randomizer(call: types.CallbackQuery):
    # first_image_call = call
    if getattr(sys, 'frozen', False):
        path = os.path.dirname(sys.executable)
    elif __file__:
        path = os.path.dirname(__file__)
    path = "\\".join(path.split('\\')[:-2])

    with open(f'{path}\\data\\img\\{call.message.chat.id}\\last_text.txt', "r") as last_text:
        all_message = last_text.readlines()
        last_msg = all_message[-1][:-1]

    add_user_text(photo_name=f"{call.data[4:]}.jpg",
                  user_text=last_msg,
                  user_id=int(call.message.chat.id),
                  user_name=call.from_user.username)

    img = open(f"{path}\\data\\img\\{call.message.chat.id}\\{call.data[4:]}_{last_msg}.jpg", "rb")

    await bot.edit_message_media(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 media=types.InputMediaPhoto(img)
                                 )

    await bot.edit_message_caption(chat_id=call.message.chat.id,
                                   message_id=call.message.message_id,
                                   caption=f"<b>{last_msg}</b> 🙃",
                                   reply_markup=main_menu
                                   )
