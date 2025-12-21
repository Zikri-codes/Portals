
from .formatter import portal_formatter
import os
import time

def coords_validator(raw_coords: str) -> float:
    raw_coords = raw_coords.strip()
    
    try:
        raw_coords = float(raw_coords)
        return raw_coords
    except ValueError:
        raise ValueError("Coordinate must be a valid number")

def y_validator(raw_y):
    if raw_y is None:
        return "y?"
    
    raw_y = str(raw_y).strip()
    
    if raw_y == "":
        return "y?"
    
    if not raw_y.isdigit():
        return "y?"
    
    try:
        y_value = float(raw_y)
    except ValueError:
        raise ValueError("Y must be a valid number or left empty")
    
    y_value = int(round(y_value))
    
    if y_value <= -60 or y_value >= 319:
        raise ValueError("Y must be below 319 and above -60")
    
    return y_value

def dimension_validator(dimension: str) -> bool:
    dimension = dimension.replace(" ", "").lower()
    if dimension not in ["overworld", "nether", "end"]:
        return True
    return False

def file_exist_validator(FILE) -> bool:
    if not os.path.exists(FILE) or os.stat(FILE).st_size == 0:
        return True

def portal_exist_validator(data, x, y, z, dimension: str) -> bool:
    for portal in data:
        if (
            portal["Coords"] == [x, y, z] and
            portal["Dimension"] == dimension
        ):
            return True
    return False

def input_coords_validator(raw: list[str]) -> str:
    if len(raw) == 3:
        x, y, z = raw
        return x, y, z
    elif len(raw) == 2:
        x, z = raw
        y = None
        return x, y, z
    else:
        for r in raw:
            print("\nCoordinate Must be X Y Z or X Z") if r.isdigit() else print("\nMust be a Valid Number")
        return