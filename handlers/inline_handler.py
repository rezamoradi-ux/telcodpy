from typing import Callable, Optional

class InlineHandler:
    """
    مدیریت‌کننده کوئری‌های اینلاین
    """
    
    def __init__(
        self,
        callback: Callable,
        pattern: Optional[str] = None
    ):
        self.callback = callback
        self.pattern = pattern
    
    async def handle(self, event):
        """پردازش رویداد اینلاین"""
        if hasattr(event, 'query'):
            query = event.query if hasattr(event, 'query') else event
            if self.pattern:
                if hasattr(query, 'text') and self.pattern in query.text:
                    return await self.callback(event)
            else:
                return await self.callback(event)
        
        return None
    
    def matches(self, query: str) -> bool:
        """بررسی تطابق با الگو"""
        if not self.pattern:
            return True
        
        return self.pattern in query