from .constants import D_LINE

ERR_MESSAGE: dict = {
    "ERR_CHOICE(0,5)": "you must choose a value beetwen 1 and 4, or 0",
    "ERR_CHOICE(1,2)": "you must choose either 1 or 2",
    "ERR_LEN": "the coords length Must be X | Y | Z or X | Z length",
    "ERR_Y_RANGE": "y axis must below 320 and above -60",
    "ERR_FILE_MISSING": "portals.json is missing",
    "ERR_FILE_EMPTY": "there is no portal here",
    "ERR_DUPLICATE": "portal already exist",
    "ERR_INDEX_OUT_OF_RANGE": "portal not found",
    "ERR_UNKNOWN_DIMS": "not a valid dimension",
    "ERR_EMPTY_NAME": "name can't be empty",
    "ERR_NUM": "please insert a valid number"
}

def show_err(err_code: str) -> None:
    print(D_LINE)
    message = ERR_MESSAGE.get(err_code, "something went wrong")
    print(f"[!] {message}")
    print(D_LINE)