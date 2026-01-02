DIMENSIONS = ("overworld", "nether", "end")

def normalize_y(y: str | None) -> str:
    if y is None:
        return "y?"
    try:
        return str(int(round(float(y))))
    except ValueError:
        return "y?"

def resolve_dimension(raw: str) -> tuple[str | None, str | None]:
    query = raw.replace(" ", "").lower()
    for d in DIMENSIONS:
        if d.startswith(query):
            return d.capitalize(), None
    return None, "ERR_UNKNOWN_DIMS"