from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime


@dataclass
class Note:
    id: Optional[int]
    title: str
    content: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
