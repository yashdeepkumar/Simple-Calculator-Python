from tkinter import *
 
root = Tk()
root.title("Calculator")

# Creating the functions for the buttons
def common_action(number):
	current_number = output_display_box.get()
	output_display_box.delete(0, END)
	output_display_box.insert(0, str(current_number) + str(number))

def add_action():
	first_number = output_display_box.get()
	global f_num, math
	math = "Addition" 
	f_num = int(first_number)
	output_display_box.delete(0, END)

def sub_action():
	first_number = output_display_box.get()
	global f_num, math
	math = "Subtraction" 
	f_num = int(first_number)
	output_display_box.delete(0, END)

def mul_action():
	first_number = output_display_box.get()
	global f_num, math
	math = "Multiplication" 
	f_num = int(first_number)
	output_display_box.delete(0, END)

def div_action():
	first_number = output_display_box.get()
	global f_num, math
	math = "Division" 
	f_num = int(first_number)
	output_display_box.delete(0, END)

def equal_to_action():
	second_number = output_display_box.get()
	output_display_box.delete(0, END)
	if math == "Addition":
		output_display_box.insert(0,  f_num + int(second_number))
	if math == "Subtraction":
		output_display_box.insert(0,  f_num - int(second_number))
	if math == "Division":
		output_display_box.insert(0,  f_num / int(second_number))
	if math == "Multiplication":
		output_display_box.insert(0,  f_num * int(second_number))


def clear_action():
	output_display_box.delete(0, END)

# First creating the widgets
output_display_box = Entry(root, width=35, borderwidth=5)

button_for_number_1 = Button(root, text="1", padx=40, pady=20, command=lambda: common_action(1))
button_for_number_2 = Button(root, text="2", padx=40, pady=20, command=lambda: common_action(2))
button_for_number_3 = Button(root, text="3", padx=40, pady=20, command=lambda: common_action(3))
button_for_number_4 = Button(root, text="4", padx=40, pady=20, command=lambda: common_action(4))
button_for_number_5 = Button(root, text="5", padx=40, pady=20, command=lambda: common_action(5))
button_for_number_6 = Button(root, text="6", padx=40, pady=20, command=lambda: common_action(6))
button_for_number_7 = Button(root, text="7", padx=40, pady=20, command=lambda: common_action(7))
button_for_number_8 = Button(root, text="8", padx=40, pady=20, command=lambda: common_action(8))
button_for_number_9 = Button(root, text="9", padx=40, pady=20, command=lambda: common_action(9))
button_for_number_0 = Button(root, text="0", padx=40, pady=20, command=lambda: common_action(0))

button_for_clear = Button(root, text="Clear", padx=79, pady=20, command=clear_action)
button_for_addition = Button(root, text="+", padx=39, pady=20, command=add_action)
button_for_subtraction = Button(root, text="-", padx=41, pady=20, command=sub_action)
button_for_multiplication = Button(root, text="*", padx=40, pady=20, command=mul_action)
button_for_division = Button(root, text="/", padx=41, pady=20, command=div_action)
button_for_result = Button(root, text="=", padx=91, pady=20, command=equal_to_action)

# Second placing them in the correct position
output_display_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_for_number_1.grid(row=3, column=0)
button_for_number_2.grid(row=3, column=1)
button_for_number_3.grid(row=3, column=2)

button_for_number_4.grid(row=2, column=0)
button_for_number_5.grid(row=2, column=1)
button_for_number_6.grid(row=2, column=2)

button_for_number_7.grid(row=1, column=0)
button_for_number_8.grid(row=1, column=1)
button_for_number_9.grid(row=1, column=2)

button_for_number_0.grid(row=4, column=0)
button_for_clear.grid(row=4, column=1, columnspan=2)

button_for_result.grid(row=5, column=1, columnspan=2)
button_for_addition.grid(row=5, column=0)

button_for_subtraction.grid(row=6, column=0)
button_for_division.grid(row=6, column=2)
button_for_multiplication.grid(row=6, column=1)

root.mainloop()