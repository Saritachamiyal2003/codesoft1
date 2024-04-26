import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(show="")

def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Length label and entry
length_label = tk.Label(root, text="Length:")
length_label.grid(row=1, column=0, padx=10, pady=10)

length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, padx=10, pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Password entry
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()