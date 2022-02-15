from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=2)

btn_doge = InlineKeyboardButton(text="doge", callback_data="btn_doge")
btn_gosling = InlineKeyboardButton(text="gosling", callback_data="btn_gosling")
btn_kekw = InlineKeyboardButton(text="kekw", callback_data="btn_kekw")
btn_pepe = InlineKeyboardButton(text="pepe", callback_data="btn_pepe")

main_menu.add(btn_doge, btn_gosling, btn_kekw, btn_pepe)