import random

from pyrogram import filters
from pyrogram.types import Message

from config import LOGGER_ID as LOG_GROUP_ID
from ChampuXMusic import app
from ChampuXMusic.utils.database import delete_served_chat, get_assistant

photo = [
    "https://te.legra.ph/file/f6a2f71a516d8a5f88a29.jpg",
    "https://telegra.ph/file/4d303296e4fac9a40ea07.jpg",
    "https://telegra.ph/file/6f22d2d88f5b43ab9a805.jpg",
]


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    try:
        userbot = await get_assistant(message.chat.id)

        left_chat_member = message.left_chat_member
        if left_chat_member and left_chat_member.id == (await app.get_me()).id:
            remove_by = (
                message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
            )
            title = message.chat.title
            username = (
                f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
            )
            chat_id = message.chat.id
            left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
            await delete_served_chat(chat_id)
            await userbot.leave_chat(chat_id)
    except Exception as e:
        return
