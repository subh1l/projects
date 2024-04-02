import os

def refresh():
        operating_system = os.name

        match operating_system:
                case "posix": return os.system("clear")
                case "nt": return os.system("cls")