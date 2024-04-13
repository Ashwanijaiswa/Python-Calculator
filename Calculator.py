import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Error! Division by zero"
            else:
                result = num1 / num2

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input")
        

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry fields
entry1 = tk.Entry(root)
entry1.grid(row=0, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=1)

# Create operation dropdown
operation_var = tk.StringVar(root)
operation_choices = ['+', '-', '*', '/']
operation_dropdown = tk.OptionMenu(root, operation_var, *operation_choices)
operation_dropdown.grid(row=0, column=2)
operation_var.set('+')

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, columnspan=3)

# Create result label
result_label = tk.Label(root, text="")
result_label.grid(row=2, columnspan=3)

# Run the main event loop
root.mainloop()
