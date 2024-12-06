from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonRequestUser,
    KeyboardButtonRequestChat,
    ChatAdministratorRights,
)

welcome_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="👤 User",
                request_user=KeyboardButtonRequestUser(
                    request_id=1,  # Unikal identifikator
                    user_is_bot=False,  # Faqat odamlar uchun
                    user_is_premium=None
                )
            ),
            KeyboardButton(
                text="🤖 Bot",
                request_user=KeyboardButtonRequestUser(
                    request_id=2,  # Unikal identifikator
                    user_is_bot=True,  # Faqat botlar uchun
                    user_is_premium=None
                )
            )
        ],
        [
            KeyboardButton(
                text="👥 Group",
                request_chat=KeyboardButtonRequestChat(
                    request_id=3,  # Unikal identifikator
                    chat_is_channel=False,  # Faqat guruhlar uchun
                    chat_is_forum=None,
                    chat_has_username=None,
                    user_administrator_rights=ChatAdministratorRights(
                        is_anonymous=False,
                        can_manage_chat=True
                    ),
                    bot_administrator_rights=None,
                    bot_is_member=True
                )
            ),
            KeyboardButton(
                text="📢 Channel",
                request_chat=KeyboardButtonRequestChat(
                    request_id=4,  # Unikal identifikator
                    chat_is_channel=True,  # Faqat kanallar uchun
                    chat_is_forum=None,
                    chat_has_username=None,
                    user_administrator_rights=None,
                    bot_administrator_rights=None,
                    bot_is_member=True
                )
            )
        ]
    ],
    resize_keyboard=True  # Tugmachalarni kichraytirish
)