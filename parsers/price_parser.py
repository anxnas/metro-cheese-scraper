import re
from decimal import Decimal
from typing import Optional

class PriceParser:
    @staticmethod
    def parse(price_str: Optional[str]) -> Optional[Decimal]:
        if price_str:
            price_str = re.sub(r'[^\d.]', '', price_str)
            return Decimal(price_str)
        return None