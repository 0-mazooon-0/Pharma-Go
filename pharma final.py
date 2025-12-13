import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.filedialog as fd
from PIL import Image, ImageTk
import fitz  # PyMuPDF
import json
import os


# Path to store the credentials JSON file
# saving the credentials in a json file to be able to use them later
pharmacist_credentials_file = "phramacist_credentials.json"
customer_credentials_file = "customer_credentials.json"

# Load the pharmacist credentials from the JSON file
def load_pharmacist_credentials():
    if os.path.exists(pharmacist_credentials_file): #check if the file exists
        with open(pharmacist_credentials_file, "r") as file: #open the file in read mode
            return json.load(file) #load the credentials from the file
    else:
        return {} #return an empty dictionary if the file does not exist

# Initialize or load the credentials into memory
pharmacist_credentials = load_pharmacist_credentials()

# Function to check the pharmacist login
def check_pharmacist_credentials(username, password): #function to check the pharmacist credentials
    if username in pharmacist_credentials and pharmacist_credentials[username] == password: #check if the username exists in the credentials and the password is correct
        print("Pharmacist verified successfully!")
        return True 
    else:
        print("Invalid credentials. Please try again.")
        return False

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


# Helper functions
def help():
    messagebox.showinfo("help!", "contact: 01008613609") # displaying a message box with the contact number

######## Funtions for customer sign up ########
def account_num_creation():  # function to create a new account number
    if personal_info: # check if there are any accounts in the list
        return personal_info[-1].acc_number + 1     #return the last account number + 1
    else:
        return 1 #return 1 if there are no accounts in the list

def new_account():
    root.withdraw() # To close the toplevel form
    def create_account():
        name = entry_name.get()
        phonenumber = entry_phonenumber.get()
        password = entry_password.get()
        city = entry_city.get()
        streetname = entry_streetname.get()
        buildingdetails = entry_buildingdetails.get()

        if not name or not phonenumber or not password or not city or not streetname or not buildingdetails:
            messagebox.showerror("Error", "All fields are required.")
            return

        if not password.isdigit() or len(password) != 4:
            messagebox.showerror("Error", "Password must be a 4-digit number.")
            return

        acc_number = account_num_creation()
        location = Location(city, streetname, buildingdetails)
        personal_info.append(PersonalInfo(name, password, acc_number, None, location))
        messagebox.showinfo("Success", f"Account created! Your Account ID: {acc_number}")
        new_account_window.destroy() 
        root.deiconify()

    new_account_window = tk.Toplevel(root)
    new_account_window.title("New Account")
    new_account_window.configure(bg="#D5F5E3")
    new_account_window.geometry('1024x1024')
    
    tk.Label(new_account_window, text="Create New Account", font=("Arial", 16, "bold"), bg="#D5F5E3").grid(row=0, columnspan=2, pady=10)
    
    tk.Label(new_account_window, text="Name:", bg="#D5F5E3").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_name = tk.Entry(new_account_window)
    entry_name.grid(row=1, column=1)

    tk.Label(new_account_window, text="phone number:", bg="#D5F5E3").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_phonenumber = tk.Entry(new_account_window)
    entry_phonenumber.grid(row=2, column=1)

    tk.Label(new_account_window, text="Password (4-digit):", bg="#D5F5E3").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_password = tk.Entry(new_account_window, show="*")
    entry_password.grid(row=3, column=1)

    tk.Label(new_account_window, text="City:", bg="#D5F5E3").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_city = tk.Entry(new_account_window)
    entry_city.grid(row=4, column=1)

    tk.Label(new_account_window, text="Street Name:", bg="#D5F5E3").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    entry_streetname = tk.Entry(new_account_window)
    entry_streetname.grid(row=5, column=1)

    tk.Label(new_account_window, text="Building Details:", bg="#D5F5E3").grid(row=6, column=0, padx=10, pady=5, sticky="e")
    entry_buildingdetails = tk.Entry(new_account_window)
    entry_buildingdetails.grid(row=6, column=1)

    tk.Button(new_account_window,text="Back",bg="red", fg="white",command=lambda:[new_account_window.destroy(),root.deiconify()]).grid(row=7, columnspan=2, pady=10)
    tk.Button(new_account_window, text="Create Account", command=create_account, bg="#1E8449", fg="white").grid(row=8, columnspan=2, pady=10)

########  ########  ########  ########  ########

