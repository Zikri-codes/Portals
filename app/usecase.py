from core.config import DATA_PATH
from core.parsers import parse_coords, parse_num
from core.normalizers import normalize_y, resolve_dimension
from core.validator import valid_y
from core.checks import checks_file, portal_exists
from core.converter import converter
from core.formatter import formatter
from data.repository import load_portals, save_portals

def convert_portal(raw: list[str], choice: str) -> dict:
    if choice == "2":
        to_nether = True
    elif choice == "1":
        to_nether = False
    else:
        return {"ok": False, "err": "ERR_CHOICE(1,2)"}
    
    coords, err = parse_coords(raw)
    if err:
        return {"ok": False, "err": err}
    
    x, y, z = coords
    
    x, err = parse_num(x)
    if err:
        return {"ok": False, "err": err}
    y, err = valid_y(normalize_y(y))
    if err:
        return {"ok": False, "err": err}
    z, err = parse_num(z)
    if err:
        return {"ok": False, "err": err}
    
    conv_x, conv_y, conv_z = converter(x, y, z, to_nether)
    
    return {
        "ok": True,
        "result": (
            str(conv_x),
            str(conv_y),
            str(conv_z)
            )
    }

def delete_portal(choice: str) -> dict:
    ok, err = checks_file(DATA_PATH)
    if not ok:
        return {"ok": False, "err": err}
    
    portals = load_portals(DATA_PATH)
    if not portals:
        return {"ok": False, "err": "ERR_FILE_EMPTY"}
    
    index, err = parse_num(choice)
    if err:
        return {"ok": False, "err": err}
    
    index -= 1
    if index < 0 or index >= len(portals):
        return {"ok": False, "err": "ERR_INDEX_OUT_OF_RANGE"}
    
    deleted = portals.pop(index)
    save_portals(portals, DATA_PATH)
    
    return {
        "ok": True,
        "deleted": deleted
    }

def show_portals() -> dict:
    ok, err = checks_file(DATA_PATH)
    if not ok:
        return {"ok": False, "err": err}
    
    portals = load_portals(DATA_PATH)
    if not portals:
        return {"ok": False, "err": "ERR_FILE_EMPTY"}

    return {
        "ok": True,
        "data": portals
    }

def add_portals(raw_name: str, raw_dims: str, raw_coords: list[str]) -> dict:
    if raw_name == "" or raw_name is None:
        return {"ok": False, "err": "ERR_EMPTY_NAME"}
    
    dims, err = resolve_dimension(raw_dims)
    if err:
        return {"ok": False, "err": err}
    
    coords, err = parse_coords(raw_coords)
    if err:
        return {"ok": False, "err": err}
    
    x, y, z = coords
    
    x, err = parse_num(x)
    if err:
        return {"ok": False, "err": err}
    y, err = valid_y(normalize_y(y))
    if err:
        return {"ok": False, "err": err}
    z, err = parse_num(z)
    if err:
        return {"ok": False, "err": err}
    
    x = str(x)
    y = str(y)
    z = str(z)
    
    portals = load_portals(DATA_PATH)
    
    ok, err = portal_exists(portals, x, y, z, dims)
    if not ok:
        return {"ok": False, "err": err}
    
    portal = formatter(raw_name, dims, x, y, z)
    
    added = portals.append(portal)
    save_portals(portals, DATA_PATH)
    
    return {
        "ok": True,
        "name": raw_name
    }