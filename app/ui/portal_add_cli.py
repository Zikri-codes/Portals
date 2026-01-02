from .constants import D_LINE

def add_prompt() -> tuple[str, str, list[str, ...]]:
    print(D_LINE)
    name = input("Name        : ")
    dimension = input("Dimension   : ")
    coords = input("Coordinate  : ").strip().split()
    return name, dimension, coords

def add_result(name: str) -> None:
    print(f"\nportal \"{name}\" has been added")
    print(D_LINE)