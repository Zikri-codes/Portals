from .constants import DELAY_S, D_LINE
from time import sleep as delay

def portals_show_cli(portals: dict[str, ...]) -> None:
    print(D_LINE)
    print("The List of The Portals:")
    for i, portal in enumerate(portals, start=1):
        name_p = portal["Name"]
        dim_p = portal["Dimension"]
        coords_p = portal["Coords"]
        print(f"{i}. {name_p} | {dim_p} | {coords_p}")
        delay(DELAY_S)
    print(D_LINE)