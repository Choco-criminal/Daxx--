import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID" , "25475489"))
API_HASH = getenv("API_HASH" , "3fc2b371f4fbb0166758736414d8be92")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN" , "7617090520:AAH6OqlzkAGlJUhtd6O3yd9sRfDo6lxwn00")
#-------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","UnknownX_9_11")
#--------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Fubuki_xbot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "˹𝙁ᴜʙᴜᴋɪ ✘ 𝐌ᴜsɪᴄ˼🫧")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "Ur_Vortex")
# ---------------------------------------------------------
UPSTREAM_REPO = UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Choco-criminal/Soul",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", " 11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"
) 
# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))

#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI" , "mongodb+srv://Choco:Choco@cluster0.yddf3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID" , -1002122538649)) 
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID" , -1002122538649))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID" , 1266240012))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

#-----------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_bottt")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ANIME_CHAT_ANG")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "900"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 509))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION1", "BQGsE4IAQjJ_8wRNvR_IVIjoYxq9x8FQ6tC4acZQ0NX89CC3QXoaqsu-J54f_QPUbVtVOAsUhex84ZYsn2JnYYJ1LZSK_JQ1MZSlt91H3GAkUCb_W1KPnV12mV6Vdik2ODFVfXyMMBSn8zkxBlUzaVE3GLbejDcjub0F2UZBU7xUHPSx9td3q5WtUu_m5Rsr07MYy17RoDaEiiJVS3JrjToehIq7gO1w776K6DaOcT3lyh1ikeK7cPRPZioEl2AFrG9TBGHxLnLLnkjQ8FtVtcSicUrx7lthZD86bdlCvVqnVVcfi2u078L0iiLLBEGqqWqE0MQHXy19nakYhnm-Fqzi4khCGQAAAAFv0KDhAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
TEMP_DB_FOLDER = "tempdb"
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/pC0.mp4"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/AAt.mp4"
)
PLAYLIST_IMG_URL = "https://envs.sh/p4F.jpg"
STATS_IMG_URL = "https://envs.sh/pYG.mp4"
COUPLE_IMG_URL = "https://envs.sh/Abq.mp4"
TELEGRAM_AUDIO_URL = "https://envs.sh/pC3.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/pC3.jpg"
STREAM_IMG_URL = "https://envs.sh/p4e.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/p4w.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/4e4c15823f0056c0756c8-1230cfcb94e69c070c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/vTelegraphBot-10-21-13https://graph.org/vTelegraphBot-10-21-13"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/vTelegraphBot-10-21-13https://graph.org/vTelegraphBot-10-21-13"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/c7ea15528fc9816e05141-0a5598ac2585dae36f.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
