import tkinter as tk

def greet_user():
    user_name = entry.get()
    greeting = f"Hello, {user_name}!"
    label.config(text=greeting)

# Create the main application window
root = tk.Tk()
root.title("Greeting Program")

# Create a label for instructions
instruction_label = tk.Label(root, text="Enter your name and press the button:")
instruction_label.pack()

# Create an entry widget for user input
entry = tk.Entry(root)
entry.pack()

# Create a button for greeting the user
button = tk.Button(root, text="Greet Me", command=greet_user)
button.pack()

# Create a label for displaying the greeting
label = tk.Label(root, text="")
label.pack()

# Start the Tkinter main loop
root.mainloop()