import os
from . import cal

if __name__ == "__main__":
    operating_system = os.name

    match operating_system:
        case "nt": os.system("clear")
        case "posix": os.system("cls")

    