def formatter(name: str, dimension: str, x: str, y: str, z: str) -> dict:
    return {
        "Name": name,
        "Dimension": dimension,
        "Coords": [x, y, z]
    }