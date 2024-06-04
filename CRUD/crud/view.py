from . import operation

def delete_terminal():
    read_terminal() 
    while(True):
        print("Please choose number that will be deleted")
        book_num = int(input("Book number: "))
        book_data = operation.read(index = book_num)

        if book_data:
            data_break = book_data.split(",")
            pk = data_break[0]
            data_add = data_break[1]
            writer = data_break[2]
            title = data_break[3]
            year = data_break[4][:-1]   

            print("\n"+"="*100)
            print("\nFollowing data will be deleted")
            print(f"1. Title\t: {title:.40}")            
            print(f"2. Writer\t: {writer:.40}")
            print(f"3. Year\t\t: {year:.4}")
            finish = input("Are you sure?[Y/n]")
            if finish == "y" or finish == "Y":
                operation.delete(book_num)
                break 
        else:
            print("Invalid number, please try again")

    print("Data deleted")

def update_terminal():
    read_terminal()
    while(True):
        print("Please choose number that will be updated")
        book_num = int(input("Book number: "))
        book_data = operation.read(index = book_num)  

        if book_data:
            break
        else:
            print("Invalid number, please try again")

    data_break = book_data.split(",")
    pk = data_break[0]
    data_add = data_break[1]
    writer = data_break[2]
    title = data_break[3]
    year = data_break[4][:-1]
     
    while(True):
        print("\n"+"="*100)
        print("\nPlease enter data desired to be updated")
        print(f"1. Title\t: {title:.40}")
        print(f"2. Writer\t: {writer:.40}")
        print(f"3. Year\t\t: {year:.4}")

        user_option = input("Choose data [1, 2, 3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": title =  input("Title\t: ")
            case "2": writer =  input("Writer\t: ")
            case "3":
                while(True):
                    try:
                        year = int(input("Year\t: "))
                        if len(str(year)) == 4:
                            break
                        else:
                            print("Year only support 4 number")
                    except:
                        print("Year must in number, please try again")
            case _: print("Invalid index")

        print("New data")
        print(f"1. Title\t: {title:.40}")
        print(f"2. Writer\t: {writer:.40}")
        print(f"3. Year\t: {year:4}")
        finish = input("Is the data correct?[Y/n]")
        if finish == "y" or finish == "Y":
          break

    operation.update(book_num, pk, data_add, year, title, writer)


def create_terminal():
    print("\n\n"+"="*100)
    print("Add data")
    writer = input("Writer\t: ")
    title = input("Title\t: ")
    while(True):
        try:
            year = int(input("Year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("Year only support 4 number")
            break
        except:
            print("Year must in number, please re-enter year data")

    operation.create(year, title, writer)
    print("\nThis is your new data")
    read_terminal()

def read_terminal():
    data_file = operation.read()
    index = "No"
    title = "Title"
    writer = "Writer"
    year = "Year"

    print("\n"+"="*100)
    print(f"{index:4} | {title:40} | {writer:40} | {year:5}")
    print("-"*100)

    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        writer = data_break[2]
        title = data_break[3]
        year = data_break[4]
        print(f"{index+1:4} | {title:.40} | {writer:.40} | {year:4}",end="")


    print("="*100+"\n")
