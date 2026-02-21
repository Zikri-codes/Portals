def valid_y(y: str) -> tuple[str | int, None]:
    if y == "y?":
        return "y?", None
    inty = int(y)
    if (-60 <= inty <= 320):
        return inty, None
    return "y?", None