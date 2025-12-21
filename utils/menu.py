
from core import input_coords_validator, dimension_validator
import sys
import time

default_line = "-" * 40

def greet_menu() -> None:
    text: str = "Storage of Coords ·  · Library of Coords"
    for t in text:
        print(t, end="", flush=True)
        time.sleep(0.015)
    time.sleep(0.25)
    print("\n" + "—" * len(text))
def option_menu() -> None:
    menu: list[str] = ["Converter", "Add Portal", "Delete Portal", "Show Portal"]
    for i, m in enumerate(menu, start=1):
        print(f"{i}. {m}")
        time.sleep(0.1)
    time.sleep(0.1)
    print("0. Exit")
def show_detailed_converter_menu(choice: str) -> tuple[str]:
    if choice == "1":
        print(default_line)
        print("Nether → Overworld : Converter")
        print("\nInput : X | Y | Z")
        coords = input("Input : ").strip().split()
        try:
            x, y, z = input_coords_validator(coords)
        except TypeError:
            print(default_line)
            time.sleep(0.5)
            return
        return x, y, z
    elif choice == "2":
        print(default_line)
        print("Overworld  → Nether: Converter")
        print("\nInput : X | Y | Z")
        coords = input("Input : ").strip().split()
        try:
            x, y, z = input_coords_validator(coords)
        except TypeError:
            print(default_line)
            time.sleep(0.5)
            return
        return x, y, z
def show_converter_menu() -> str:
    print(default_line)
    text = "Converter:\n1. Nether → Overworld\n2. Overworld → Nether"
    print(text)
    time.sleep(0.5)
    user = input("\nChoose(1/2) : ")
    return user
def show_add_menu():
    print(default_line)
    name = input("Name      : ").strip()
    if name == "" or name == None:
        print("\nName can't be empty")
        print(default_line)
        time.sleep(0.5)
        return
    dimension = input("Dimension : ").capitalize()
    if dimension_validator(dimension):
        print(f"\nInvalid dimension: \"{dimension}\"")
        print('Hint: dimension must be in this list\n["Overworld", "Nether", "End"]')
        print(default_line)
        time.sleep(0.5)
        return
    coords = input("Coords    : ").strip().split()
    x, y, z = input_coords_validator(coords)
    return name, dimension, x, y, z
def show_delete_menu(portals):
    print(default_line)
    if not portals:
        print("There's no portals here!")
        return
    print("Wich portals do you want to delete? 0 for cancel")
    for i, portal in enumerate(portals, start=1):
        print(f"{i}. {portal['Name']}")
        time.sleep(0.1)
    deleted_portal = input("\nChoose(num) : ")
    return deleted_portal
def show_portals_menu(portals):
    print(default_line)
    if not portals:
        print("There's no portals here!")
        return
    print("The List of The Portals:")
    time.sleep(0.2)
    for i, portal in enumerate(portals, start=1):
        print(f"{i}. {portal["Name"]} | {portal["Dimension"]} | {portal["Coords"]}")
        time.sleep(0.1)
def close_menu():
    text: str = "Storage of Coords ·  · Library of Coords"
    print("—" * len(text))
    time.sleep(0.25)
    for t in text:
        print(t, end="", flush=True)
        time.sleep(0.015)
    print("")

if __name__ == "__main__":
    # greet_menu()
    # time.sleep(0.6)
    # option_menu()
    # converter_menu()
    show_detailed_converter_menu("1")