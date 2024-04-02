# # import calculator as cal
import os

def heading():
    operating_system = os.name
    match operating_system:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print(25*"=")
    print("TLI calculator".center(25))
    print(25*"=" + "\n")

while(True):
    heading()

    # ambil input
    angka1 = float(input(" "))
    heading()
    operator = input(f"{angka1} ")
    heading()
    angka2 = float(input(f"{angka1} {operator} "))

    match operator:
        case "+": hasil = angka1 + angka2
        case "-": hasil = angka1 - angka2
        case  "/": hasil = angka1 / angka2
        case operator if "*" or "x": hasil = angka1*angka2
    # print(hasil)

    print(f"{angka1} {operator} {angka2} = {hasil}")

    input("pause")
    

#         # print(25*"=")
#         # print("TLI calculator".center(25))
#         # print(25*"=" + "\n")


#         # angka_1 = float(input(" "))
#         # operator = input(f"{angka_1} ")
#         # angka_2 = float(input(f"{angka_1} {operator} "))

#         # # percabangannya

#         # if operator == "+":
#         #     hasil = angka_1 + angka_2
#         #     print(f"hasilnya adalah {hasil}")
#         # elif operator == "-":
#         #     hasil = angka_1 - angka_2
#         #     print(f"hasilnya adalah {hasil}")
#         # elif operator == "x" or operator == "*":
#         #     hasil = angka_1 * angka_2
#         #     print(f"hasilnya adalah {hasil}")
#         # elif operator == "/":
#         #     hasil = angka_1 / angka_2
#         #     print(f"hasilnya adalah {hasil}")

# print(50.0 / 5.0)