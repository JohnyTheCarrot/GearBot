from discord import utils

from Util import Configuration

emojis = dict()

BACKUPS = {
    "1": "1⃣",
    "2": "2⃣",
    "3": "3⃣",
    "4": "4⃣",
    "5": "5⃣",
    "6": "6⃣",
    "7": "7⃣",
    "8": "8⃣",
    "9": "9⃣",
    "10": "🔟",
    "ALTER": "🛠",
    "BAN": "🚪",
    "BEAN": "🌱",
    "BOOT": "👢",
    "BUG": "🐛",
    "CLOCK": "⏰",
    "CREATE": "🔨",
    "DELETE": "⛏",
    "DIAMOND": "⚙",
    "DND": "❤",
    "EDIT": "📝",
    "EYES": "👀",
    "GOLD": "⚙",
    "IDLE": "💛",
    "INNOCENT": "😇",
    "IRON": "⚙",
    "JOIN": "📥",
    "LEAVE": "📤",
    "LEFT": "◀",
    "LOADING": "⏳",
    "MUTE": "😶",
    "NAMETAG": "📛",
    "NICKTAG": "📛",
    "NO": "🚫",
    "OFFLINE": "💙",
    "ONLINE": "💚",
    "QUESTION": "❓",
    "REFRESH": "🔁",
    "RIGHT": "▶",
    "ROLE_ADD": "🛫",
    "ROLE_REMOVE": "🛬",
    "SEARCH": "🔎",
    "SINISTER": "😈",
    "SPY": "🕵",
    "STONE": "⚙",
    "STREAMING": "💜",
    "TACO": "🌮",
    "THINK": "🤔",
    "TODO": "📋",
    "TRASH": "🗑",
    "VOICE": "🔊",
    "WARNING": "⚠",
    "WHAT": "☹",
    "WINK": "😉",
    "WOOD": "⚙",
    "WRENCH": "🔧",
    "YES": "✅",
}


def initialize(bot):
    for name, eid in Configuration.get_master_var("EMOJI", {}).items():
        emojis[name] = utils.get(bot.emojis, id=eid)


def get_chat_emoji(name):
    return str(get_emoji(name))


def get_emoji(name):
    if name in emojis:
        return emojis[name]
    else:
        return BACKUPS[name]