######## Pharmacist Portal ########
def pharmacist_portal():

    root.withdraw()

    def add_medicine():
        name = entry_medicine_name.get()
        price = entry_medicine_price.get()
        description = entry_medicine_description.get()

        if not name or not price or not description:
            messagebox.showerror("Error", "All fields are required.")
            return
        if not price.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "Price must be a valid number.")
            return

        if name in medicines:
            messagebox.showerror("Error", f"{name} already exists in the inventory.")
        else:
            medicines[name] = {"price": float(price), "description": description}
            messagebox.showinfo("Success", f"{name} added successfully!")
            update_medicine_list()

    def remove_medicine():
        selected = medicine_listbox.curselection()
        if selected:
            medicine = medicine_listbox.get(selected[0])
            del medicines[medicine]
            messagebox.showinfo("Success", f"{medicine} removed successfully!")
            update_medicine_list()
        else:
            messagebox.showerror("Error", "Please select a medicine to remove.")

    def update_price():
        selected = medicine_listbox.curselection()
        new_price = entry_new_price.get()

        if not selected:
            messagebox.showerror("Error", "Please select a medicine to update.")
            return
        if not new_price.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "New price must be a valid number.")
            return

        medicine = medicine_listbox.get(selected[0])
        medicines[medicine]["price"] = float(new_price)
        messagebox.showinfo("Success", f"Price for {medicine} updated successfully!")
        update_medicine_list()

    def update_medicine_list():
        medicine_listbox.delete(0, tk.END)
        for med in medicines:
            medicine_listbox.insert(tk.END, med)
      
    # Create the pharmacist window
    pharmacist_window = tk.Toplevel(root)
    pharmacist_window.title("Pharmacist Portal")
    pharmacist_window.configure(bg="#D5F5E3")
    pharmacist_window.geometry('1024x1024')

    tk.Label(pharmacist_window, text="Pharmacist Portal", font=("Arial", 16, "bold"), bg="#D5F5E3").pack(pady=10)

    # Add Medicine Section
    tk.Label(pharmacist_window, text="Add New Medicine", font=("Arial", 12, "bold"), bg="#D5F5E3").pack(pady=5)
    tk.Label(pharmacist_window, text="Name:", bg="#D5F5E3").pack()
    entry_medicine_name = tk.Entry(pharmacist_window)
    entry_medicine_name.pack()

    tk.Label(pharmacist_window, text="Price:", bg="#D5F5E3").pack()
    entry_medicine_price = tk.Entry(pharmacist_window)
    entry_medicine_price.pack()

    tk.Label(pharmacist_window, text="Description:", bg="#D5F5E3").pack()
    entry_medicine_description = tk.Entry(pharmacist_window)
    entry_medicine_description.pack()

    tk.Button(pharmacist_window, text="Add Medicine", command=add_medicine, bg="#1E8449", fg="white").pack(pady=5)

    # Remove Medicine Section
    tk.Label(pharmacist_window, text="Remove Medicine", font=("Arial", 12, "bold"), bg="#D5F5E3").pack(pady=10)
    medicine_listbox = tk.Listbox(pharmacist_window, height=10, width=30)
    medicine_listbox.pack()
    update_medicine_list()

    tk.Button(pharmacist_window, text="Remove Selected Medicine", command=remove_medicine, bg="#A93226", fg="white").pack(pady=5)

    # Update Price Section
    tk.Label(pharmacist_window, text="Update Medicine Price", font=("Arial", 12, "bold"), bg="#D5F5E3").pack(pady=10)
    tk.Label(pharmacist_window, text="New Price:", bg="#D5F5E3").pack()
    entry_new_price = tk.Entry(pharmacist_window)
    entry_new_price.pack()

    tk.Button(pharmacist_window, text="Update Price", command=update_price, bg="#3498DB", fg="white").pack(pady=5)

    # Exit Button
    tk.Button(pharmacist_window, text="Back", command= lambda:[pharmacist_window.destroy(),root.deiconify()], bg="#2874A6", fg="white").pack(pady=10)

######## ######## ######## ########


