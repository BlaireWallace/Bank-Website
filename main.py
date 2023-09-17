import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import info

#  -------------------- CONSTANTS --------------------------- #
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"



# ----- NEW USER FUNCTIONS -------------------- #

# Allow the user to create their own username
def create_username(event):
    
    username = userNameVar.get()

    # Check if username is certain length and contains certain characters
    if len(username) >= 10:
        if username[0].isupper() == True:
            if " " not in username:
                print("First charcter is uppercase, is long, has no spaces")
                return True
            else:
                messagebox.showinfo(title="Invalid Username", message="Username must be 10 characters long, first letter must be upper case, have no spaces")
                return False
        else:
            messagebox.showinfo(title="Invalid Username", message="Username must be 10 characters long, first letter must be upper case, have no spaces")
            return False
    else:
        messagebox.showinfo(title="Invalid Username", message="Username must be 10 characters long, first letter must be upper case, have no spaces")
        return False


# Allow the user to create their own password
def create_password(event):
    password = passwordVar.get()

    special_chars = [
    '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']',
    '\\', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '¥', '€', '£'
]
    letter_count = sum(1 for char in password if char.isalpha())

    if len(password) >= 12:
        if password[0].isupper() == True:
            if " " not in password:
                if any(char.isdigit() for char in password):
                    if (letter_count >= 10):
                        if any(char in special_chars for char in password):
                            print("All conditions met")
                            return True
                        else:
                            messagebox.showinfo(title="Invalid Password", message="Password must be 12 characters long, first letter must be upper case, have no spaces, contain 1 number, contain 1 special character")
                            return False
                    else:
                        messagebox.showinfo(title="Invalid Password", message="Password must be 12 characters long, first letter must be upper case, have no spaces, contain 1 number, contain 1 special character")
                        return False
                else:
                    messagebox.showinfo(title="Invalid Password", message="Password must be 12 characters long, first letter must be upper case, have no spaces, contain 1 number, contain 1 special character")
                    return False
            else:
                messagebox.showinfo(title="Invalid Password", message="Password must be 12 characters long, first letter must be upper case, have no spaces, contain 1 number, contain 1 special character")
                return False
        else:
            messagebox.showinfo(title="Invalid Password", message="Password must be 12 characters long, first letter must be upper case, have no spaces, contain 1 number, contain 1 special character")
            return False
    else:
        messagebox.showinfo(title="Invalid Password", message="Password must be 12 characters long, first letter must be upper case, have no spaces, contain 1 number, contain 1 special character")
        return False
                



# Will check if create user name and password functions return true and give them a unique ID (map to sign up button)
def check_credentials(event):
    if (create_username(event) == True and create_password(event) == True):
        print("Both Username and Password are valid!")
    else:
        print("Either your username or password was invalid")
    
    info.display()





# ----------- UI SETUP --------------------- #
window = ttk.Window()
window.title("Bank Website")
window.geometry("800x500")
window.resizable(False, False)




canvas = ttk.Canvas(width=800, height=500, bg = YELLOW, highlightthickness=0)


# Creatas the Labels
menu_title = ttk.Label(text= "Sign in and Start Banking", font = (FONT_NAME, 15))
username_website = ttk.Label(text="Username:")
password_website = ttk.Label(text="Password:")


# Entry
userNameVar = tk.StringVar()
passwordVar = tk.StringVar()

entry_username = ttk.Entry(width = 21,textvariable=userNameVar)
entry_username.bind("<Return>", create_username)



entry_password = ttk.Entry(width = 21, textvariable=passwordVar)
entry_password.bind("<Return>", create_password)

# Buttons
sign_up_btn = ttk.Button(text="Sign In", width=10)
sign_up_btn.bind("<Button-1>", check_credentials)  # Binds lefdt click button to the Sign Up button


menu_title.pack(expand=True)
username_website.pack(expand=True)
entry_username.pack(expand=True)
password_website.pack(expand=True)
entry_password.pack(expand=True)
sign_up_btn.pack(expand=True)




window.mainloop()
