from v1 import *

def account_num_creation():
    """Generate a new account number"""
    if personal_info:
        return personal_info[-1].acc_number + 1
    else:
        return 1

def create_account(name, phonenumber, password, city, streetname, buildingdetails):
    """Create a new customer account"""
    # Validate inputs
    if not all([name, phonenumber, password, city, streetname, buildingdetails]):
        return False, "All fields are required."
    
    # Validate password (4-digit number)
    if not password.isdigit() or len(password) != 4:
        return False, "Password must be a 4-digit number."
    
    # Create account
    acc_number = account_num_creation()
    location = Location(city, streetname, buildingdetails)
    account = PersonalInfo(name, password, acc_number, phonenumber, location)
    personal_info.append(account)
    
    # For this version, we'll store in memory only
    print(f"Account created: {name}, ID: {acc_number}")
    
    return True, f"Account created! Your Account ID: {acc_number}", account

def authenticate_customer(acc_number, password):
    """Authenticate a customer by account number and password"""
    try:
        acc_number = int(acc_number)
    except ValueError:
        return False, "Invalid account number format.", None
    
    for account in personal_info:
        if account.acc_number == acc_number and account.password == password:
            return True, f"Welcome {account.name}!", account
    
    return False, "Invalid account number or password.", None

def get_customer_info(acc_number):
    """Get customer information by account number"""
    try:
        acc_number = int(acc_number)
    except ValueError:
        return None
    
    for account in personal_info:
        if account.acc_number == acc_number:
            return account
    
    return None

def list_all_customers():
    """List all registered customers"""
    if not personal_info:
        return "No customers registered."
    
    result = "Registered Customers:\n"
    for customer in personal_info:
        result += f"ID: {customer.acc_number}, Name: {customer.name}, Phone: {customer.phonenumber}\n"
    
    return result

if __name__ == "__main__":
    # Test account management functions
    print("=== Testing Account Management ===\n")
    
    # Test creating accounts
    result1 = create_account("John Doe", "1234567890", "1234", "Cairo", "Main St", "Building 5")
    print(f"Create account 1: {result1[1]}")
    
    result2 = create_account("Jane Smith", "0987654321", "5678", "Alexandria", "Corniche", "Apt 12")
    print(f"Create account 2: {result2[1]}")
    
    # Test authentication
    auth_result = authenticate_customer("1", "1234")
    print(f"\nAuthenticate John: {'Success' if auth_result[0] else 'Failed'} - {auth_result[1]}")
    
    # Test listing customers
    print(f"\n{list_all_customers()}")
    
    print(f"\nTotal accounts: {len(personal_info)}")
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
