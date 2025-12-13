import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Import previous versions
from Front.v4_frontend import (NewAccountWindow, CustomerLoginWindow, 
PharmacistLoginWindow, HelpWindow, PharmacistPortalWindow)

class TransactionWindow:
    def __init__(self, parent, customer_name="Customer"):
        self.parent = parent
        self.customer_name = customer_name
        self.window = tk.Toplevel(parent)
        self.window.title("Transaction Portal - Version 5")
        self.window.configure(bg="#D5F5E3")
        self.window.geometry('1000x800')
        
        # Mock cart data
        self.cart_items = []
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        tk.Label(self.window, text=f"Welcome, {self.customer_name}!", 
                font=("Arial", 24, "bold"), bg="#D5F5E3").pack(pady=20)
        
        # Main content frame
        main_frame = tk.Frame(self.window, bg="#D5F5E3")
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Left frame - Medicine selection
        left_frame = tk.Frame(main_frame, bg="#D5F5E3")
        left_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=10)
        
        # Right frame - Cart
        right_frame = tk.Frame(main_frame, bg="#D5F5E3")
        right_frame.pack(side=tk.RIGHT, fill='both', expand=True, padx=10)
        
        # Setup left frame (Medicine selection)
        self.setup_medicine_selection(left_frame)
        
        # Setup right frame (Cart)
        self.setup_cart_display(right_frame)
        
        # Exit button
        tk.Button(self.window, text="Exit Transaction", 
                 bg="#2874A6", fg="white", font=("Arial", 14),
                 command=self.window.destroy).pack(pady=20)
    
    def setup_medicine_selection(self, parent):
        tk.Label(parent, text="Select Medicine", 
                font=("Arial", 16, "bold"), bg="#D5F5E3").pack(pady=10)
        
        # Medicine dropdown
        tk.Label(parent, text="Medicine:", 
                bg="#D5F5E3", font=("Arial", 12)).pack(pady=5)
        
        sample_medicines = ["Panadol", "Voltaren", "Catafast", "Congestal", "Omega3"]
        self.medicine_combo = ttk.Combobox(parent, 
                                          values=sample_medicines,
                                          font=("Arial", 12), 
                                          width=30)
        self.medicine_combo.pack(pady=5)
        self.medicine_combo.set("Select medicine")
        
        # Buttons
        button_frame = tk.Frame(parent, bg="#D5F5E3")
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Add to Cart", 
                 bg="#1E8449", fg="white", font=("Arial", 12),
                 command=self.add_to_cart_ui).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="View Description", 
                 bg="#3498DB", fg="white", font=("Arial", 12),
                 command=self.view_description_ui).pack(side=tk.LEFT, padx=5)
        
        # Search/Filter
        tk.Label(parent, text="Search Medicine:", 
                bg="#D5F5E3", font=("Arial", 12)).pack(pady=(30,5))
        
        search_frame = tk.Frame(parent, bg="#D5F5E3")
        search_frame.pack(pady=5)
        
        self.search_entry = tk.Entry(search_frame, font=("Arial", 12), width=25)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Button(search_frame, text="Search", 
                 bg="#D35400", fg="white", font=("Arial", 12),
                 command=self.search_medicine_ui).pack(side=tk.LEFT, padx=5)
    
    def setup_cart_display(self, parent):
        tk.Label(parent, text="Your Cart", 
                font=("Arial", 16, "bold"), bg="#D5F5E3").pack(pady=10)
        
        # Cart listbox
        list_frame = tk.Frame(parent, bg="#D5F5E3")
        list_frame.pack(pady=10, fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.cart_listbox = tk.Listbox(list_frame, 
                                      height=15, 
                                      font=("Arial", 12),
                                      yscrollcommand=scrollbar.set)
        self.cart_listbox.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.config(command=self.cart_listbox.yview)
        
        # Total price display
        self.total_label = tk.Label(parent, text="Total: $0.00", 
                                   font=("Arial", 14, "bold"), bg="#D5F5E3", fg="#1E8449")
        self.total_label.pack(pady=10)
        
        # Cart buttons
        cart_button_frame = tk.Frame(parent, bg="#D5F5E3")
        cart_button_frame.pack(pady=20)
        
        tk.Button(cart_button_frame, text="Remove Item", 
                 bg="#A93226", fg="white", font=("Arial", 12),
                 command=self.remove_item_ui).pack(side=tk.LEFT, padx=5)
        
        tk.Button(cart_button_frame, text="Clear Cart", 
                 bg="#E74C3C", fg="white", font=("Arial", 12),
                 command=self.clear_cart_ui).pack(side=tk.LEFT, padx=5)
        
        tk.Button(cart_button_frame, text="Proceed to Payment", 
                 bg="#1E8449", fg="white", font=("Arial", 12),
                 command=self.payment_ui).pack(side=tk.LEFT, padx=5)
        
        # PDF Import button
        tk.Button(parent, text="Import Prescription PDF", 
                 bg="#8E44AD", fg="white", font=("Arial", 12),
                 command=self.import_pdf_ui).pack(pady=10)
    
    def add_to_cart_ui(self):
        medicine = self.medicine_combo.get()
        if medicine and medicine != "Select medicine":
            price = 10.0  # Mock price
            self.cart_items.append((medicine, price))
            self.update_cart_display()
            print(f"Added {medicine} to cart")
    
    def view_description_ui(self):
        medicine = self.medicine_combo.get()
        if medicine and medicine != "Select medicine":
            print(f"Showing description for {medicine}")
            # In real app, this would show a messagebox
    
    def search_medicine_ui(self):
        search_term = self.search_entry.get()
        print(f"Searching for: {search_term}")
    
    def remove_item_ui(self):
        selection = self.cart_listbox.curselection()
        if selection:
            index = selection[0]
            if index < len(self.cart_items):
                self.cart_items.pop(index)
                self.update_cart_display()
                print(f"Removed item at index {index}")
    
    def clear_cart_ui(self):
        self.cart_items = []
        self.update_cart_display()
        print("Cart cleared")
    
    def payment_ui(self):
        total = sum(price for _, price in self.cart_items)
        print(f"Processing payment: ${total:.2f}")
        self.cart_items = []
        self.update_cart_display()
    
    def import_pdf_ui(self):
        print("Import PDF clicked - UI only")
    
    def update_cart_display(self):
        self.cart_listbox.delete(0, tk.END)
        total = 0
        
        for medicine, price in self.cart_items:
            item_text = f"{medicine} - ${price:.2f}"
            self.cart_listbox.insert(tk.END, item_text)
            total += price
        
        self.total_label.config(text=f"Total: ${total:.2f}")

class PharmaGoFrontendV5:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PharmaGo - Version 5")
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
        
        # Demo button to show transaction window directly
        tk.Button(self.root, text="[Demo] Open Transaction", 
                 bg="#8E44AD", fg="white", font=("Arial", 14),
                 command=lambda: TransactionWindow(self.root, "Demo User")).pack(pady=10)
    
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
    app = PharmaGoFrontendV5()
    app.run()