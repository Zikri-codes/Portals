def parse_num(raw_num: str) -> tuple[int | None, str | None]:
    raw_num = raw_num.strip()
    try:
        return int(round(float(raw_num))), None
    except ValueError:
        return None, "ERR_NUM"

def parse_coords(raw: list[str]) -> tuple[tuple[str, str | None, str] |  None, str | None]:
    if len(raw) not in (2, 3):
        return None, "ERR_LEN"
    for r in raw:
        if not r.replace("-", "", 1).isdigit():
            return None, "ERR_NUM"
    if len(raw) == 2:
        return (raw[0], None, raw[1]), None
    return (raw[0], raw[1], raw[2]), None