from typing import Optional

class MiniApp:
    """مدیریت مینی اپ‌ها"""
    def __init__(
        self,
        name: str,
        url: str,
        icon_url: Optional[str] = None,
        webhook_url: Optional[str] = None,
        data: Optional[dict] = None
    ):
        self.name = name
        self.url = url
        self.icon_url = icon_url
        self.webhook_url = webhook_url
        self.data = data or {}
    
    def set_data(self, key: str, value: Any):
        """تنظیم داده برای اپ"""
        self.data[key] = value
    
    def get_data(self, key: str, default: Any = None):
        """دریافت داده از اپ"""
        return self.data.get(key, default)
    
    def to_dict(self):
        """تبدیل به دیکشنری"""
        return {
            "name": self.name,
            "url": self.url,
            "icon_url": self.icon_url,
            "webhook_url": self.webhook_url,
            "data": self.data
        }