"""
TelcodPy - کتابخانه پیشرفته برای ساخت ربات‌های تلگرام
ساخته شده توسط: RezaMoradi
تلگرام: @zcodPY
"""

from .client import TelcodClient
from .types import (
    Message, InlineKeyboard, ReplyKeyboard,
    KeyboardButton, InlineKeyboardButton,
    MiniApp, PremiumEmoji
)
from .handlers import MessageHandler, CallbackHandler
from .decorators import on_message, on_callback

__version__ = "1.0.0"
__author__ = "RezaMoradi"
__telegram__ = "@zcodPY"

__all__ = [
    'TelcodClient',
    'Message',
    'InlineKeyboard',
    'ReplyKeyboard',
    'KeyboardButton',
    'InlineKeyboardButton',
    'MiniApp',
    'PremiumEmoji',
    'MessageHandler',
    'CallbackHandler',
    'on_message',
    'on_callback'
]