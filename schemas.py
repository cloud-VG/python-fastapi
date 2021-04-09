from pydantic import BaseModel
from typing import List, Optional


class Audio(BaseModel):
    type: str
    id: int
    name: str
    duration: int
    host: Optional[str] = None
    participants: List[str] = []
    author: Optional[str] = None
    narrator: Optional[str] = None
