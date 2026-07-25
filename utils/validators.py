from typing import Union, Optional
import re

class Validators:
    """
    کلاس اعتبارسنجی داده‌ها
    """
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """اعتبارسنجی شماره تلفن"""
        pattern = r'^\+?[0-9]{10,15}$'
        return bool(re.match(pattern, phone))
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """اعتبارسنجی ایمیل"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_url(url: str) -> bool:
        """اعتبارسنجی URL"""
        pattern = r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
        return bool(re.match(pattern, url))
    
    @staticmethod
    def validate_username(username: str) -> bool:
        """اعتبارسنجی نام کاربری"""
        pattern = r'^[a-zA-Z0-9_]{3,32}$'
        return bool(re.match(pattern, username))
    
    @staticmethod
    def validate_chat_id(chat_id: Union[int, str]) -> bool:
        """اعتبارسنجی شناسه چت"""
        if isinstance(chat_id, int):
            return True
        if isinstance(chat_id, str):
            return chat_id.startswith('@') or chat_id.isdigit()
        return False
    
    @staticmethod
    def validate_bot_token(token: str) -> bool:
        """اعتبارسنجی توکن ربات"""
        pattern = r'^[0-9]+:[a-zA-Z0-9_-]+$'
        return bool(re.match(pattern, token))
    
    @staticmethod
    def validate_message_id(message_id: int) -> bool:
        """اعتبارسنجی شناسه پیام"""
        return isinstance(message_id, int) and message_id > 0
    
    @staticmethod
    def validate_callback_data(data: str) -> bool:
        """اعتبارسنجی داده کالبک"""
        return isinstance(data, str) and len(data) <= 64

class InputValidator:
    """کلاس پیشرفته اعتبارسنجی ورودی"""
    
    def __init__(self):
        self.validators = Validators()
    
    def validate(self, value: any, validator_type: str) -> bool:
        """اعتبارسنجی با نوع مشخص"""
        validator_map = {
            'phone': self.validators.validate_phone,
            'email': self.validators.validate_email,
            'url': self.validators.validate_url,
            'username': self.validators.validate_username,
            'chat_id': self.validators.validate_chat_id,
            'bot_token': self.validators.validate_bot_token,
            'message_id': self.validators.validate_message_id,
            'callback_data': self.validators.validate_callback_data
        }
        
        validator = validator_map.get(validator_type)
        if validator:
            return validator(value)
        return False
    
    def validate_all(self, data: dict, rules: dict) -> dict:
        """اعتبارسنجی چندین فیلد"""
        errors = {}
        for field, validator_type in rules.items():
            value = data.get(field)
            if value is not None and not self.validate(value, validator_type):
                errors[field] = f"فیلد {field} معتبر نیست"
        return errors