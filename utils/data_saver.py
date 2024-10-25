import json
from typing import List
from models.product import Product
from utils.json_encoder import JSONEncoder

class DataSaver:
    @staticmethod
    def save_to_json(data: List[Product], filename: str) -> None:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([product.to_dict() for product in data], f, ensure_ascii=False, indent=2, cls=JSONEncoder)