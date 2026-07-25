from enum import Enum
from typing import Dict, List

class PremiumEmoji:
    """
    کلاس مدیریت ایموجی‌های پریمیوم تلگرام
    """
    
    # تمام ایموجی‌های پریمیوم تلگرام
    PREMIUM_EMOJIS = {
        "🔥": "🌟",
        "❤️": "💖",
        "⭐": "🌟",
        "💎": "💎",
        "👑": "👑",
        "✨": "✨",
        "🌈": "🌈",
        "🎯": "🎯",
        "💫": "💫",
        "⚡": "⚡",
        "🔥": "🔥",
        "🎉": "🎉",
        "💝": "💝",
        "🎊": "🎊",
        "🏆": "🏆",
        "🦋": "🦋",
        "🌺": "🌺",
        "🌊": "🌊",
        "🌅": "🌅",
        "🌄": "🌄",
        "🌠": "🌠",
        "🌌": "🌌",
        "🌍": "🌍",
        "🌎": "🌎",
        "🌏": "🌏",
        "🌕": "🌕",
        "🌖": "🌖",
        "🌗": "🌗",
        "🌘": "🌘",
        "🌙": "🌙",
        "🌚": "🌚",
        "🌛": "🌛",
        "🌜": "🌜",
        "🌝": "🌝",
        "🌞": "🌞",
        "🌟": "🌟",
        "🌠": "🌠",
        "🌡": "🌡",
        "🌤": "🌤",
        "🌥": "🌥",
        "🌦": "🌦",
        "🌧": "🌧",
        "🌨": "🌨",
        "🌩": "🌩",
        "🌪": "🌪",
        "🌫": "🌫",
        "🌬": "🌬",
        "🌀": "🌀",
        "🌂": "🌂",
        "☂": "☂",
        "☔": "☔",
        "⛱": "⛱",
        "⚡": "⚡",
        "🔥": "🔥",
        "💧": "💧",
        "🌊": "🌊",
        "🎄": "🎄",
        "🎅": "🎅",
        "🎆": "🎆",
        "🎇": "🎇",
        "✨": "✨",
        "🎈": "🎈",
        "🎉": "🎉",
        "🎊": "🎊",
        "🎋": "🎋",
        "🎌": "🎌",
        "🎍": "🎍",
        "🎎": "🎎",
        "🎏": "🎏",
        "🎐": "🎐",
        "🎑": "🎑"
    }
    
    def __init__(self):
        self.emojis = self.PREMIUM_EMOJIS
    
    @classmethod
    def get_all(cls) -> Dict[str, str]:
        """دریافت تمام ایموجی‌های پریمیوم"""
        return cls.PREMIUM_EMOJIS
    
    @classmethod
    def get_random(cls) -> str:
        """دریافت یک ایموجی پریمیوم تصادفی"""
        import random
        return random.choice(list(cls.PREMIUM_EMOJIS.keys()))
    
    @classmethod
    def get_by_name(cls, name: str) -> str:
        """دریافت ایموجی پریمیوم با نام"""
        return cls.PREMIUM_EMOJIS.get(name, name)
    
    @classmethod
    def is_premium(cls, emoji: str) -> bool:
        """بررسی پریمیوم بودن ایموجی"""
        return emoji in cls.PREMIUM_EMOJIS.values()
    
    @classmethod
    def get_badge(cls) -> str:
        """دریافت نشان پریمیوم"""
        return "👑"
    
    @classmethod
    def get_star(cls) -> str:
        """دریافت ستاره پریمیوم"""
        return "⭐"
    
    @classmethod
    def get_diamond(cls) -> str:
        """دریافت الماس پریمیوم"""
        return "💎"

class PremiumStatus:
    """وضعیت پریمیوم کاربر"""
    def __init__(self, is_premium: bool = False, emojis: List[str] = None):
        self.is_premium = is_premium
        self.emojis = emojis or []
    
    def add_emoji(self, emoji: str):
        """اضافه کردن ایموجی پریمیوم"""
        if PremiumEmoji.is_premium(emoji):
            self.emojis.append(emoji)
    
    def remove_emoji(self, emoji: str):
        """حذف ایموجی پریمیوم"""
        if emoji in self.emojis:
            self.emojis.remove(emoji)
    
    def get_emojis(self) -> List[str]:
        """دریافت لیست ایموجی‌ها"""
        return self.emojis
    
    def has_emoji(self, emoji: str) -> bool:
        """بررسی وجود ایموجی"""
        return emoji in self.emojis