import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import API_TOKEN
from keyboards.default.def_buttons import welcome_buttons

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"""
Welcome {message.from_user.first_name}!🤠

🪪 In this bot you can get the id of any group, channel, user or bot

📤 To use the bot, click on the buttons below and share the chat whose ID you want to know. - In response, the bot will return the ID of the chat you shared

🇺🇸 To change the language send the /lang command

📝 You can get the ID in many other ways. Send the /help command

🤑 Want to donate to me? Send the /donate command

📢 For updates on the bot subscribe to @GetChatID_Updates
""", reply_markup=welcome_buttons)


@dp.message_handler(content_types=types.ContentType.USER_SHARED)
async def user_shared_func(message: types.Message):
    try:
        user_shared = message.user_shared
        if user_shared:
            await message.reply(f"The ID is: `{user_shared.user_id}`", parse_mode="Markdown")
    except:
        print("Error")




@dp.message_handler(content_types=types.ContentType.CHAT_SHARED)
async def chat_shared_func(message: types.Message):
    try:
        chat_shared = message.chat_shared
        chat_id = chat_shared._values.get("chat_id")
        if chat_id:
            await message.answer(f"The ID is: `{chat_id}`", parse_mode="Markdown")
        else:
            print("chat_id mavjud emas.")
    except:
        print("chat_id mavjud emas.")

@dp.message_handler(commands=['me'])
async def me_func(message: types.Message):
    me_id = message.from_user.id
    await message.reply(f"The ID is: `{me_id}`", parse_mode="Markdown")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)