from datetime import datetime

from models.vehicle import Vehicle
from strategies.pricing_strategy import PricingStrategy


class WeekdayPricingStrategy(PricingStrategy):
    def calculate_price(
        self, entry_time: datetime, exit_time: datetime, vehicle: Vehicle
    ) -> float:
        print(f"Amount calculated using WeekdayPricingStrategy")
        return 100
