import re
from os import environ
from Script import script

def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f'Error - {type} is invalid, exiting now')
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Bot information
API_ID = environ.get('API_ID', '16126827')
if len(API_ID) == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', 'd20e26deea812797eb00e731122a8372')
if len(API_HASH) == 0:
    print('Error - API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '5717884182:AAEfNaBiEYOS4o_U_XmqOP3WKVeWdx3_5OA')
if len(BOT_TOKEN) == 0:
    print('Error - BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '8080'))

# Bot pics
PICS = (environ.get('PICS', 'http://telegra.ph/file/2ab6ac6692cc50728ff30.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '661301615')
if len(ADMINS) == 0:
    print('Error - ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1001603505179 -1001810293410').split()]
if len(INDEX_CHANNELS) == 0:
    print('Info - INDEX_CHANNELS is empty')
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1002348851932')
if len(LOG_CHANNEL) == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)

# support group
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1001762991266')
if len(SUPPORT_GROUP) == 0:
    print('Error - SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://New:New@cluster0.29hkq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
if len(DATABASE_URL) == 0:
    print('Error - DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "Ajithkumar")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Ajithkumar_AK')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/kmsmovies1')
OWNER_USERNAME = environ.get("OWNER_USERNAME", "https://t.me/Team_Admins_2023")
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/kmsmovies1')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/kmsmovies1')
TUTORIAL = environ.get("TUTORIAL", "https://t.me/kmsmovies1")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/kmsmovies1")

# Bot settings
DELETE_TIME = int(environ.get('DELETE_TIME', 3600)) # Add time in seconds
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10))
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'hindi english telugu tamil kannada malayalam marathi punjabi bengali gujarati').split()]
QUALITY = [quality.lower() for quality in environ.get('QUALITY', 'Hdrip Web-Dl Bluray HDR FHD 240P 480P 540P 720P 1080P 1440P 2K 2160P 4K').split()]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "mdiskshortner.link")
SHORTLINK_API = environ.get("SHORTLINK_API", "1cf9ae3a85f3180eb45564a2a47e03f074b47a6a")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
PM_FILE_DELETE_TIME = int(environ.get('PM_FILE_DELETE_TIME', '180'))

# boolean settings
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
IS_VERIFY = is_enabled('IS_VERIFY', False)
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
WELCOME = is_enabled('WELCOME', True)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", False)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IMDB = is_enabled('IMDB', True)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled('SHORTLINK', False)

#premium info
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://mallucampaign.in/images/img_1722336532.jpg')
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'chandru.125@okhdfcbank')

# for stream
IS_STREAM = is_enabled('IS_STREAM', True)
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1002242824850")
if len(BIN_CHANNEL) == 0:
    print('Error - BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "https://nice-meris-mahaan.koyeb.app/")
if len(URL) == 0:
    print('Error - URL is missing, exiting now')
    exit()
else:
    if URL.startswith(('https://', 'http://')):
        if not URL.endswith("/"):
            URL += '/'
    elif is_valid_ip(URL):
        URL = f'http://{URL}/'
    else:
        print('Error - URL is not valid, exiting now')
        exit()

#start_command_reactions
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🆒", "👻"] #don't add any emoji because tg not support all emoji reactions
