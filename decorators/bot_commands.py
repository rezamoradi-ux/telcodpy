from functools import wraps
from typing import Callable, Optional

def on_message(pattern: Optional[str] = None, is_regex: bool = False):
    """
    دکوراتور برای مدیریت پیام‌ها
    
    Args:
        pattern: الگوی پیام
        is_regex: آیا الگو regex است
    """
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)
        
        wrapper._is_handler = True
        wrapper._handler_type = 'message'
        wrapper._pattern = pattern
        wrapper._is_regex = is_regex
        return wrapper
    return decorator

def on_callback(pattern: Optional[str] = None, is_regex: bool = False):
    """
    دکوراتور برای مدیریت کالبک‌ها
    
    Args:
        pattern: الگوی کالبک
        is_regex: آیا الگو regex است
    """
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)
        
        wrapper._is_handler = True
        wrapper._handler_type = 'callback'
        wrapper._pattern = pattern
        wrapper._is_regex = is_regex
        return wrapper
    return decorator

def on_inline(pattern: Optional[str] = None):
    """
    دکوراتور برای مدیریت کوئری‌های اینلاین
    
    Args:
        pattern: الگوی کوئری
    """
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)
        
        wrapper._is_handler = True
        wrapper._handler_type = 'inline'
        wrapper._pattern = pattern
        return wrapper
    return decorator

def admin_only(admin_ids: list):
    """
    دکوراتور برای محدود کردن دسترسی به ادمین‌ها
    
    Args:
        admin_ids: لیست شناسه‌های ادمین
    """
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # دریافت کاربر از رویداد
            event = args[0] if args else None
            if event and hasattr(event, 'sender_id'):
                if event.sender_id not in admin_ids:
                    return await event.answer("⛔ شما دسترسی به این بخش ندارید!")
            return await func(*args, **kwargs)
        return wrapper
    return decorator

def rate_limit(limit: int = 5, per_seconds: int = 60):
    """
    دکوراتور برای محدودیت نرخ
    
    Args:
        limit: تعداد مجاز در بازه زمانی
        per_seconds: بازه زمانی به ثانیه
    """
    from collections import defaultdict
    import time
    
    last_calls = defaultdict(list)
    
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # دریافت کاربر از رویداد
            event = args[0] if args else None
            if event and hasattr(event, 'sender_id'):
                user_id = event.sender_id
                now = time.time()
                
                # پاک کردن درخواست‌های قدیمی
                last_calls[user_id] = [t for t in last_calls[user_id] if now - t < per_seconds]
                
                if len(last_calls[user_id]) >= limit:
                    return await event.answer(f"⏳ لطفاً {per_seconds} ثانیه صبر کنید!")
                
                last_calls[user_id].append(now)
            
            return await func(*args, **kwargs)
        return wrapper
    return decorator

def log_activity(logger):
    """
    دکوراتور برای لاگ کردن فعالیت‌ها
    
    Args:
        logger: شیء لاگر
    """
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                logger.info(f"Executing {func.__name__}")
                result = await func(*args, **kwargs)
                logger.info(f"Successfully executed {func.__name__}")
                return result
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {e}")
                raise
        return wrapper
    return decorator