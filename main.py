import tkinter as tk
from tkinter import messagebox

#  -------------------- CONSTANTS --------------------------- #
YELLOW = "#f7f5dd"








# ----------- UI SETUP --------------------- #
window = tk.Tk()
window.title("Bank Website")
window.geometry("800x500")
window.resizable(False, False)

canvas = tk.Canvas(width=800, height=500, bg = YELLOW, highlightthickness=0)


username_website = tk.Label(text="Username:")
password_website = tk.Label(text="Password:")








canvas.grid(column=1, row=1)
window.mainloop()