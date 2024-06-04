import os
import crud as crud

if __name__ == "__main__":
    operating_system = os.name

    match operating_system:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

    print("="*25)    
    print("WELCOME TO THE".center(25))
    print("crud PROJECT".center(25))
    print("="*25)    

    crud.init_terminal()

    while(True):
        match operating_system:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("="*25)    
        print("WELCOME TO THE".center(25))
        print("crud PROJECT".center(25))
        print("="*25)

        print("1. Create Data")
        print("2. Read Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. exit\n")

        user_option = input("Option: ")


        match user_option:
            case "1": crud.create_terminal()
            case "2": crud.read_terminal()
            case "3": crud.update_terminal()
            case "4": crud.delete_terminal()
            case "5": exit()
              
        finish = input("Are you done?[Y/n]")
        if finish == "y" or finish == "Y":
          break

print("End of program")