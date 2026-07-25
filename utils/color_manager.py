class ColorManager:
    """مدیریت رنگ‌های شیشه‌ای"""
    
    GLASS_COLORS = {
        "blue_glass": {
            "bg": "#4A90E2",
            "text": "#FFFFFF",
            "glass": "rgba(255,255,255,0.2)"
        },
        "red_glass": {
            "bg": "#E74C3C",
            "text": "#FFFFFF",
            "glass": "rgba(255,255,255,0.2)"
        },
        "green_glass": {
            "bg": "#2ECC71",
            "text": "#FFFFFF",
            "glass": "rgba(255,255,255,0.2)"
        },
        "purple_glass": {
            "bg": "#9B59B6",
            "text": "#FFFFFF",
            "glass": "rgba(255,255,255,0.2)"
        },
        "gold_glass": {
            "bg": "#F39C12",
            "text": "#FFFFFF",
            "glass": "rgba(255,255,255,0.2)"
        },
        "pink_glass": {
            "bg": "#E91E63",
            "text": "#FFFFFF",
            "glass": "rgba(255,255,255,0.2)"
        },
        "cyan_glass": {
            "bg": "#00BCD4",
            "text": "#FFFFFF",
            "glass": "rgba(255,255,255,0.2)"
        },
        "orange_glass": {
            "bg": "#FF6F00",
            "text": "#FFFFFF",
            "glass": "rgba(255,255,255,0.2)"
        },
        "indigo_glass": {
            "bg": "#3F51B5",
            "text": "#FFFFFF",
            "glass": "rgba(255,255,255,0.2)"
        },
        "teal_glass": {
            "bg": "#009688",
            "text": "#FFFFFF",
            "glass": "rgba(255,255,255,0.2)"
        }
    }
    
    def apply_glass_effect(self, text: str, color_name: str) -> str:
        """اعمال افکت شیشه‌ای روی دکمه"""
        if color_name in self.GLASS_COLORS:
            color = self.GLASS_COLORS[color_name]
            # ساخت دکمه با افکت شیشه‌ای (برای تلگرام به صورت متن برمی‌گردانیم)
            return f"✨ {text} ✨"
        return text
    
    def get_glass_colors(self) -> list:
        """دریافت لیست رنگ‌های شیشه‌ای"""
        return list(self.GLASS_COLORS.keys())