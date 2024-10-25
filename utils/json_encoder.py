import json
from decimal import Decimal
from typing import Any, Union

class JSONEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Union[float, Any]:
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)