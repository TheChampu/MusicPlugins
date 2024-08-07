import aiohttp
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ChampuXMusic import app


@app.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git ChampuXD")
        return

    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/users/{username}"

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()

            try:
                url = result["html_url"]
                name = result["name"]
                company = result["company"]
                bio = result["bio"]
                created_at = result["created_at"]
                avatar_url = result["avatar_url"]
                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]

                caption = f"""ɢɪᴛʜᴜʙ ɪɴғᴏ ᴏғ {name}
                
ᴜsᴇʀɴᴀᴍᴇ: {username}
ʙɪᴏ: {bio}
ʟɪɴᴋ: [Here]({url})
ᴄᴏᴍᴩᴀɴʏ: {company}
ᴄʀᴇᴀᴛᴇᴅ ᴏɴ: {created_at}
ʀᴇᴩᴏsɪᴛᴏʀɪᴇs: {repositories}
ʙʟᴏɢ: {blog}
ʟᴏᴄᴀᴛɪᴏɴ: {location}
ғᴏʟʟᴏᴡᴇʀs: {followers}
ғᴏʟʟᴏᴡɪɴɢ: {following}"""

            except Exception as e:
                print(str(e))

    # Create an inline keyboard with a close button
    close_button = InlineKeyboardButton("Close", callback_data="close")
    inline_keyboard = InlineKeyboardMarkup([[close_button]])

    # Send the message with the inline keyboard
    await message.reply_photo(
        photo=avatar_url, caption=caption, reply_markup=inline_keyboard
    )


__MODULE__ = "Github"
__HELP__ = """
## GitHub Commands Help

### 1. /github or /git
**Description:**
Fetches GitHub user information.

**Usage:**
/github [username]

**Details:**
- Retrieves information about the specified GitHub user.
- Displays details such as username, bio, company, repositories, followers, and more.
- Provides a link to the user's GitHub profile.
- Accessible by providing a valid GitHub username after the command.

**Examples:**
- `/github ChampuXD`
"""
