from typing import List, Union, Optional, Any
from enum import Enum

class KeyboardButton:
    """دکمه کیبورد معمولی"""
    def __init__(self, text: str):
        self.text = text

class InlineKeyboardButton:
    """دکمه کیبورد اینلاین با رنگ‌های شیشه‌ای"""
    def __init__(
        self,
        text: str,
        callback_data: Optional[str] = None,
        url: Optional[str] = None,
        color: Optional[str] = None
    ):
        self.text = text
        self.callback_data = callback_data
        self.url = url
        self.color = color  # رنگ شیشه‌ای

class InlineKeyboard:
    """کیبورد اینلاین با دکمه‌های شیشه‌ای رنگی"""
    def __init__(
        self,
        buttons: List[List[InlineKeyboardButton]],
        row_width: int = 2
    ):
        self.buttons = [btn for row in buttons for btn in row]
        self.row_width = row_width

class ReplyKeyboard:
    """کیبورد معمولی"""
    def __init__(
        self,
        buttons: List[List[KeyboardButton]],
        row_width: int = 2,
        resize_keyboard: bool = True,
        one_time_keyboard: bool = False
    ):
        self.buttons = [btn for row in buttons for btn in row]
        self.row_width = row_width
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard