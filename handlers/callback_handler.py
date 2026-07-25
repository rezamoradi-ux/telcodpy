from typing import Callable, Optional, Pattern
import re

class CallbackHandler:
    """
    مدیریت‌کننده کالبک‌ها
    """
    
    def __init__(
        self,
        callback: Callable,
        pattern: Optional[str] = None,
        is_regex: bool = False
    ):
        self.callback = callback
        self.pattern = pattern
        self.is_regex = is_regex
        self._compiled_pattern = None
        
        if pattern and is_regex:
            self._compiled_pattern = re.compile(pattern)
    
    async def handle(self, event):
        """پردازش رویداد کالبک"""
        if not hasattr(event, 'data'):
            return None
        
        data = event.data.decode('utf-8') if hasattr(event.data, 'decode') else str(event.data)
        
        if self.pattern:
            if self.is_regex:
                if self._compiled_pattern and self._compiled_pattern.match(data):
                    return await self.callback(event)
            else:
                if self.pattern in data:
                    return await self.callback(event)
        else:
            return await self.callback(event)
        
        return None
    
    def matches(self, data: str) -> bool:
        """بررسی تطابق با الگو"""
        if not self.pattern:
            return True
        
        if self.is_regex and self._compiled_pattern:
            return bool(self._compiled_pattern.match(data or ""))
        
        return self.pattern in (data or "")