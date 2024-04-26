import json
from typing import Union, Any, Optional


def safely_transfer_to_json_obj(data: Union[dict[str, Any], list[Any]]) -> Union[dict, list]:
    if not isinstance(data, dict) and not isinstance(data, list):
        raise ValueError("not isinstance(data, dict) and not isinstance(data, list)")
    return json.loads(json.dumps(data, ensure_ascii=False, indent=2, default=str))


def safely_transfer_to_json_str(data: Union[dict[str, Any], list[Any]]) -> Optional[str]:
    if not data:
        return None
    return json.dumps(safely_transfer_to_json_obj(data), ensure_ascii=False, indent=2)
