
from .validator import coords_validator, y_validator

def overworld_nether_converter (x, y, z) -> tuple:
    x = int(round(coords_validator(x)))
    z = int(round(coords_validator(z)))
    y = y_validator(y)
    
    nether_x = x // 8
    nether_z = z // 8
    
    return nether_x, y, nether_z
def nether_overworld_converter (x, y, z) -> dict:
    x = int(round(coords_validator(x)))
    z = int(round(coords_validator(z)))
    y = y_validator(y)
    
    overworld_x = x * 8
    overworld_z = z * 8
    
    return overworld_x, y, overworld_z

