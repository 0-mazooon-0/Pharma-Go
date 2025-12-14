import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.filedialog as fd
from PIL import Image, ImageTk
import fitz  # PyMuPDF
import json
import os


# Global variables to store account and cart information
personal_info = []
cart = []
medicines = {
    "Panadol": {"price": 10.0, "description": "Pain reliever for headaches and fever."},
    "Voltaren": {"price": 15.0, "description": "Anti-inflammatory for joint pain."},
    "Catafast": {"price": 12.0, "description": "Fast relief for dental pain."},
    "Congestal": {"price": 8.0, "description": "Relieves nasal congestion."},
    "Omega3": {"price": 20.0, "description": "Supplement for heart health."},
    "Aspirin": {"price": 5.0, "description": "Reduces fever and inflammation."},
    "Amoxicillin": {"price": 18.0, "description": "Antibiotic for bacterial infections."},
    "Ibuprofen": {"price": 22.0, "description": "Reduces pain and swelling."},
    "Paracetamol": {"price": 6.0, "description": "Relieves mild to moderate pain."},
    "Zyrtec": {"price": 25.0, "description": "Antihistamine for allergies."},
    "Metformin": {"price": 30.0, "description": "Oral medication for type 2 diabetes."},
    "Lipitor": {"price": 45.0, "description": "Statin used to lower cholesterol."},
    "Claritin": {"price": 20.0, "description": "Antihistamine for allergic reactions."},
    "Lisinopril": {"price": 12.0, "description": "Used to treat high blood pressure."},
    "Ciprofloxacin": {"price": 18.0, "description": "Antibiotic for bacterial infections."},
    "Advil": {"price": 8.0, "description": "Pain reliever and anti-inflammatory."},
    "Naproxen": {"price": 14.0, "description": "Pain reliever for arthritis and other conditions."},
    "Tadalafil": {"price": 35.0, "description": "Used to treat erectile dysfunction."},
    "Furosemide": {"price": 11.0, "description": "Diuretic for treating fluid retention."},
    "Amoxiclav": {"price": 19.0, "description": "Combination antibiotic for infections."},
    "Allegra": {"price": 23.0, "description": "Antihistamine for hay fever and allergies."},
    "Propranolol": {"price": 17.0, "description": "Beta-blocker used for high blood pressure and heart issues."},
    "Sildenafil": {"price": 40.0, "description": "Used to treat erectile dysfunction."},
    "Prednisone": {"price": 12.0, "description": "Steroid used to treat inflammation."},
    "Valium": {"price": 25.0, "description": "Medication for anxiety and muscle spasms."},
    "Omeprazole": {"price": 10.0, "description": "Proton pump inhibitor for acid reflux."},
    "Diazepam": {"price": 15.0, "description": "Used to relieve anxiety, muscle spasms, and seizures."},
    "Oxycodone": {"price": 40.0, "description": "Strong pain reliever for severe pain."},
    "Losartan": {"price": 20.0, "description": "Used to treat high blood pressure and heart failure."},
    "Ranitidine": {"price": 13.0, "description": "Used to treat stomach ulcers and acid reflux."},
    "Hydrochlorothiazide": {"price": 12.0, "description": "Diuretic for high blood pressure and edema."},
    "Diphenhydramine": {"price": 10.0, "description": "Antihistamine for allergies and sleep aid."},
    "Metoprolol": {"price": 14.0, "description": "Beta-blocker for heart disease and hypertension."},
    "Warfarin": {"price": 16.0, "description": "Anticoagulant to prevent blood clots."},
    "Gabapentin": {"price": 20.0, "description": "Used for nerve pain and seizures."},
    "Fluoxetine": {"price": 18.0, "description": "Antidepressant used for anxiety and depression."},
    "Cetirizine": {"price": 9.0, "description": "Antihistamine for hay fever and allergies."},
    "Bupropion": {"price": 22.0, "description": "Used for depression and smoking cessation."},
    "Amlodipine": {"price": 10.0, "description": "Used to treat high blood pressure and chest pain."},
    "Tramadol": {"price": 30.0, "description": "Pain reliever for moderate to severe pain."},
    "Citalopram": {"price": 15.0, "description": "Antidepressant used for anxiety and depression."},
    "Pregabalin": {"price": 28.0, "description": "Used for nerve pain and seizures."},
    "Clonazepam": {"price": 24.0, "description": "Used for anxiety, panic attacks, and seizures."},
    "Loratadine": {"price": 12.0, "description": "Antihistamine for hay fever and other allergies."},
    "Doxycycline": {"price": 18.0, "description": "Antibiotic for bacterial infections."},
    "Chloroquine": {"price": 26.0, "description": "Used to prevent and treat malaria."},
    "Tamsulosin": {"price": 11.0, "description": "Used for enlarged prostate treatment."},
    "Zolpidem": {"price": 23.0, "description": "Sedative-hypnotic used for insomnia."},
    "Benzonatate": {"price": 17.0, "description": "Cough suppressant used for dry cough."},
    "Spironolactone": {"price": 13.0, "description": "Used for heart failure, high blood pressure, and edema."}
}


