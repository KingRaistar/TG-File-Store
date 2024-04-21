import os

API_ID = int(os.environ.get("26958127", ))
API_HASH = os.environ.get("35854ae4e372945836b8bbd8c22c1c23", )
BOT_TOKEN = os.environ.get("6964402951:AAGavXvlbswiC1Kh9t3d7BJ85qrOU7YC_EI", )
DB_CHANNEL_ID = os.environ.get("-1002042880811")
IS_PRIVATE = os.environ.get("IS_PRIVATE",True) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("6972152979"))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("6972152979", "").split(" ")) if os.environ.get("6972152979") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(6972152979)
