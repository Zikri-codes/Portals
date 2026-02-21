from .constants import DELAY_S, D_LINE
from time import sleep as delay

def conv_show() -> None:
    print(D_LINE)
    print("Converter:")
    delay(DELAY_S)
    for i, opt in enumerate(("Nether → Overworld", "Overworld → Nether"), start=1):
        print(f"{i}. {opt}")
        delay(DELAY_S)

def conv_ask_coords() -> list[str, ...]:
    print(D_LINE)
    print("Input : X | Y | Z")
    raw = input("Input : ").strip().split()
    return raw

def conv_result(conv_x: str, conv_y: str, conv_z: str) -> None:
    print(f"Output : {conv_x} | {conv_y} | {conv_z}")
    delay(DELAY_S)
    print(D_LINE)