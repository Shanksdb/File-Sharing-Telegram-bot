from operator import add
import os
import logging


# import dotenv
# dotenv.load_dotenv()


from logging.handlers import RotatingFileHandler

#force user to join your backup channel leave 0 if you don't need.
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))

if FORCE_SUB_CHANNEL > FORCE_SUB_CHANNEL2:
    temp = FORCE_SUB_CHANNEL2 
    FORCE_SUB_CHANNEL2 = FORCE_SUB_CHANNEL
    FORCE_SUB_CHANNEL = temp

#bot stats
BOT_STATS_TEXT = os.environ.get("BOTS_STATS_TEXT","<b>BOT UPTIME 🌺</b>\n{uptime}")
#send custom message when user interact with bot
USER_REPLY_TEXT = os.environ.get("USER_REPLY_TEXT", "Don't send me messages directly I'm only File Share bot! 📌")

#your bot token here from https://telegram.me/BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7787292643:AAEkY1HYMwpM56BsKglXCedAYDvZC-I1Wc0") 
#your api id from https://my.telegram.org/apps
APP_ID = int(os.environ.get("APP_ID", "28713982"))
#your api hash from https://my.telegram.org/apps
API_HASH = os.environ.get("API_HASH", "237e15f7c006b10b4fa7c46fee7a5377")
#your channel_id from https://t.me/MissRose_bot by forwarding dummy message to rose and applying command `/id` in reply to that message
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002436812797"))
#your id of telegram can be found by https://t.me/MissRose_bot with '/id' command
OWNER_ID = int(os.environ.get("OWNER_ID", "5792873052"))
#port set to default 8080
PORT = os.environ.get("PORT", "8080")
#your database url mongodb only You can use mongo atlas free cloud database
DB_URL = os.environ.get("DB_URL", "mongodb+srv://drapixstore:Y7DJWJCCpBQClI5o@cluster0.fq7ee6x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#your database name
DB_NAME = os.environ.get("DB_NAME", "ayanakajidb")

#for creating telegram thread for bot to improve performance of the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "60"))
#your start default command message.
START_MSG = os.environ.get("START_MESSAGE", "<blockquote><b>ʟᴏᴠᴇ ᴀɴɪᴍᴇ? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴡᴀᴛᴄʜ ᴡʜᴀᴛ ʏᴏᴜ'ʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.</blockquote>\n\nᴄʜᴇᴄᴋ ᴏᴜᴛ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ꜰᴏʀ ᴍᴏʀᴇ!👇</b>")
#your telegram tag without @
OWNER_TAG = os.environ.get("OWNER_TAG", "Ayanakaji")
#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "0"))


#Shortner (token system) 
"""
some token verification sites
https://dashboard.shareus.io/
"""

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
USE_SHORTLINK = True if os.environ.get('USE_SHORTLINK', "TRUE") == "TRUE" else False 
# only shareus service known rightnow rest you can test on your own
SHORTLINK_API_URL = os.environ.get("SHORTLINK_API_URL", "modijiurl.com")
# SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "")
#use this key if not working ☠️ (jokin!!)
SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "822b16f3a80cec0d4138a4f083ff472f8d5a5d52")
#add your custom time in secs for shortlink expiration.
# 24hr = 86400
# 12hr = 43200
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "120")) # Add time in seconds
#put TRUE if you want shortner in every link generated by the bot.
U_S_E_P = True if (True if os.environ.get('U_S_E_P', "TRUE") == "TRUE" else False) and (USE_SHORTLINK) else False
#Tutorial video for the user of your shortner on how to download.
TUT_VID = os.environ.get("TUT_VID","https://t.me/hentai_hindi_dubbed/72")





#Payment to remove the token system
#put TRUE if you want this feature
USE_PAYMENT = True if (True if os.environ.get("USE_PAYMENT","TRUE") == "TRUE" else False) and (USE_SHORTLINK) else False
#UPI ID
UPI_ID = os.environ.get("UPI_ID", "𝗗𝗺 - @Ayanakaji")
#UPI QR CODE IMAGE
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "https://t.me//Ayanakaji")
#SCREENSHOT URL of ADMIN for verification of payments
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/{OWNER_TAG}")
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "49 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "199 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "299 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "599rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "999 rs")



#force message for joining the channel
FORCE_MSG = os.environ.get("FORCE_MSG", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b> 🥺")
#custom caption 
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
#protected content so that no files can be sent from the bot to anyone. recommended False
# TRUE for yes FALSE if no
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "FALSE") == "TRUE" else False
#used if you dont need buttons on database channel.
# True for yes False if no
DISABLE_CHANNEL_BUTTON = True if os.environ.get("DISABLE_CHANNEL_BUTTON", "TRUE") == "TRUE" else False
#you can add admin inside the bot(bug right now will fix later)

#add admins with space seperated
# 7195990000 289371935 248979023
ADMIN_LIST = os.environ.get("ADMINS", "5792873052 7195990500").split()




#no need to add anything from now on
ADMINS = [int(admin) for admin in ADMIN_LIST if admin.isdigit()]
ADMINS.append(OWNER_ID)


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
