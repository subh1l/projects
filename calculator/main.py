import os
import math

if __name__ == '__main__':
    operating_sys = os.name
    while(True):
        match operating_sys:
            case 'posix': os.system('clear')
            case 'nt': os.system('cls')

        print(25*"=")
        print("Basic calculator".center(25))
        print(25*"=")

        num1 = input("first number/ans: ")
        operator = input('operator[+,-,*,/,root,sqr,pow]: ')
        if operator == 'root' or operator == 'sqr':
            pass
        else:
            num2 = int(input("second number: "))

        if num1 == 'ans':
            num1 = result
        else:
            num1 = int(num1)

        match operator:
            case '+': result = num1 + num2
            case '-': result = num1 - num2
            case '*': result = num1*num2
            case '/': result = num1 / num2
            case 'root': result = math.sqrt(num1)
            case 'sqr': result = num1*num1
            case 'pow': result = num1**num2

        if operator == 'root' or operator == 'sqr':
            print(f'\n{operator} {num1} = {result}')
        else:
            print(f'\n{num1} {operator} {num2} = {result}')

        finished = input('finish?[Y/n]')
        if finished == 'Y' or finished == 'y':
            break