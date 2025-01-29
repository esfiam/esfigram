def serialize_clean(obj):
    if obj is None:
        return None

    if isinstance(obj, dict):
        new_dict = {}
        for k, v in obj.items():
            cleaned = serialize_clean(v)
            if cleaned is not None:
                new_dict[k] = cleaned
        return new_dict

    if isinstance(obj, list):
        new_list = []
        for item in obj:
            cleaned = serialize_clean(item)
            if cleaned is not None:
                new_list.append(cleaned)
        return new_list

    if isinstance(obj, bool):
        return int(obj)

    if hasattr(obj, "to_dict") and callable(obj.to_dict):
        return serialize_clean(obj.to_dict())

    return obj


def replace_reserved_keys(data: dict) -> dict:
    RESERVED_KEYS = {"from": "from_user"}

    def process_item(item):
        if isinstance(item, dict):
            return {RESERVED_KEYS.get(k, k): process_item(v) for k, v in item.items()}
        if isinstance(item, list):
            return [process_item(v) for v in item]
        return item

    return process_item(data)
