import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

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
window = ttk.Window()
window.title("Bank Website")
window.geometry("2000x1500")
window.resizable(False, False)




canvas = ttk.Canvas(width=800, height=500, bg = YELLOW, highlightthickness=0)


# Creatas the Labels
menu_title = ttk.Label(text= "Sign in and Start Banking", font = (FONT_NAME, 15))
username_website = ttk.Label(text="Username:")
password_website = ttk.Label(text="Password:")


# Entrys
entry_username = ttk.Entry(width = 21)
entry_password = ttk.Entry(width = 21)

# Buttons
sign_up_btn = ttk.Button(text="Sign Up", width=10)

# Places widgets to the window

# menu_title.grid(row = 10, column = 0)

# username_website.grid(row = 0, column = 0)
# entry_username.grid(row = 0, column = 1)
# password_website.grid(row = 1, column = 0)
# entry_password.grid(row = 1, column = 1)

# sign_up_btn.grid(row = 4, column = 4)


# window.rowconfigure(10)
# window.columnconfigure(10)

menu_title.pack()
username_website.pack()




window.mainloop()
