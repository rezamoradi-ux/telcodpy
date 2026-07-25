class EmojiManager:
    """مدیریت ایموجی‌های پریمیوم"""
    
    PREMIUM_EMOJIS = {
        "🔥": "🌟",  # پریمیوم جایگزین
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
        # ایموجی‌های جدید پریمیوم
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
        "🌜": "🌜"
    }
    
    def __init__(self):
        self.all_emojis = self.PREMIUM_EMOJIS
    
    def get_emoji(self, emoji_name: str) -> str:
        """دریافت ایموجی پریمیوم"""
        return self.all_emojis.get(emoji_name, emoji_name)
    
    def add_premium_emojis(self, text: str) -> str:
        """اضافه کردن ایموجی‌های پریمیوم به متن"""
        for normal, premium in self.all_emojis.items():
            if normal in text:
                text = text.replace(normal, premium)
        return text
    
    def is_premium_emoji(self, emoji: str) -> bool:
        """بررسی پریمیوم بودن ایموجی"""
        return emoji in self.all_emojis.values()