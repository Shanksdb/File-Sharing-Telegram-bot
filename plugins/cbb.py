from pyrogram import Client 
from bot import Bot
from config import OWNER_ID, ABOUT_TXT, HELP_TXT, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                     InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')],
                [InlineKeyboardButton('ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ', url='https://t.me/Cultured_Madness'),
                 InlineKeyboardButton('ʜᴇɴᴛᴀɪ ᴄʜᴀɴɴᴇʟ', url='https://t.me/+0VRiOl0R0n02NzY1')],
                [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')]
            ])
        )
    elif data == "premium":
        await query.message.edit_text(
            text=f"<b>ᴘʀᴇᴍɪᴜᴍ ʙᴇɴᴇғɪᴛs & ᴘᴇʀᴋs\nᴅɪʀᴇᴄᴛ ᴄʜᴀɴɴᴇʟ ʟɪɴᴋs, ɴᴏ ᴀᴅ ʟɪɴᴋs\nsᴘᴇᴄɪᴀʟ ᴀᴄᴄᴇss ɪɴ ᴇᴠᴇɴᴛs\n\nᴘʀɪᴄɪɴɢ ʀᴀᴛᴇs\n𝟷 ᴍᴏɴᴛʜ - ɪɴʀ 𝟸𝟺𝟿/$7\n𝟹 ᴍᴏɴᴛʜs - ɪɴʀ 349/$15\n𝟼 ᴍᴏɴᴛʜs - ɪɴʀ 𝟻𝟿𝟿/$39\n𝟿 ᴍᴏɴᴛʜs - ɪɴʀ 749/$49\n𝟷𝟸 ᴍᴏɴᴛʜs - ɪɴʀ 999/$79\n\nᴡᴀɴᴛ ᴛᴏ ʙᴜʏ?\nᴅᴍ @LUFFY1JOYBOY\nsᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ to @arindam69x\n\nWe Have ʟɪᴍɪᴛᴇᴅ sᴇᴀᴛs ғᴏʀ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Owner", url="https://t.me/LUFFY1JOYBOY"),
                        InlineKeyboardButton("Main Channel", url="https://t.me/Cultured_Madness")
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
