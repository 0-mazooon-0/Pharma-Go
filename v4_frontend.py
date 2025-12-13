import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Import previous versions
from Front.v3_frontend import NewAccountWindow, CustomerLoginWindow, PharmacistLoginWindow, HelpWindow

class PharmacistPortalWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Pharmacist Portal - Version 4")
        self.window.configure(bg="#D5F5E3")
        self.window.geometry('900x700')
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        tk.Label(self.window, text="Pharmacist Portal", 
                font=("Arial", 24, "bold"), bg="#D5F5E3").pack(pady=20)
        
        # Notebook for tabs
        notebook = ttk.Notebook(self.window)
        notebook.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Tab 1: Add Medicine
        add_frame = tk.Frame(notebook, bg="#D5F5E3")
        notebook.add(add_frame, text="Add Medicine")
        self.setup_add_tab(add_frame)
        
        # Tab 2: View/Remove Medicine
        view_frame = tk.Frame(notebook, bg="#D5F5E3")
        notebook.add(view_frame, text="View/Remove")
        self.setup_view_tab(view_frame)
        
        # Tab 3: Update Price
        update_frame = tk.Frame(notebook, bg="#D5F5E3")
        notebook.add(update_frame, text="Update Price")
        self.setup_update_tab(update_frame)
        
        # Exit button
        tk.Button(self.window, text="Exit Portal", 
                 bg="#2874A6", fg="white", font=("Arial", 14),
                 command=self.window.destroy).pack(pady=20)
    
    def setup_add_tab(self, parent):
        tk.Label(parent, text="Add New Medicine", 
                font=("Arial", 16, "bold"), bg="#D5F5E3").pack(pady=10)
        
        form_frame = tk.Frame(parent, bg="#D5F5E3")
        form_frame.pack(pady=20)
        
        fields = [
            ("Medicine Name:", "entry_name"),
            ("Price ($):", "entry_price"),
            ("Description:", "entry_desc")
        ]
        
        for i, (label, var_name) in enumerate(fields):
            tk.Label(form_frame, text=label, bg="#D5F5E3", 
                    font=("Arial", 12)).grid(row=i, column=0, sticky="e", padx=10, pady=10)
            
            if "desc" in var_name:
                entry = tk.Text(form_frame, height=4, width=40, font=("Arial", 12))
            else:
                entry = tk.Entry(form_frame, font=("Arial", 12), width=40)
            
            entry.grid(row=i, column=1, padx=10, pady=10)
            setattr(self, var_name, entry)
        
        tk.Button(parent, text="Add Medicine", 
                 bg="#1E8449", fg="white", font=("Arial", 14),
                 command=self.add_medicine_ui).pack(pady=20)
    
    def setup_view_tab(self, parent):
        tk.Label(parent, text="Medicine Inventory", 
                font=("Arial", 16, "bold"), bg="#D5F5E3").pack(pady=10)
        
        # Listbox with scrollbar
        list_frame = tk.Frame(parent, bg="#D5F5E3")
        list_frame.pack(pady=10)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.medicine_listbox = tk.Listbox(list_frame, 
                                          height=15, 
                                          width=50, 
                                          font=("Arial", 12),
                                          yscrollcommand=scrollbar.set)
        self.medicine_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=self.medicine_listbox.yview)
        
        # Populate with sample data
        sample_medicines = ["Panadol - $10.0", "Voltaren - $15.0", "Catafast - $12.0"]
        for med in sample_medicines:
            self.medicine_listbox.insert(tk.END, med)
        
        # Buttons
        button_frame = tk.Frame(parent, bg="#D5F5E3")
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Remove Selected", 
                 bg="#A93226", fg="white", font=("Arial", 14),
                 command=self.remove_medicine_ui).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Refresh List", 
                 bg="#3498DB", fg="white", font=("Arial", 14),
                 command=self.refresh_list_ui).pack(side=tk.LEFT, padx=10)
    
    def setup_update_tab(self, parent):
        tk.Label(parent, text="Update Medicine Price", 
                font=("Arial", 16, "bold"), bg="#D5F5E3").pack(pady=10)
        
        form_frame = tk.Frame(parent, bg="#D5F5E3")
        form_frame.pack(pady=20)
        
        tk.Label(form_frame, text="Select Medicine:", 
                bg="#D5F5E3", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        
        self.medicine_combo = ttk.Combobox(form_frame, 
                                          values=["Panadol", "Voltaren", "Catafast"],
                                          font=("Arial", 12), 
                                          width=30)
        self.medicine_combo.grid(row=0, column=1, padx=10, pady=10)
        self.medicine_combo.set("Select medicine")
        
        tk.Label(form_frame, text="New Price ($):", 
                bg="#D5F5E3", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        self.entry_new_price = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.entry_new_price.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Button(parent, text="Update Price", 
                 bg="#3498DB", fg="white", font=("Arial", 14),
                 command=self.update_price_ui).pack(pady=20)
    
    def add_medicine_ui(self):
        print("Add Medicine clicked - UI only")
        name = self.entry_name.get() if hasattr(self.entry_name, 'get') else "N/A"
        price = self.entry_price.get() if hasattr(self.entry_price, 'get') else "N/A"
        desc = self.entry_desc.get("1.0", tk.END) if hasattr(self.entry_desc, 'get') else "N/A"
        print(f"Medicine to add: {name}, Price: {price}")
    
    def remove_medicine_ui(self):
        print("Remove Medicine clicked - UI only")
        selection = self.medicine_listbox.curselection()
        if selection:
            print(f"Removing item at index {selection[0]}")
    
    def refresh_list_ui(self):
        print("Refresh List clicked - UI only")
    
    def update_price_ui(self):
        print("Update Price clicked - UI only")
        medicine = self.medicine_combo.get()
        new_price = self.entry_new_price.get()
        print(f"Updating {medicine} to ${new_price}")

class PharmaGoFrontendV4:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PharmaGo - Version 4")
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
                 command=self.open_pharmacist_portal).pack(pady=20)
        
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
    
    def open_pharmacist_portal(self):
        PharmacistPortalWindow(self.root)
    
    def open_help(self):
        HelpWindow(self.root)
    
    def run(self):
        self.setup_ui()
        self.root.mainloop()

if __name__ == "__main__":
    app = PharmaGoFrontendV4()
    app.run()