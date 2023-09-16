import tkinter as tk
from tkinter import messagebox

#  -------------------- CONSTANTS --------------------------- #
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"



# ----- NEW USER FUNCTIONS -------------------- #
def create_username():
    fgdf


def create_password():
    dfdf


def create_ID():
    dfdf

# ----------- UI SETUP --------------------- #
window = tk.Tk()
window.title("Bank Website")
window.geometry("800x500")
window.resizable(False, False)




canvas = tk.Canvas(width=800, height=500, bg = YELLOW, highlightthickness=0)


# Creatas the Labels
menu_title = tk.Label(text= "Sign in and Start Banking", font = (FONT_NAME, 30))
username_website = tk.Label(text="Username:")
password_website = tk.Label(text="Password:")


# Entrys
entry_username = tk.Entry(width = 21)
entry_password = tk.Entry(width = 21)

# Buttons
sign_up_btn = tk.Button(text="Sign Up", width=10)

# Places widgets to the window
menu_title.grid(row = 10, column = 0)

username_website.grid(row = 0, column = 0)
entry_username.grid(row = 0, column = 1)
password_website.grid(row = 1, column = 0)
entry_password.grid(row = 1, column = 1)

sign_up_btn.grid(row = 4, column = 4)


window.rowconfigure(10)
window.columnconfigure(10)
window.mainloop()
