from datetime import datetime

from strategies.pricing_strategy import PricingStrategy
from strategies.weekday_pricing_strategy import WeekdayPricingStrategy
from strategies.weekend_pricing_strategy import WeekendPricingStrategy


class PricingStrategyFactory:
    @staticmethod
    def get_strategy() -> PricingStrategy:
        if datetime.now().weekday() < 5:
            return WeekdayPricingStrategy()
        else:
            return WeekendPricingStrategy()
