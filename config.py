from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "34446649"))
API_HASH = getenv("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
UPDATES_CHANNEL = str(os.environ.get('UPDATES_CHANNEL', Matching_pfp_Gallery))
BOT_TOKEN = getenv("BOT_TOKEN", "8772312754:AAEken-freWxFhAHuVZ8iRsUT_oerjz3fT8")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", 7892805795)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/log_channel_a")
