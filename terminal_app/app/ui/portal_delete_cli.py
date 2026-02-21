from .constants import DELAY_S, D_LINE
from time import sleep as delay

def delete_show(portals: list[dict, ...]) -> None:
    print(D_LINE)
    print("Select The Portals to be deleted")
    for i, portal in enumerate(portals, start=1):
        print(f'{i}. {portal["Name"]}')
        delay(DELAY_S)

def delete_result(name: str) -> None:
    print(f"portal \"{name}\" has been deleted")
    print(D_LINE)