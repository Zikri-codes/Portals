# Minecraft Coords Library

from core import *
from storage import *
from utils import *
from time import sleep as d

default_line = "-" * 40
running = True

def main(user: str):
    if user == "1":
        converter = show_converter_menu()
        if converter == "1":
            try:
                x, y, z = show_detailed_converter_menu("1")
            except TypeError:
                return
            xo, yo, zo = nether_overworld_converter(x, y, z)
            print(f"\nOutput : {xo} | {yo} | {zo}")
            print(default_line)
            d(0.5)
        elif converter == "2":
            try:
                x, y, z = show_detailed_converter_menu("2")
            except TypeError:
                return
            xn, yn, zn = overworld_nether_converter(x, y, z)
            print(f"\nOutput : {xn} | {yn} | {zn}")
            print(default_line)
            d(0.5)
        else:
            print("Must choose 1/2") if converter.isdigit() else print("Must be a Valid Number")
            print(default_line)
            d(0.5)
    elif user == "2":
        try:
            name, dimension, x, y, z = show_add_menu()
        except TypeError:
            return
        adder = add_datamanager(x, y, z, dimension, name)
        print(f"\n\"{name}\" Has been added to the portals") if adder else print("Something went wrong")
        print(default_line)
        d(0.5)
    elif user == "3":
        portals = load_datamanager()
        deleted_portal = show_delete_menu(portals)
        if not portals:
            print(default_line)
            d(0.5)
            return
        if deleted_portal == "0":
            print("[0] Canceled")
            print(default_line)
            d(0.5)
            return
        if deleted_portal == "" or deleted_portal == None:
            print("Can't be Empty")
            print(default_line)
            d(0.5)
            return
        try:
            deleted_portal = int(deleted_portal) - 1
        except ValueError:
            print("Must be a Valid Number")
            print(default_line)
            d(0.5)
            return
        delete_datamanager(deleted_portal)
        recent_deleted = portals[deleted_portal]["Name"]
        print(f"\n\"{recent_deleted}\" Has been deleted")
        print(default_line)
        d(0.5)
    elif user == "4":
        portals = load_datamanager()
        show_portals_menu(portals)
        print(default_line)
        d(0.5)
    elif user == "0":
        close_menu()
        return "0"
    else:
        print("Must choose 0-5") if user.isdigit() else print("Must be a number!")
        print(default_line)

greet_menu()
while running:
    option_menu()
    user = input("\nChoose(num) : ").strip()
    result = main(user)
    if result == "0":
        running = False