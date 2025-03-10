from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=(
                "<b> ⟦⟧ Hi There Vro!💫\n"
                "┏━━━━━━━❪❂❫━━━━━━━━\n"
                "◈ ᴄʀᴇᴀᴛᴏʀ: <a href='http://t.me/Ayanakaji'>Ʉ₦₭Ø₩₦</a>\n"
                "◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href='https://t.me/hentai_hindi_dub'>ᴄᴜʟᴛᴜʀᴇᴅ</a>\n"
                "◈ ʜᴇɴᴛᴀɪ : <a href='https://t.me/+fdYEeYOudS8yMjY1n'>ʜᴇɴᴛᴀɪ</a>\n"
                "◈ɪɴᴅɪᴀɴ ʟᴇᴀᴋs: <a href='https://t.me/+McYaSyY87qgyZDNl'>ɪɴᴅɪᴀɴ ʟᴇᴀᴋs</a>\n"
                "┗━━━━━━━❪❂❫━━━━━━━━</b>"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔒 Close", callback_data="close")]
            ])
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "buy_prem":
        await query.message.edit_text(
            text=(
                f"👋 ᴋᴏɴɪᴄʜɪᴡᴀ {query.from_user.username}\n\n"
                "<b>ᴘʀᴇᴍɪᴜᴍ ʙᴇɴɪғɪᴛs ᴀɴᴅ ᴘʀɪᴄᴇs</b>\n"
                "• ᴅɪʀᴇᴄᴛ ᴄʜᴀɴɴᴇʟ ʟɪɴᴋs\n"
                "• ɴᴏ ᴀᴅ ʟɪɴᴋs\n"
                "• sᴘᴇᴄɪᴀʟ ᴀᴄᴄᴇss ɪɴ ᴇᴠᴇɴᴛs\n\n"
                "<b>ᴘʀɪᴄɪɴɢ ʀᴀᴛᴇs:</b>\n"
                f"● {PRICE1} rs ғᴏʀ 7 ᴅᴀʏs ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n"
                f"● {PRICE2} rs ғᴏʀ 1 ᴍᴏɴᴛʜ ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n"
                f"● {PRICE3} rs ғᴏʀ 3 ᴍᴏɴᴛʜs ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n"
                f"● {PRICE4} rs ғᴏʀ 6 ᴍᴏɴᴛʜs ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n"
                f"● {PRICE5} rs ғᴏʀ 1 ʏᴇᴀʀ ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n"
                "<b>𝚅𝙸𝙿 / ʙᴇɴɪғɪᴛs</b>\n"
                "• ɴᴏ ʟɪɴᴋ ꜱʜᴏʀᴛᴇɴᴇʀ – ᴅɪʀᴇᴄᴛ ʟɪɴᴋꜱ, ɴᴏ ᴀᴅꜱ\n"
                "• ᴘʀᴇᴍɪᴜᴍ ʀᴇQᴜᴇꜱᴛꜱ – ʀᴇQᴜᴇꜱᴛ ᴄᴏɴᴛᴇɴᴛ ᴀɴʏᴛɪᴍᴇ\n"
                "• ᴏɴᴇ ᴍᴇᴍʙᴇʀꜱʜɪᴘ – ᴀᴄᴄᴇꜱꜱ ᴀʟʟ ᴄʜᴀɴɴᴇʟꜱ\n"
                "• Qᴜɪᴄᴋ ᴀᴄᴄᴇꜱꜱ – ɪɴꜱᴛᴀɴᴛ ᴄᴏɴᴛᴇɴᴛ ᴏɴ ᴄʟɪᴄᴋ\n"
                "• ꜰᴀꜱᴛᴇʀ ᴜᴘʟᴏᴀᴅꜱ – ᴘʀɪᴏʀɪᴛʏ ᴄᴏɴᴛᴇɴᴛ ᴅᴇʟɪᴠᴇʀʏ\n\n"
                f"ᴏᴡɴᴇʀ ɪᴅ: <code>{UPI_ID}</code>\n\n"
                f"📸ғᴏʀ ʙᴜʏɪɴɢ ᴘʀᴇᴍɪᴜᴍ ᴅᴍ (<a href='{UPI_IMAGE_URL}'>ᴘᴀʏᴍᴇɴᴛ ʟɪɴᴋ</a>)\n"
                "♻️ ᴡᴀɴᴛ ᴛᴏ ʙᴜʏ?\n"
                "ғᴏʀ ᴘᴀʏᴍᴇɴᴛ ᴅᴍ @Ayanakaji\n"
                "<b>ᴡᴇ ʜᴀᴠᴇ ʟɪᴍɪᴛᴇᴅ sᴇᴀᴛs ғᴏʀ ᴘʀɪᴍᴇ ᴜsᴇʀs</b>"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("sᴇɴᴅ ᴘᴀʏᴍᴇɴᴛ sᴄʀᴇᴇɴsʜᴏᴛ (ADMIN) 📸", url=SCREENSHOT_URL)],
                [InlineKeyboardButton("🔒 Close", callback_data="close")]
            ])
        )
