# from beanie import Document
# from pydantic import BaseModel, Field
# from datetime import datetime
# import uuid

# def get_current_datetime():
#     return datetime.now()

# class CommonModel(Document):
#     id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
#     is_active: bool = Field(default=True)
#     created_at: datetime = Field(default_factory=get_current_datetime)
#     updated_at: datetime = Field(default_factory=get_current_datetime)

#     class Settings:
#         use_state_management = True

#     def save(self, **kwargs):
#         self.updated_at = get_current_datetime()
#         return super().save(**kwargs)

# common.py
from beanie import Document, Indexed
from pydantic import Field
from typing import Optional
from datetime import datetime
import uuid

class CommonModel(Document):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        use_state_management = True
        state_management_update_strategy = "ALWAYS"

    def save(self, **kwargs):
        self.updated_at = datetime.utcnow()
        return super().save(**kwargs)

    class Config:
        orm_mode = True



