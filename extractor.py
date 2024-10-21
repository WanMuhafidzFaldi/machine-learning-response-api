def extract_json(data, parent_key=''):
    items = []
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            items.extend(extract_json(v, new_key))
    elif isinstance(data, list):
        for i, v in enumerate(data):
            new_key = f"{parent_key}[{i}]"
            items.extend(extract_json(v, new_key))
    else:
        items.append((parent_key, data))
    return items