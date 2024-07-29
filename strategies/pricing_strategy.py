from abc import ABC, abstractmethod
from datetime import datetime

from models.vehicle import Vehicle


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(
        self, entry_time: datetime, exit_time: datetime, vehicle: Vehicle
    ) -> float:
        ...
