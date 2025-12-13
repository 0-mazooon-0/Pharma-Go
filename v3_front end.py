import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Import previous version classes
from v2 import NewAccountWindow

class CustomerLoginWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Customer Login - Version 3")
        self.window.configure(bg="#D5F5E3")
        self.window.geometry('600x400')
        
        self.setup_ui()
    
    def setup_ui(self):
        tk.Label(self.window, text="Customer Login", 
                font=("Arial", 24, "bold"), bg="#D5F5E3").pack(pady=30)
        
        # Login form
        form_frame = tk.Frame(self.window, bg="#D5F5E3")
        form_frame.pack(pady=30)
        
        tk.Label(form_frame, text="Account Number:", 
                bg="#D5F5E3", font=("Arial", 14)).grid(row=0, column=0, pady=10, padx=10, sticky="e")
        self.entry_acc_number = tk.Entry(form_frame, font=("Arial", 14), width=25)
        self.entry_acc_number.grid(row=0, column=1, pady=10, padx=10)
        
        tk.Label(form_frame, text="Password:", 
                bg="#D5F5E3", font=("Arial", 14)).grid(row=1, column=0, pady=10, padx=10, sticky="e")
        self.entry_password = tk.Entry(form_frame, show="*", font=("Arial", 14), width=25)
        self.entry_password.grid(row=1, column=1, pady=10, padx=10)
        
        # Buttons
        button_frame = tk.Frame(self.window, bg="#D5F5E3")
        button_frame.pack(pady=30)
        
        tk.Button(button_frame, text="Login", 
                 bg="#1E8449", fg="white", font=("Arial", 14),
                 command=self.login_ui).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Back", 
                 bg="red", fg="white", font=("Arial", 14),
                 command=self.window.destroy).pack(side=tk.LEFT, padx=10)
    
    def login_ui(self):
        print("Customer Login clicked - UI only")
        acc_number = self.entry_acc_number.get()
        password = self.entry_password.get()
        print(f"Login attempt - Account: {acc_number}")
        self.window.destroy()

class PharmacistLoginWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Pharmacist Login - Version 3")
        self.window.configure(bg="#D5F5E3")
        self.window.geometry('600x400')
        
        self.setup_ui()
    
    def setup_ui(self):
        tk.Label(self.window, text="Pharmacist Login", 
                font=("Arial", 24, "bold"), bg="#D5F5E3").pack(pady=30)
        
        form_frame = tk.Frame(self.window, bg="#D5F5E3")
        form_frame.pack(pady=30)
        
        tk.Label(form_frame, text="Username:", 
                bg="#D5F5E3", font=("Arial", 14)).grid(row=0, column=0, pady=10, padx=10, sticky="e")
        self.entry_username = tk.Entry(form_frame, font=("Arial", 14), width=25)
        self.entry_username.grid(row=0, column=1, pady=10, padx=10)
        
        tk.Label(form_frame, text="Password:", 
                bg="#D5F5E3", font=("Arial", 14)).grid(row=1, column=0, pady=10, padx=10, sticky="e")
        self.entry_password = tk.Entry(form_frame, show="*", font=("Arial", 14), width=25)
        self.entry_password.grid(row=1, column=1, pady=10, padx=10)
        
        button_frame = tk.Frame(self.window, bg="#D5F5E3")
        button_frame.pack(pady=30)
        
        tk.Button(button_frame, text="Login", 
                 bg="#1E8449", fg="white", font=("Arial", 14),
                 command=self.pharmacist_login_ui).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Back", 
                 bg="red", fg="white", font=("Arial", 14),
                 command=self.window.destroy).pack(side=tk.LEFT, padx=10)
    
    def pharmacist_login_ui(self):
        print("Pharmacist Login clicked - UI only")
        username = self.entry_username.get()
        password = self.entry_password.get()
        print(f"Pharmacist login - Username: {username}")
        self.window.destroy()

class HelpWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Help - Version 3")
        self.window.configure(bg="#D5F5E3")
        self.window.geometry('500x300')
        
        self.setup_ui()
    
    def setup_ui(self):
        tk.Label(self.window, text="Help & Support", 
                font=("Arial", 24, "bold"), bg="#D5F5E3").pack(pady=30)
        
        tk.Label(self.window, text="For assistance, please contact:", 
                font=("Arial", 14), bg="#D5F5E3").pack(pady=10)
        
        tk.Label(self.window, text="Phone: 01008613609", 
                font=("Arial", 16, "bold"), bg="#D5F5E3", fg="#1E8449").pack(pady=10)
        
        tk.Label(self.window, text="Email: support@pharmago.com", 
                font=("Arial", 14), bg="#D5F5E3").pack(pady=10)
        
        tk.Button(self.window, text="Close", 
                 bg="#2874A6", fg="white", font=("Arial", 14),
                 command=self.window.destroy).pack(pady=30)

class PharmaGoFrontendV3:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PharmaGo - Version 3")
        self.root.configure(bg="#D5F5E3")
        self.root.geometry('1024x1024')
        
    def setup_ui(self):
        # Background
        try:
            background_image = Image.open("111.jpg")
            background_image = background_image.resize((1024, 1024), Image.Resampling.LANCZOS)
            self.background_photo = ImageTk.PhotoImage(background_image)
            background_label = tk.Label(self.root, image=self.background_photo)
            background_label.place(relwidth=1, relheight=1)
        except:
            pass
        
        # Main interface
        tk.Label(self.root, text="Welcome to PharmaGo", 
                font=("Arial", 50, "bold"), bg="#D5F5E3", fg="#1E8449").pack(pady=100)
        
        tk.Button(self.root, text="New Customer", 
                 bg="#1E8449", fg="white", font=("Arial", 20), 
                 command=self.open_new_account).pack(pady=20)
        
        tk.Button(self.root, text="Existing Customer", 
                 bg="#2874A6", fg="white", font=("Arial", 20),
                 command=self.open_customer_login).pack(pady=20)
        
        tk.Button(self.root, text="Pharmacist Portal", 
                 bg="#D35400", fg="white", font=("Arial", 20),
                 command=self.open_pharmacist_login).pack(pady=20)
        
        tk.Button(self.root, text="Help", 
                 bg="#A93226", fg="white", font=("Arial", 20),
                 command=self.open_help).pack(pady=20)
        
        tk.Button(self.root, text="Exit", 
                 command=self.root.quit, bg="#2874A6", 
                 fg="white", font=("Arial", 16)).pack(pady=30)
    
    def open_new_account(self):
        NewAccountWindow(self.root)
    
    def open_customer_login(self):
        CustomerLoginWindow(self.root)
    
    def open_pharmacist_login(self):
        PharmacistLoginWindow(self.root)
    
    def open_help(self):
        HelpWindow(self.root)
    
    def run(self):
        self.setup_ui()
        self.root.mainloop()

if __name__ == "__main__":
    app = PharmaGoFrontendV3()
    app.run()