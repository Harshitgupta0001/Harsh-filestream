from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID", "21551881"))
    API_HASH = str(env.get("API_HASH", "6e83e9e1aee5accd4868dc29aa59ebaa"))
    BOT_TOKEN = str(env.get("BOT_TOKEN"))
    OWNER_ID = int(env.get('OWNER_ID', '6359874284'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL', 'mongodb+srv://david:surya@cluster12.f7tpy44.mongodb.net/'))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "moviesworldupdates"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', '')
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/2091c2bd9ff52423d4fb1.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/0f4314c9f903a3c996ca9.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/87135b99d32804ad0d6a1.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get('FLOG_CHANNEL', '-1002166379672'))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get('ULOG_CHANNEL', '-1002166379672'))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "6359874284")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )



