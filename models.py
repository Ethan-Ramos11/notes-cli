from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Note:
    id: Optional[int]
    title: str
    content: Optional[str]
    tags: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
