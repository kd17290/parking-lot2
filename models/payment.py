import uuid
from dataclasses import dataclass, field
from enum import Enum

from models.base_model import BaseModel


class PaymentStatus(Enum):
    CREATED = "created"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


@dataclass
class Payment(BaseModel):
    ticket_id: int
    amount: float
    third_party_txn_id: str = field(default_factory=str)
    txn: str = field(init=False)
    status: PaymentStatus = field(default=PaymentStatus.CREATED)

    def __post_init__(self):
        super().__post_init__()
        self.txn = uuid.uuid4().hex
