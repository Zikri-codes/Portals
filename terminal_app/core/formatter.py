def formatter(name: str, dimension: str, x: str, y: str, z: str) -> dict:
    return {
        # "ID": _id, next update lol
        "Name": name,
        "Dimension": dimension,
        "Coords": [x, y, z]
    }