import tkinter as tk
from PIL import Image, ImageTk

class NewAccountWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("New Account - Version 2")
        self.window.configure(bg="#D5F5E3")
        self.window.geometry('800x600')
        
        self.setup_ui()
    
    def setup_ui(self):
        tk.Label(self.window, text="Create New Account", 
                font=("Arial", 20, "bold"), bg="#D5F5E3").pack(pady=20)
        
        # Form fields
        form_frame = tk.Frame(self.window, bg="#D5F5E3")
        form_frame.pack(pady=20)
        
        # Labels and entries
        fields = [
            ("Name:", "entry_name"),
            ("Phone Number:", "entry_phone"),
            ("Password (4-digit):", "entry_password", True),
            ("City:", "entry_city"),
            ("Street Name:", "entry_street"),
            ("Building Details:", "entry_building")
        ]
        
        for i, field in enumerate(fields):
            label_text = field[0]
            var_name = field[1]
            is_password = len(field) > 2 and field[2]
            
            tk.Label(form_frame, text=label_text, bg="#D5F5E3", 
                    font=("Arial", 12)).grid(row=i, column=0, sticky="e", padx=10, pady=5)
            
            entry = tk.Entry(form_frame, show="*" if is_password else None, 
                           font=("Arial", 12), width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, var_name, entry)
        
        # Buttons
        button_frame = tk.Frame(self.window, bg="#D5F5E3")
        button_frame.pack(pady=30)
        
        tk.Button(button_frame, text="Create Account", 
                 bg="#1E8449", fg="white", font=("Arial", 14),
                 command=self.create_account_ui).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Back", 
                 bg="red", fg="white", font=("Arial", 14),
                 command=self.window.destroy).pack(side=tk.LEFT, padx=10)
    
    def create_account_ui(self):
        print("Create Account clicked - UI only")
        # Get values from UI
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        password = self.entry_password.get()
        city = self.entry_city.get()
        street = self.entry_street.get()
        building = self.entry_building.get()
        
        print(f"Form data - Name: {name}, Phone: {phone}, City: {city}")
        self.window.destroy()

class PharmaGoFrontendV2:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PharmaGo - Version 2")
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
                 command=self.existing_customer_placeholder).pack(pady=20)
        
        tk.Button(self.root, text="Pharmacist Portal", 
                 bg="#D35400", fg="white", font=("Arial", 20),
                 command=self.pharmacist_placeholder).pack(pady=20)
        
        tk.Button(self.root, text="Help", 
                 bg="#A93226", fg="white", font=("Arial", 20),
                 command=self.help_placeholder).pack(pady=20)
        
        tk.Button(self.root, text="Exit", 
                 command=self.root.quit, bg="#2874A6", 
                 fg="white", font=("Arial", 16)).pack(pady=30)
    
    def open_new_account(self):
        NewAccountWindow(self.root)
    
    def existing_customer_placeholder(self):
        print("Existing Customer clicked - UI only")
    
    def pharmacist_placeholder(self):
        print("Pharmacist clicked - UI only")
    
    def help_placeholder(self):
        print("Help clicked - UI only")
    
    def run(self):
        self.setup_ui()
        self.root.mainloop()

if __name__ == "__main__":
    app = PharmaGoFrontendV2()
    app.run()