def help():
    messagebox.showinfo("help!", "contact: 01008613609") # displaying a message box with the contact number

def button_placholder():
    print("Empty button")

# Classes
class Location:
    def __init__(self, city, streetname, buildingdetails):
        self.city = city
        self.streetname = streetname
        self.buildingdetails = buildingdetails


class PersonalInfo:
    def __init__(self, name, password, acc_number, phonenumber, location):
        self.name = name
        self.password = password
        self.acc_number = acc_number
        self.phonenumber = phonenumber
        self.location = location

def account_num_creation():  # function to create a new account number
    if personal_info: # check if there are any accounts in the list
        return personal_info[-1].acc_number + 1     #return the last account number + 1
    else:
        return 1 #return 1 if there are no accounts in the list

def log():
    def login():
        acc_number = int(entry_acc_number.get())
        password = entry_password.get()
        
        # dummy account just to check functionality
        dummy_account = PersonalInfo(name="Youssef",password='4444',acc_number= 1,phonenumber='01001234567',location='rehab')
        personal_info.append(dummy_account)
        account_num_creation()

        for account in personal_info:
            if account.acc_number == acc_number and account.password == password:
                messagebox.showinfo("Success", f"Welcome {account.name}!")
                log_window.withdraw()
                return
        
        messagebox.showerror("Error", "Invalid account number or password.")

    log_window = tk.Toplevel(root)
    log_window.title("Pharma go Login")
    log_window.configure(bg="#D5F5E3")
    log_window.geometry('1024x1024')

    tk.Label(log_window, text="Pharma go Login", font=("Arial", 16, "bold"), bg="#D5F5E3").pack(pady=10)

    tk.Label(log_window, text="Account Number (ID):", bg="#D5F5E3").pack(pady=5)
    entry_acc_number = tk.Entry(log_window)
    
    entry_acc_number.pack()

    tk.Label(log_window, text="Password:", bg="#D5F5E3").pack(pady=5)
    entry_password = tk.Entry(log_window, show="*")
    entry_password.pack()

    tk.Button(log_window, text="Login", command=login, bg="#1E8449", fg="white").pack(pady=10)

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
tk.Button(root, text="Existing Customer", command=log, bg="#2874A6", fg="white", font=("Arial", 20)).pack(pady=5)
tk.Button(root, text="Pharmacist Portal", command=button_placholder, bg="#D35400", fg="white", font=("Arial", 20)).pack(pady=5)
tk.Button(root, text="Help", command=help, bg="#A93226", fg="white", font=("Arial", 20)).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, bg="#2874A6", fg="white", font=("Arial", 16)).pack(pady=5)


root.mainloop()