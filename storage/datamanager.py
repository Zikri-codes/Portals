
from core import portal_exist_validator, file_exist_validator, portal_formatter, y_validator, dimension_validator
import json

FILE = "storage/portals.json"

def load_datamanager() -> list:
    if file_exist_validator(FILE):
        return []
    with open(FILE, 'r') as f:
        return json.load(f)

def save_datamanager(data) -> None:
    with open(FILE, 'w') as f:
        json.dump(data, f)

def delete_datamanager(index: int):
    data = load_datamanager()
    
    if index < 0 or index >= len(data):
        return False
    
    deleted = data.pop(index)
    save_datamanager(data)
    return deleted

def add_datamanager(x: int, y, z: int, dimension: str, name: str) -> bool:
    y = y_validator(y)
    data = load_datamanager()
    if portal_exist_validator(data, x, y, z, dimension):
        print("Portal already exist!")
        return False
    portal = portal_formatter(name, dimension, x, y, z)
    
    data.append(portal)
    save_datamanager(data)
    return True
    
