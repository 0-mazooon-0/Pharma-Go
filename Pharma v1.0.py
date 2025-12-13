import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.filedialog as fd
from PIL import Image, ImageTk
import fitz  # PyMuPDF
import json
import os

# Helper functions
def help():
    messagebox.showinfo("help!", "contact: 01008613609") # displaying a message box with the contact number

def button_placholder():
    print("Empty button")

# Main GUI
root = tk.Tk()
root.title("PharmaGo")
root.configure(bg="#D5F5E3")
# Load and set the background image
background_image = Image.open("111.jpg")
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.Resampling.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
root.geometry('1024x1024')

background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)
tk.Label(root, text="Welcome to PharmaGo", font=("Arial", 50, "bold"), bg="#D5F5E3", fg="#1E8449").pack(pady=10)
tk.Button(root, text="New Customer", command=button_placholder, bg="#1E8449", fg="white", font=("Arial", 20)).pack(pady=5)
tk.Button(root, text="Existing Customer", command=button_placholder, bg="#2874A6", fg="white", font=("Arial", 20)).pack(pady=5)
tk.Button(root, text="Pharmacist Portal", command=button_placholder, bg="#D35400", fg="white", font=("Arial", 20)).pack(pady=5)
tk.Button(root, text="Help", command=help, bg="#A93226", fg="white", font=("Arial", 20)).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, bg="#2874A6", fg="white", font=("Arial", 16)).pack(pady=5)


root.mainloop()