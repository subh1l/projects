# import customtkinter

from calculator import input_fnum, input_snum, input_op, add, operator, result

# main_window = customtkinter.CTk()
# main_window.geometry("360x450")
# # main_window.configure(bg="dark")
# main_window.title("Basic Calculator")



# main_window.mainloop()

input_fnum()
input_op()
input_snum()

if operator == "+":
    add(num1, num2)
print(result)