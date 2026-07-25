from typing import Optional, Union, List, Dict, Any
from telethon.tl.types import Message as TelethonMessage
from datetime import datetime

class Message:
    """
    کلاس پیام برای مدیریت آسان پیام‌های تلگرام
    """
    
    def __init__(self, message: TelethonMessage):
        self._message = message
        self.id = message.id
        self.text = message.text or ""
        self.chat_id = message.chat_id if hasattr(message, 'chat_id') else None
        self.from_id = message.from_id.user_id if hasattr(message, 'from_id') and hasattr(message.from_id, 'user_id') else None
        self.date = message.date
        self.is_private = message.is_private if hasattr(message, 'is_private') else False
        self.is_group = message.is_group if hasattr(message, 'is_group') else False
        self.is_channel = message.is_channel if hasattr(message, 'is_channel') else False
        self.media = message.media if hasattr(message, 'media') else None
        self.reply_to = message.reply_to_msg_id if hasattr(message, 'reply_to_msg_id') else None
        self.entities = message.entities if hasattr(message, 'entities') else []
        
    async def reply(
        self,
        text: str,
        keyboard: Optional[Any] = None,
        parse_mode: str = "html",
        **kwargs
    ):
        """
        پاسخ به پیام
        
        Args:
            text: متن پاسخ
            keyboard: کیبورد (اختیاری)
            parse_mode: حالت پارس
        """
        from ..client import TelcodClient
        client = TelcodClient._current_instance
        
        if not client:
            raise RuntimeError("کلاینت راه‌اندازی نشده است")
        
        return await client.send_message(
            self.chat_id,
            text,
            keyboard=keyboard,
            parse_mode=parse_mode,
            reply_to=self.id,
            **kwargs
        )
    
    async def delete(self):
        """حذف پیام"""
        from ..client import TelcodClient
        client = TelcodClient._current_instance
        
        if not client:
            raise RuntimeError("کلاینت راه‌اندازی نشده است")
        
        await client.client.delete_messages(self.chat_id, [self.id])
    
    async def edit(
        self,
        text: str,
        keyboard: Optional[Any] = None,
        parse_mode: str = "html"
    ):
        """ویرایش پیام"""
        from ..client import TelcodClient
        client = TelcodClient._current_instance
        
        if not client:
            raise RuntimeError("کلاینت راه‌اندازی نشده است")
        
        # ساخت کیبورد
        reply_markup = None
        if keyboard:
            if hasattr(keyboard, 'buttons'):
                reply_markup = client._build_inline_keyboard(keyboard)
        
        await client.client.edit_message(
            self.chat_id,
            self.id,
            text,
            parse_mode=parse_mode,
            reply_markup=reply_markup
        )
    
    def get_mentions(self) -> List[str]:
        """دریافت لیست منشن‌های موجود در پیام"""
        mentions = []
        if self.entities:
            for entity in self.entities:
                if hasattr(entity, 'user_id'):
                    mentions.append(str(entity.user_id))
        return mentions
    
    def has_mention(self) -> bool:
        """بررسی وجود منشن در پیام"""
        return len(self.get_mentions()) > 0
    
    def get_commands(self) -> List[str]:
        """دریافت لیست کامندهای موجود در پیام"""
        commands = []
        if self.text and self.text.startswith('/'):
            parts = self.text.split()
            for part in parts:
                if part.startswith('/'):
                    commands.append(part)
        return commands
    
    def is_command(self, command: str) -> bool:
        """بررسی اینکه پیام یک کامند خاص است"""
        return command in self.get_commands()
    
    def get_args(self) -> List[str]:
        """دریافت آرگومان‌های کامند"""
        if self.text and self.text.startswith('/'):
            parts = self.text.split()
            if len(parts) > 1:
                return parts[1:]
        return []
    
    def to_dict(self) -> Dict[str, Any]:
        """تبدیل پیام به دیکشنری"""
        return {
            "id": self.id,
            "text": self.text,
            "chat_id": self.chat_id,
            "from_id": self.from_id,
            "date": self.date.isoformat() if self.date else None,
            "is_private": self.is_private,
            "is_group": self.is_group,
            "is_channel": self.is_channel,
            "has_media": bool(self.media),
            "reply_to": self.reply_to,
            "mentions": self.get_mentions(),
            "commands": self.get_commands()
        }

class MessageType:
    """انواع پیام‌ها"""
    TEXT = "text"
    PHOTO = "photo"
    VIDEO = "video"
    DOCUMENT = "document"
    AUDIO = "audio"
    VOICE = "voice"
    STICKER = "sticker"
    GIF = "gif"
    LOCATION = "location"
    CONTACT = "contact"
    POLL = "poll"
    GAME = "game"