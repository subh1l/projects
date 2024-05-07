import os
import CRUD as CRUD

if __name__ == "__main__":
    operating_system = os.name

    match operating_system:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

    print("WELCOME TO THE")
    print("CRUD PROJECT")
    print("=============================")    

    CRUD.init_terminal()

    while(True):
        match operating_system:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("WELCOME TO THE")
        print("CRUD PROJECT")
        print("=============================")

        print("1. Create Data")
        print("2. Read Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. exit\n")

        user_option = input("Option: ")


        match user_option:
            case "1": CRUD.create_terminal()
            case "2": CRUD.read_terminal()
            case "3": CRUD.update_terminal()
            case "4": CRUD.delete_terminal()
            case "5": exit()
              
        finish = input("Are you done?[Y/n]")
        if finish == "y" or finish == "Y":
          break

print("End of program")