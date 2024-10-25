from typing import Dict, Any, Optional
from decimal import Decimal

class Product:
    def __init__(self, product_id: int, name: str, link: str, regular_price: Optional[Decimal], promo_price: Optional[Decimal], brand: str):
        self.id: int = product_id
        self.name: str = name
        self.link: str = link
        self.regular_price: Optional[Decimal] = regular_price
        self.promo_price: Optional[Decimal] = promo_price
        self.brand: str = brand

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'link': self.link,
            'regular_price': self.regular_price,
            'promo_price': self.promo_price,
            'brand': self.brand
        }