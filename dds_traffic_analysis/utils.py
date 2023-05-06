
from typing import Any, Dict


def add_key_to_dict(_dict: Dict, key: Any, initial_value: Any) -> Any:
    if _dict.get(key) is None:
        _dict[key] = initial_value
    return _dict[key]
