import json

def load_portals(file: str) -> list[dict]:
    with open(file, 'r') as f:
        return json.load(f)

def save_portals(portal: list[dict], file: str) -> None:
    with open(file, 'w') as f:
        json.dump(portal, f)