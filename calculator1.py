import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Clear the input fields and result
def clear_all():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Setting up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Styling the window
root.geometry("400x400")
root.configure(bg="#282C34")

# Creating input fields for the two numbers
label_num1 = tk.Label(root, text="Enter first number:", font=("Arial", 14), bg="#e6faff", fg="#003d4d")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root, font=("Arial", 14), width=10)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:", font=("Arial", 14), bg="#e6faff", fg="#003d4d")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, font=("Arial", 14), width=10)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Dropdown menu for operation choices
operation_var = tk.StringVar()
operation_var.set('+')  # default value

operation_label = tk.Label(root, text="Select operation:", font=("Arial", 14), bg="#e6faff", fg="#003d4d")
operation_label.grid(row=2, column=0, padx=10, pady=10)

operation_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operation_menu.config(font=("Arial", 14), bg="#98C379", fg="white", width=5)
operation_menu.grid(row=2, column=1, padx=10, pady=10)

# Button to perform calculation
calc_button = tk.Button(root, text="Calculate", command=calculate, font=("Arial", 14), bg="#e6faff", fg="#003d4d", width=10)
calc_button.grid( row=3, column=0, columnspan=2, padx=10, pady=10)

# Button to clear all inputs
clear_button = tk.Button(root, text="Clear", command=clear_all, font=("Arial", 14), bg="#e6faff", fg="#003d4d", width=10)
clear_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result: ", font=("Arial", 16), bg="#e6faff", fg="#003d4d")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

# Start the Tkinter event loop
root.mainloop()

