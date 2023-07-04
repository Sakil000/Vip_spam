## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQBMcWgv7bA18_d-QT0v67paNDqyvFn3ci3s4txjkWcW7Jq518zRQ6s00YkEBUZP3dynGcLbvbVRNaPf1hbZ-rWPV26hdNlBqtdDQHqUhg2O_9ub76stOAhMNdLpjjs_RQUF3KE6dpdfIgdnwF7TMEo_jkIdNXNwqUvcfd4zLcoGjJtO67v1ZveVhGKZI7kb36r_MRlLexqe0zK-cM_s4RyzS75idDDQBB6qgqr089U-zPR7p-5CzJasKpeta5pzyG1TOSEW0oXzRBjdZd0XGQViL_n0vhOVkBDbFm_psAszEQvj2fQbCnFUGhvpfAX9cMqep6rBCuSk-XnRQWZJu4mwAAAAAVtc-zoA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "6325577627:AAEX9rcDUArFBPn8f1tf3-dymaohWEgdghI")
BOT_NAME = getenv("BOT_NAME", "InayaMusic")

API_ID = int(getenv("API_ID", "26792767"))
API_HASH = getenv("API_HASH", "d5892fe7d458bff884fde1f1efbaadf3")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Inaya:Inaya@inaya.wbxxiws.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "𝄟┼𝆺𝅥⃝ᶦϻ‌ ᵛ‌ᵎᵖ ≛⃝⍣⃟ _𝗦𝗔𝗞𝗜𝗟𝄟≛⃝❥︎︎≛⃝⍣⃟* ⁪")
OWNER_USERNAME = getenv("OWNER_USERNAME", "YO_UR_OFFICIAL_CRUSH")
ALIVE_NAME = getenv("ALIVE_NAME", "InayaXMusic")
BOT_USERNAME = getenv("BOT_USERNAME", "InayaXrobot")
OWNER_ID = getenv("OWNER_ID", "6024212623")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "➻ ˹𝑰ɳαყα᭄ ✘ 𝑴µรเc˼")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Vip_Sakil_Bio")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Vip_Sakil_Bio")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5941400521").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/a84cf350aeb2800b94708.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/bce7fb03ce073b0e70bc2.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1200"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/VIP-SAKIL/Inayaspam")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/cafa810a301ef87acf875.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/97c666440d9b3d70dfe1c.jpg")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/e3063dd280b3598d04511.jpg")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/97c666440d9b3d70dfe1c.jpg")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/cafa810a301ef87acf875.jpg")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/97c666440d9b3d70dfe1c.jpg")
HEROKU_MODE = getenv("HEROKU_MODE", None)
