import re
from pydantic import BaseModel, Field, field_validator

BANNED_WORDS = ["кринж", "рофл", "вайб"]

class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)

    @field_validator("message")
    @classmethod
    def check_banned_words(cls, v: str) -> str:
        text_lower = v.lower()
        for word in BANNED_WORDS:
            if re.search(re.escape(word[:4]), text_lower):
                raise ValueError("Использование недопустимых слов")
        return v
