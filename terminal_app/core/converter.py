def converter(x: int, y: int | str, z: int, to_nether: bool) -> tuple[int, str | int, int]:
    if to_nether:
        return  x // 8, y, z // 8
    return x * 8, y, z * 8