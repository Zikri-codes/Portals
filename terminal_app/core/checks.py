import os

def checks_file(path: str) -> tuple[bool, str | None]:
    if not os.path.exists(path):
        return False, "ERR_FILE_MISSING"
    if os.stat(path).st_size == 0:
        return False, "ERR_FILE_EMPTY"
    return True, None

def portal_exists(data: list[dict], x: str, y: str, z: str, dimension: str) -> tuple[bool, str | None]:
    for portal in data:
        if portal["Coords"] == [x, y, z] and portal["Dimension"] == dimension:
            return False, "ERR_DUPLICATE"
    return True, None