import tkinter as tk
from tkinter import messagebox

# Simulate a database of users
# In practice, use a real database and securely handle passwords
users = {
    "user1": "password1",
    "user2": "password2",
}

def attempt_login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Check if the username exists and the password matches
    if username in users and users[username] == password:
        messagebox.showinfo("Login Success", "Welcome to the Gym!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Set up the GUI
window = tk.Tk()
window.title("Gym Login Page")

# Username Field
label_username = tk.Label(window, text="Username:")
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

# Password Field
label_password = tk.Label(window, text="Password:")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Login Button
button_login = tk.Button(window, text="Login", command=attempt_login)
button_login.pack()

window.mainloop()