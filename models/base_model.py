from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class BaseModel(ABC):
    id: int | None = field(init=False)
    created_at: datetime = field(init=False)
    updated_at: datetime = field(init=False)

    def __post_init__(self):
        self.id = None
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
