import tkinter as tk
from tkinter import ttk

# Function to handle button clicks
def on_button_click(value):
    if value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Create the main window
root = tk.Tk()
root.title("Elegant Calculator")
root.geometry("400x600")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 18), padding=10)
style.configure("TEntry", font=("Arial", 24))

# Entry widget for display
entry = ttk.Entry(root, justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Add buttons to the grid
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        button = ttk.Button(root, text=btn_text, command=lambda value=btn_text: on_button_click(value))
        button.grid(row=i + 1, column=j, sticky="nsew", padx=5, pady=5)

# Adjust row and column weights for responsiveness
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Background color and button styling
root.configure(bg="#2E3440")
style.configure("TButton", background="#4C566A", foreground="white", borderwidth=1)
style.map("TButton",
          background=[("active", "#5E81AC")],
          foreground=[("active", "white")])

# Run the application
root.mainloop()