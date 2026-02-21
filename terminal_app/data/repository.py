import json

def load_portals(file: str) -> list[dict]:
    with open(file, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_portals(portal: list[dict], file: str) -> None:
    with open(file, 'w') as f:
        json.dump(portal, f)