import tkinter as tk

# Function to perform calculations
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = entry_operation.get()

    if operation == '+':
        result.set(num1 + num2)
    elif operation == '-':
        result.set(num1 - num2)
    elif operation == '*':
        result.set(num1 * num2)
    elif operation == '/':
        if num2 == 0:
            result.set("Division by zero is not allowed.")
        else:
            result.set(num1 / num2)
    else:
        result.set("Invalid operation")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create input fields
entry_num1 = tk.Entry(window)
entry_num1.pack()
entry_operation = tk.Entry(window)
entry_operation.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create a result label
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.pack()

# Create a Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Start the GUI event loop
window.mainloop()
