from app.ui import portal_add_cli as ui_add
from app.ui import portal_show_cli as ui_show
from app.ui import portal_delete_cli as ui_del
from app.ui import converter_cli as ui_conv
from app.ui import errors_cli as ui_err
from app.ui import commons_cli as ui_cmn
from app import usecase as usc
from data import repository as dat_repo
from core import config as conf

def _conv(opt_conv: str) -> None:
    coords = ui_conv.conv_ask_coords()
    result = usc.convert_portal(coords, opt_conv)
    if not result["ok"]:
        ui_err.show_err(result["err"])
        return
    x, y, z = result["result"]
    ui_conv.conv_result(x, y, z)

def _opt1() -> None:
    ui_conv.conv_show()
    opt = ui_cmn.ask()
    if opt == "1":
        _conv(opt)
    elif opt == "2":
        _conv(opt)
    else:
        ui_err.show_err("ERR_CHOICE(1,2)")

def _opt2() -> None:
    data = ui_add.add_prompt()
    name, dims, coords = data
    result = usc.add_portals(name, dims, coords)
    if not result["ok"]:
        ui_err.show_err(result["err"])
        return
    ui_add.add_result(result["name"])

def _opt3() -> None:
    portals = dat_repo.load_portals(conf.DATA_PATH)
    ui_del.delete_show(portals)
    opt_del = ui_cmn.ask()
    result = usc.delete_portal(opt_del)
    if not result["ok"]:
        ui_err.show_err(result["err"])
        return
    ui_del.delete_result(result["deleted"]["Name"])

def _opt4() -> None:
    portals = usc.show_portals()
    ui_show.portals_show_cli(portals["data"])

def main() -> None:
    ui_cmn.greet()
    while True:
        ui_cmn.menu()
        opt = ui_cmn.ask()
        
        if opt == "1":
            _opt1()
        elif opt == "2":
            _opt2()
        elif opt == "3":
            _opt3()
        elif opt == "4":
            _opt4()
        elif opt == "0":
            ui_cmn.farewell()
            return
        else:
            ui_err.show_err("ERR_CHOICE(0,5)")
        
if __name__ == "__main__":
    main()