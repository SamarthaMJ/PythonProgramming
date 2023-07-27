import tkinter as tk


def on_button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


def on_clear():
    entry.delete(0, tk.END)


def on_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for displaying the input and output
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create the calculator buttons
for button_text, row, col in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=10, command=lambda text=button_text: on_button_click(text))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text='C', padx=20, pady=10, command=on_clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Equal button
equal_button = tk.Button(root, text='=', padx=20, pady=10, command=on_equal)
equal_button.grid(row=5, column=2, columnspan=2)

# Start the GUI main loop
root.mainloop()
