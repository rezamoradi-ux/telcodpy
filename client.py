import asyncio
from telethon import TelegramClient, events
from telethon.tl.types import (
    Message, KeyboardButton, KeyboardButtonRow,
    ReplyInlineMarkup, ReplyKeyboardMarkup,
    InlineKeyboardButton as TelethonInlineButton
)
from typing import Union, List, Dict, Any, Callable, Optional
import logging
from .types import (
    InlineKeyboard, ReplyKeyboard,
    InlineKeyboardButton, KeyboardButton,
    Message as TelcodMessage,
    MiniApp, PremiumEmoji
)
from .handlers import MessageHandler, CallbackHandler
from .utils.emoji_manager import EmojiManager
from .utils.color_manager import ColorManager

class TelcodClient:
    """
    کلاینت اصلی کتابخانه TelcodPy
    """
    
    def __init__(
        self,
        api_id: Optional[int] = None,
        api_hash: Optional[str] = None,
        bot_token: Optional[str] = None,
        session_name: str = "telcod_session"
    ):
        """
        راه‌اندازی کلاینت
        
        Args:
            api_id: شناسه API (برای حالت کاربری)
            api_hash: هش API (برای حالت کاربری)
            bot_token: توکن ربات (برای حالت ربات)
            session_name: نام جلسه
        """
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_token = bot_token
        self.session_name = session_name
        self.client = None
        self.is_bot = bool(bot_token)
        self.handlers = []
        self.emoji_manager = EmojiManager()
        self.color_manager = ColorManager()
        
        # تنظیم لاگر
        logging.basicConfig(
            format='[%(levelname)s] %(asctime)s - %(message)s',
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)
    
    async def start(self):
        """شروع کلاینت"""
        if self.is_bot:
            self.client = TelegramClient(
                self.session_name,
                api_id=self.api_id or 0,
                api_hash=self.api_hash or "",
                connection_retries=5
            )
            await self.client.start(bot_token=self.bot_token)
        else:
            if not self.api_id or not self.api_hash:
                raise ValueError("برای حالت کاربری، api_id و api_hash الزامی است")
            self.client = TelegramClient(
                self.session_name,
                self.api_id,
                self.api_hash
            )
            await self.client.start()
        
        self.logger.info("✅ کلاینت با موفقیت راه‌اندازی شد")
        return self
    
    async def stop(self):
        """متوقف کردن کلاینت"""
        if self.client:
            await self.client.disconnect()
            self.logger.info("⏹️ کلاینت متوقف شد")
    
    def on_message(self, pattern: str = None):
        """
        دکوراتور برای مدیریت پیام‌ها
        
        Args:
            pattern: الگوی پیام (اختیاری)
        """
        def decorator(func: Callable):
            handler = MessageHandler(func, pattern)
            self.handlers.append(handler)
            
            @self.client.on(events.NewMessage(pattern=pattern))
            async def wrapper(event):
                try:
                    message = TelcodMessage(event.message)
                    await func(message)
                except Exception as e:
                    self.logger.error(f"خطا در پردازش پیام: {e}")
            
            return func
        return decorator
    
    def on_callback(self, pattern: str = None):
        """
        دکوراتور برای مدیریت کالبک‌ها
        
        Args:
            pattern: الگوی کالبک (اختیاری)
        """
        def decorator(func: Callable):
            handler = CallbackHandler(func, pattern)
            self.handlers.append(handler)
            
            @self.client.on(events.CallbackQuery(pattern=pattern))
            async def wrapper(event):
                try:
                    await func(event)
                except Exception as e:
                    self.logger.error(f"خطا در پردازش کالبک: {e}")
            
            return func
        return decorator
    
    async def send_message(
        self,
        chat_id: Union[int, str],
        text: str,
        keyboard: Union[InlineKeyboard, ReplyKeyboard] = None,
        parse_mode: str = "html",
        disable_web_page_preview: bool = False,
        **kwargs
    ) -> TelcodMessage:
        """
        ارسال پیام
        
        Args:
            chat_id: شناسه چت
            text: متن پیام
            keyboard: کیبورد (اختیاری)
            parse_mode: حالت پارس (html/markdown)
            disable_web_page_preview: غیرفعال کردن پیش‌نمایش وب
        """
        if not self.client:
            raise RuntimeError("کلاینت راه‌اندازی نشده است. ابتدا start() را فراخوانی کنید.")
        
        # بررسی پریمیوم ایموجی
        if "premium" in text.lower() and hasattr(self, 'premium_check'):
            if await self._check_premium(chat_id):
                text = self.emoji_manager.add_premium_emojis(text)
        
        # ساخت کیبورد
        reply_markup = None
        if keyboard:
            if isinstance(keyboard, InlineKeyboard):
                reply_markup = self._build_inline_keyboard(keyboard)
            elif isinstance(keyboard, ReplyKeyboard):
                reply_markup = self._build_reply_keyboard(keyboard)
        
        # ارسال پیام
        try:
            result = await self.client.send_message(
                chat_id,
                text,
                parse_mode=parse_mode,
                reply_markup=reply_markup,
                disable_web_page_preview=disable_web_page_preview,
                **kwargs
            )
            return TelcodMessage(result)
        except Exception as e:
            self.logger.error(f"خطا در ارسال پیام: {e}")
            raise
    
    def _build_inline_keyboard(self, keyboard: InlineKeyboard):
        """ساخت کیبورد اینلاین"""
        rows = []
        current_row = []
        
        for button in keyboard.buttons:
            if isinstance(button, InlineKeyboardButton):
                # ساخت دکمه با رنگ‌های شیشه‌ای
                if button.color:
                    button_data = self.color_manager.apply_glass_effect(
                        button.text,
                        button.color
                    )
                else:
                    button_data = button.text
                
                current_row.append(
                    TelethonInlineButton(
                        text=button_data,
                        callback_data=button.callback_data,
                        url=button.url
                    )
                )
                
                if len(current_row) == keyboard.row_width:
                    rows.append(KeyboardButtonRow(buttons=current_row))
                    current_row = []
        
        if current_row:
            rows.append(KeyboardButtonRow(buttons=current_row))
        
        return ReplyInlineMarkup(rows=rows)
    
    def _build_reply_keyboard(self, keyboard: ReplyKeyboard):
        """ساخت کیبورد معمولی"""
        rows = []
        current_row = []
        
        for button in keyboard.buttons:
            if isinstance(button, KeyboardButton):
                current_row.append(
                    KeyboardButton(text=button.text)
                )
                
                if len(current_row) == keyboard.row_width:
                    rows.append(KeyboardButtonRow(buttons=current_row))
                    current_row = []
        
        if current_row:
            rows.append(KeyboardButtonRow(buttons=current_row))
        
        return ReplyKeyboardMarkup(
            rows=rows,
            resize=keyboard.resize_keyboard,
            one_time=keyboard.one_time_keyboard
        )
    
    async def _check_premium(self, chat_id: Union[int, str]) -> bool:
        """بررسی پریمیوم بودن کاربر"""
        try:
            user = await self.client.get_entity(chat_id)
            return hasattr(user, 'premium') and user.premium
        except:
            return False
    
    def get_premium_emoji(self, emoji_name: str) -> str:
        """دریافت ایموجی پریمیوم"""
        return self.emoji_manager.get_emoji(emoji_name)
    
    def create_mini_app(
        self,
        app_name: str,
        app_url: str,
        icon_url: str = None,
        webhook_url: str = None
    ) -> MiniApp:
        """
        ایجاد مینی اپ
        
        Args:
            app_name: نام اپ
            app_url: آدرس اپ
            icon_url: آدرس آیکون
            webhook_url: آدرس وب‌هوک
        """
        return MiniApp(
            name=app_name,
            url=app_url,
            icon_url=icon_url,
            webhook_url=webhook_url
        )
    
    async def send_mini_app(
        self,
        chat_id: Union[int, str],
        mini_app: MiniApp,
        title: str = "🎮 مینی اپ",
        description: str = "برای باز کردن اپ کلیک کنید"
    ):
        """
        ارسال مینی اپ
        
        Args:
            chat_id: شناسه چت
            mini_app: شیء مینی اپ
            title: عنوان
            description: توضیحات
        """
        if not self.client:
            raise RuntimeError("کلاینت راه‌اندازی نشده است")
        
        # ساخت کیبورد با دکمه مخصوص مینی اپ
        keyboard = InlineKeyboard([
            [InlineKeyboardButton(
                text="🚀 باز کردن اپ",
                url=mini_app.url,
                color="blue_glass"
            )],
            [InlineKeyboardButton(
                text="ℹ️ اطلاعات",
                callback_data=f"mini_app_info_{mini_app.name}"
            )]
        ])
        
        message = f"""
<b>{title}</b>

📱 {mini_app.name}

{description}

🔗 <a href='{mini_app.url}'>لینک مستقیم</a>
"""
        
        return await self.send_message(
            chat_id,
            message,
            keyboard=keyboard,
            parse_mode="html"
        )
    
    async def run(self):
        """اجرای کلاینت"""
        if not self.client:
            await self.start()
        
        self.logger.info("🚀 ربات شروع به کار کرد...")
        await self.client.run_until_disconnected()