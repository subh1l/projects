import os
import math

if __name__ == "__main__":
    operating_sys = os.name
    while(True):
        match operating_sys:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print(25*"=")
        print("Basic calculator".center(25))
        print(25*"=")

        while(True):
            num1 = input('first number: ')
            if num1 == 'ans':
                try:
                    num1 = result
                    break
                except:
                    num1 = 0
            if num1 != 'ans':
                try:
                    int(num1)
                    break
                except:
                    print('must be number')
                    continue
            
        operator = input("operator[+,-,*,/,root,sqr,pow]: ")
        if operator == "root" or operator == "sqr":
            pass
        else:
            while(True):
                try:
                    num2 = int(input("second number: "))
                    break
                except:
                    print("must be number")
                    continue
                

        confirm = input("Are you sure?[Y/n]")
        if confirm == "n":
            continue
        else:
            match operator:
                case "+": result = num1 + num2
                case "-": result = num1 - num2
                case "*": result = num1*num2
                case "/": result = num1 / num2
                case "root": result = math.sqrt(num1)
                case "sqr": result = num1*num1
                case "pow": result = num1**num2

            if operator == "root" or operator == "sqr":
                print(f"\n{operator} {num1} = {result}")
            else:
                print(f"\n{num1} {operator} {num2} = {result}")

            finished = input("finish?[Y/n]")
            if finished == "Y" or finished == "y":
                break