######## Function to handle pharmacist login ########
def pharmacist_login():
    def verify_login():
        username = entry_username.get()
        password = entry_password.get()

        # Check the credentials
        if check_pharmacist_credentials(username, password):
            messagebox.showinfo("Success", "Pharmacist verified successfully!")
            pharmacist_portal()
            # Proceed with other actions for the pharmacist (e.g., adding/removing medicines)
        else:
            messagebox.showerror("Error", "Invalid credentials. Please try again.")
           

    # Create login window
    pharmacist_window = tk.Toplevel(root)
    pharmacist_window.title("Pharmacist Login")
    pharmacist_window.configure(bg="#D5F5E3")
    pharmacist_window.geometry('1024x1024')

    tk.Label(pharmacist_window, text="Pharmacist Login", font=("Arial", 16, "bold"), bg="#D5F5E3").pack(pady=10)

    tk.Label(pharmacist_window, text="Username:", bg="#D5F5E3").pack(pady=5)
    entry_username = tk.Entry(pharmacist_window)
    entry_username.pack(pady=5)

    tk.Label(pharmacist_window, text="Password:", bg="#D5F5E3").pack(pady=5)
    entry_password = tk.Entry(pharmacist_window, show="*")
    entry_password.pack(pady=5)

    tk.Button(pharmacist_window, text="Login", command=lambda:[verify_login(),pharmacist_window.withdraw()], bg="#1E8449", fg="white").pack(pady=10)
    tk.Button(pharmacist_window,text="Back",bg="red", fg="white",command=lambda:[pharmacist_window.destroy(),root.deiconify()]).pack(pady=10)

######## ######## ######## ########

######## Funtions for customer login in ########
def log():
    def login():
        acc_number = int(entry_acc_number.get())
        password = entry_password.get()
       

        for account in personal_info:
            if account.acc_number == acc_number and account.password == password:
                messagebox.showinfo("Success", f"Welcome {account.name}!")
                root.withdraw()  # Hide the main window
                log_window.withdraw()
                perform_transaction(account)
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
    tk.Button(log_window,text="Back",bg="red", fg="white",command=lambda: [log_window.destroy(),root.deiconify()]).pack(pady=10)
   
########  ########  ########  ########  ########

