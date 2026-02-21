from .constants import TITLE, DELAY_XS, DELAY_S, DELAY_M, T_LINE, D_LINE
from time import sleep as delay

def banner(TITLE: str, *, top: bool = False) -> None:
    if top:
        print(T_LINE)
        delay(DELAY_M)
    
    for ch in TITLE:
        print(ch, end="", flush=True)
        delay(DELAY_XS)
    
    delay(DELAY_M)
    print()
    
    if not top:
        print(T_LINE)

def greet() -> None:
    banner(TITLE, top=False)

def farewell() -> None:
    banner(TITLE, top=True)

def menu() -> None:
    options: list[str] = ["Converter", "Add Portal", "Delete Portal", "Show Portals"]
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
        delay(DELAY_S)
    print("0. Exit")
    print(D_LINE)

def ask() -> str:
    return input(">> ")

if __name__ == "__main__":
    menu()