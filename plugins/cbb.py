from pyrogram import version 
from bot import Bot 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
 
from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL 
 
@Bot.on_callback_query() 
async def cb_handler(client: Bot, query: CallbackQuery): 
    data = query.data 
    if data == "about": 
        await query.message.edit_text( 
            text = f"<b> ⟦⟧ Hi There Vro!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n◈ ᴄʀᴇᴀᴛᴏʀ: <a href=http://t.me/Ayanjdjdakaji>Ʉ₦₭Ø₩₦</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/hentaii_hindi_dub>ᴄᴜʟᴛᴜʀᴇᴅ</a>\n◈ ʜᴇɴᴛᴀɪ : <a href=https://t.me/+fdYEeYOudS8yMjY1n>ʜᴇɴᴛᴀɪ</a>\n◈ɪɴᴅɪᴀɴ ʟᴇᴀᴋs: <a href=https://t.me/+McYaSyY87qgyZDNl>ɪɴᴅɪᴀɴ ʟᴇᴀᴋs</a>\n◈  :\n┗━━━━━━━❪❂❫━━━━━━━━</b>", 
            disable_web_page_preview = True, 
            reply_markup = InlineKeyboardMarkup( 
                [ 
                    [ 
                        InlineKeyboardButton("🔒 Close", callback_data = "close") 
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
    elif data == "buy_prem": 
        await query.message.edit_text( 
            text=f"👋 ᴋᴏɴɪᴄʜɪᴡᴀ {query.from_user.username}\n blockquote><b>ᴘʀᴇᴍɪᴜᴍ ʙᴇɴɪғɪᴛs ᴀɴᴅ ᴘʀɪᴄᴇs /n• ᴅɪʀᴇᴄᴛ ᴄʜᴀɴɴᴇʟ ʟɪɴᴋs /n• ɴᴏ ᴀᴅ ʟɪɴᴋs /n • sᴘᴇᴄɪᴀʟ ᴀᴄᴄᴇss ɪɴ ᴇᴠᴇɴᴛs</blockquote> \n \n🎖️  blockquote><b>ᴘʀᴇᴍɪᴜᴍ ʙᴇɴɪғɪᴛs ᴀɴᴅ ᴘʀɪᴄᴇs</blockquote>ᴘʀɪᴄɪɴɢ ʀᴀᴛᴇs:\n\n● {PRICE1} rs ғᴏʀ 7 ᴅᴀʏs ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n● {PRICE2} rs ғᴏʀ 1 ᴍᴏɴᴛʜ ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n● {PRICE3} rs For 3 ᴍᴏɴᴛʜs ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n● {PRICE4} rs For 6 ᴍᴏɴᴛʜs ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n● {PRICE5} rs For 1 ʏᴇᴀʀ ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n blockquote><b>𝚅𝙸𝙿 / ʙᴇɴɪғɪᴛs 
ɴᴏ ʟɪɴᴋ ꜱʜᴏʀᴛᴇɴᴇʀ – ᴅɪʀᴇᴄᴛ ʟɪɴᴋꜱ, ɴᴏ ᴀᴅꜱ /n • ᴘʀᴇᴍɪᴜᴍ ʀᴇQᴜᴇꜱᴛꜱ – ʀᴇQᴜᴇꜱᴛ ᴄᴏɴᴛᴇɴᴛ ᴀɴʏᴛɪᴍᴇ /n • ᴏɴᴇ ᴍᴇᴍʙᴇʀꜱʜɪᴘ – ᴀᴄᴄᴇꜱꜱ ᴀʟʟ ᴄʜᴀɴɴᴇʟꜱ /n • Qᴜɪᴄᴋ ᴀᴄᴄᴇꜱꜱ – ɪɴꜱᴛᴀɴᴛ ᴄᴏɴᴛᴇɴᴛ ᴏɴ ᴄʟɪᴄᴋ /n • ꜰᴀꜱᴛᴇʀ ᴜᴘʟᴏᴀᴅꜱ – ᴘʀɪᴏʀɪᴛʏ ᴄᴏɴᴛᴇɴᴛ ᴅᴇʟɪᴠᴇʀʏ</blockquote>\n ᴏᴡɴᴇʀ ɪᴅ-  <code>{UPI_ID}</code>\n\n\n📸ғᴏʀ ʙᴜʏɪɴɢ ᴘʀᴇᴍɪᴜᴍ ᴅᴍ({UPI_IMAGE_URL}) /n ♻️ ᴡᴀɴᴛ ᴛᴏ ʙᴜʏ?  
ғᴏʀ ᴘᴀʏᴍᴇɴᴛ ᴅᴍ @Ayanakajiii /n blockquote><b>ᴡᴇ ʜᴀᴠᴇ ʟɪᴍɪᴛᴇᴅ sᴇᴀᴛs ғᴏʀ ᴘʀɪᴍᴇ ᴜsᴇʀs</blockquote>", 
            disable_web_page_preview=True, 
            reply_markup = InlineKeyboardMarkup( 
                [    
                    [ 
                        InlineKeyboardButton("sᴇɴᴅ ᴘᴀʏᴍᴇɴᴛ sᴄʀᴇᴇɴsʜᴏᴛ(ADMIN) 📸", url=(SCREENSHOT_URL)) 
                    ], 
                    [ 
                        InlineKeyboardButton("🔒 Close", callback_data = "close") 
                    ] 
                ] 
            ) 
                    )