######## Customer Portal ########
def perform_transaction(account):
    def update_cart():
        cart_listbox.delete(0, tk.END)
        total_price = 0
        for item, price in cart:
            cart_listbox.insert(tk.END, f"{item} - ${price['price']:.2f}")
            total_price += price['price']
        total_price_label.config(text=f"Total: ${total_price:.2f}")

    def search_medicine():
        medicine = medicine_dropdown.get()

        if medicine in medicines:
            cart.append((medicine, medicines[medicine]))
            update_cart()
        else:
            messagebox.showerror("Medicine Not Found", f"{medicine} is not available.")
            
    def view_description():
        medicine = medicine_dropdown.get()
        if medicine in medicines:
            description = medicines[medicine]["description"]
            messagebox.showinfo("Description", f"{medicine}: {description}")
        else:
            messagebox.showerror("Error", "Select a valid medicine.")

    def remove_item():
        selected = cart_listbox.curselection()
        if selected:
            cart.pop(selected[0])
            update_cart()
        else:
            messagebox.showwarning("Warning", "Please select an item to remove.")


    def pay():
        if not cart:
            messagebox.showinfo("Cart", "Your cart is empty.")
        else:
            total_price = sum(price['price'] for _, price in cart)
            messagebox.showinfo("Payment", f"Payment completed. Total: ${total_price:.2f}")
            cart.clear()
            update_cart()
            
    def import_and_display_pdf():
    # Open file dialog to select a PDF file
        filepath = fd.askopenfilename(filetypes=[("PDF files", "*.pdf")])

        if filepath:
            try:
                # Open the PDF file using PyMuPDF
                pdf_document = fitz.open(filepath)

                # Create a new window to display the PDF
                pdf_window = tk.Toplevel(root)
                pdf_window.title(f"Viewing: {filepath.split('/')[-1]}")
                pdf_window.configure(bg="#D5F5E3")

                tk.Label(pdf_window, text=f"Viewing: {filepath.split('/')[-1]}", font=("Arial", 12, "bold"), bg="#D5F5E3").pack(pady=5)

                # Canvas to display the PDF pages
                canvas = tk.Canvas(pdf_window, width=800, height=1000, bg="white")
                canvas.pack(pady=10, padx=10)

                # Scrollbar
                scrollbar = tk.Scrollbar(pdf_window, orient="vertical", command=canvas.yview)
                scrollbar.pack(side="right", fill="y")
                canvas.configure(yscrollcommand=scrollbar.set)

                # Render the current page of the PDF
                page_index = [0]  # Track current page as a list (mutable)

                def render_page(index):
                    page = pdf_document[index]
                    pixmap = page.get_pixmap()
                    image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

                    # Resize the image to fit the canvas
                    image.thumbnail((800, 1000), Image.Resampling.LANCZOS)  # Use Resampling.LANCZOS instead of ANTIALIAS
                    tk_image = ImageTk.PhotoImage(image)

                    # Clear canvas and display new page
                    canvas.delete("all")
                    canvas.create_image(0, 0, anchor="nw", image=tk_image)
                    canvas.image = tk_image  # Keep a reference to the image object
                    pdf_window.geometry(f"{image.width+20}x{image.height+50}")  # Add padding for the window's borders and controls

                    # Update window title with page number
                    pdf_window.title(f"Viewing: {filepath.split('/')[-1]} (Page {index + 1}/{len(pdf_document)})")

                # Navigation buttons
                def on_mouse_wheel(event):
                    if event.delta > 0:  # Previous page
                        prev_page()
                    elif event.delta < 0:  # Next page
                        next_page()

                pdf_window.bind("<MouseWheel>", on_mouse_wheel)
                def next_page():
                    if page_index[0] < len(pdf_document) - 1:
                        page_index[0] += 1
                        render_page(page_index[0])

                def prev_page():
                     if page_index[0] > 0:
                        page_index[0] -= 1
                        render_page(page_index[0])

                # Initially render the first page
                render_page(page_index[0])

                # Navigation controls
                control_frame = tk.Frame(pdf_window, bg="#D5F5E3")
                control_frame.pack(pady=10)

                

            except Exception as e:
                messagebox.showerror("Error", f"Failed to load PDF: {str(e)}")




    transaction_window = tk.Toplevel(root)
    transaction_window.title("Transaction")
    transaction_window.configure(bg="#D5F5E3")
    transaction_window.geometry('1024x1024')

    tk.Label(transaction_window, text=f"Welcome, {account.name}!", font=("Arial", 16, "bold"), bg="#D5F5E3").pack(pady=10)

    tk.Label(transaction_window, text="Select Medicine:", bg="#D5F5E3").pack(pady=5)
    medicine_dropdown = ttk.Combobox(transaction_window, values=list(medicines.keys()), state="readonly")
    medicine_dropdown.pack()

    tk.Button(transaction_window, text="Add to Cart", command=search_medicine, bg="#1E8449", fg="white").pack(pady=5)

    tk.Label(transaction_window, text="Cart:", bg="#D5F5E3").pack(pady=5)
    cart_listbox = tk.Listbox(transaction_window, height=10, width=30)
    cart_listbox.pack()

    total_price_label = tk.Label(transaction_window, text="Total: $0.00", bg="#D5F5E3", font=("Arial", 12))
    total_price_label.pack()
    tk.Button(transaction_window, text="View Description", command=view_description, bg="#3498DB", fg="white").pack(pady=5)
    tk.Button(transaction_window, text="Remove Item", command=remove_item, bg="#A93226", fg="white").pack(pady=5)
    tk.Button(transaction_window, text="Pay", command=pay, bg="#1E8449", fg="white").pack(pady=5)
    tk.Button(transaction_window, text="Import and View PDF", command=import_and_display_pdf, bg="#D35400", fg="white", font=("Arial", 12)).pack(pady=5)
    tk.Button(transaction_window, text="Exit", command=lambda: [transaction_window.destroy(),root.deiconify()], bg="#2874A6", fg="white").pack(pady=5)
    
######## ######## ######## ########

# Main GUI
root = tk.Tk()
root.title("PharmaGo")
root.configure(bg="#D5F5E3")
root.geometry('1024x1024')

tk.Label(root, text="Welcome to PharmaGo", font=("Arial", 50, "bold"), bg="#D5F5E3", fg="#1E8449").pack(pady=10)
tk.Button(root, text="New Customer", command=new_account, bg="#1E8449", fg="white", font=("Arial", 20)).pack(pady=5)
tk.Button(root, text="Existing Customer", command=log, bg="#2874A6", fg="white", font=("Arial", 20)).pack(pady=5)
tk.Button(root, text="Pharmacist Portal", command=pharmacist_login, bg="#D35400", fg="white", font=("Arial", 20)).pack(pady=5)
tk.Button(root, text="Help", command=help, bg="#A93226", fg="white", font=("Arial", 20)).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, bg="#2874A6", fg="white", font=("Arial", 16)).pack(pady=5)



root.mainloop()



