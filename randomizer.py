import random
import os

def main_menu():
    os.system("clear")
    print("1. random name picker")
    print("2. random team generator")
    print("3. exit\n")

    choice = input("Your choice: ")

    if choice == "1":
        names = input("enter names[comma separated]: ")
        names = [name for name in names.split(",")]
        random_name(names)
        pause()
        main_menu()

    elif choice == "2":
        names = input("enter names[comma separated]: ")
        names = [name for name in names.split(",")]
        number = int(input("enter number of groups: "))
        random_team(names, number)
        pause()
        main_menu()

    elif choice == "3":
        exit()

    else:
        print("invalid choice")
        main_menu()

def random_team(names, number):
    random.shuffle(names)
    size = len(names) // number
    groups = []
    for i in range(number):
        group = names[i*size :(i + 1)*size]
        groups.append(group)
    
    for i in range(len(names) % number):
        groups[i].append(names[(i + 1)*(-1)])
    result = groups

    for i, group in enumerate(result):
        print(f"group {i + 1}: {', '.join(group)}")

def random_name(names):
    name = random.choices(names)
    print(name)

def pause():
    input("Press any key ")


if __name__ == "__main__":
    main_menu()