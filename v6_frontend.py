import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import io

# Import previous versions
from Front.v5_frontend import (NewAccountWindow, CustomerLoginWindow, 
                                   PharmacistLoginWindow, HelpWindow, 
                                   PharmacistPortalWindow, TransactionWindow)

class PDFViewerWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("PDF Viewer - Version 6")
        self.window.configure(bg="#D5F5E3")
        self.window.geometry('900x700')
        
        # Mock PDF data
        self.current_page = 0
        self.total_pages = 5
        self.pdf_loaded = False
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.window, bg="#D5F5E3")
        header_frame.pack(fill='x', pady=10)
        
        tk.Label(header_frame, text="PDF Prescription Viewer", 
                font=("Arial", 20, "bold"), bg="#D5F5E3").pack(side=tk.LEFT, padx=20)
        
        # Import button
        tk.Button(header_frame, text="Import PDF", 
                 bg="#3498DB", fg="white", font=("Arial", 12),
                 command=self.import_pdf_ui).pack(side=tk.RIGHT, padx=20)
        
        # Main display area
        display_frame = tk.Frame(self.window, bg="white", relief=tk.SUNKEN, bd=2)
        display_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Canvas for PDF display (mock)
        self.canvas = tk.Canvas(display_frame, bg="white", highlightthickness=0)
        self.canvas.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create mock PDF content
        self.create_mock_pdf_content()
        
        # Page navigation
        nav_frame = tk.Frame(self.window, bg="#D5F5E3")
        nav_frame.pack(pady=10)
        
        tk.Button(nav_frame, text="◀ Previous", 
                 bg="#2874A6", fg="white", font=("Arial", 12),
                 command=self.previous_page).pack(side=tk.LEFT, padx=5)
        
        self.page_label = tk.Label(nav_frame, text="Page 1 of 5", 
                                  font=("Arial", 12), bg="#D5F5E3")
        self.page_label.pack(side=tk.LEFT, padx=20)
        
        tk.Button(nav_frame, text="Next ▶", 
                 bg="#2874A6", fg="white", font=("Arial", 12),
                 command=self.next_page).pack(side=tk.LEFT, padx=5)
        
        # Zoom controls
        zoom_frame = tk.Frame(self.window, bg="#D5F5E3")
        zoom_frame.pack(pady=10)
        
        tk.Label(zoom_frame, text="Zoom:", 
                font=("Arial", 12), bg="#D5F5E3").pack(side=tk.LEFT, padx=5)
        
        tk.Button(zoom_frame, text="+", 
                 bg="#D5F5E3", fg="black", font=("Arial", 12),
                 command=self.zoom_in).pack(side=tk.LEFT, padx=2)
        
        tk.Button(zoom_frame, text="-", 
                 bg="#D5F5E3", fg="black", font=("Arial", 12),
                 command=self.zoom_out).pack(side=tk.LEFT, padx=2)
        
        tk.Button(zoom_frame, text="Fit to Page", 
                 bg="#D5F5E3", fg="black", font=("Arial", 12),
                 command=self.fit_to_page).pack(side=tk.LEFT, padx=10)
        
        # Close button
        tk.Button(self.window, text="Close Viewer", 
                 bg="#A93226", fg="white", font=("Arial", 14),
                 command=self.window.destroy).pack(pady=20)
    
    def create_mock_pdf_content(self):
        """Create mock PDF display content"""
        self.canvas.delete("all")
        
        # Draw a mock PDF page
        self.canvas.create_rectangle(50, 50, 800, 500, outline="black", width=2)
        
        # Add some text to simulate PDF content
        self.canvas.create_text(200, 100, text="PRESCRIPTION", 
                               font=("Arial", 24, "bold"), anchor="w")
        
        self.canvas.create_line(50, 130, 800, 130, fill="black", width=1)
        
        # Mock prescription content
        prescription_content = [
            ("Patient Name:", "John Doe"),
            ("Date:", "2024-01-15"),
            ("Doctor:", "Dr. Smith"),
            ("Medication:", "Amoxicillin 500mg"),
            ("Dosage:", "Take 1 capsule every 8 hours"),
            ("Duration:", "7 days"),
            ("Refills:", "0"),
            ("Instructions:", "Take with food"),
            ("Doctor Signature:", "_________________")
        ]
        
        y_position = 170
        for label, value in prescription_content:
            self.canvas.create_text(100, y_position, text=label, 
                                   font=("Arial", 12, "bold"), anchor="w")
            self.canvas.create_text(300, y_position, text=value, 
                                   font=("Arial", 12), anchor="w")
            y_position += 30
        
        # Add a mock pharmacy stamp
        self.canvas.create_rectangle(600, 400, 780, 480, outline="blue", width=2)
        self.canvas.create_text(690, 420, text="PHARMACY", 
                               font=("Arial", 14, "bold"))
        self.canvas.create_text(690, 450, text="STAMP", 
                               font=("Arial", 12))
    
    def import_pdf_ui(self):
        print("Opening file dialog for PDF import")
        # In real app, this would open file dialog
        # For now, just simulate loading
        self.pdf_loaded = True
        self.current_page = 0
        self.total_pages = 8
        self.update_page_display()
        self.create_mock_pdf_content()
        
        # Show success message
        self.canvas.create_text(400, 550, text="PDF successfully loaded!", 
                               font=("Arial", 14, "bold"), fill="green")
    
    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_page_display()
            print(f"Navigating to page {self.current_page + 1}")
    
    def next_page(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.update_page_display()
            print(f"Navigating to page {self.current_page + 1}")
    
    def update_page_display(self):
        self.page_label.config(text=f"Page {self.current_page + 1} of {self.total_pages}")
    
    def zoom_in(self):
        print("Zooming in")
        # In real app, this would zoom the PDF view
    
    def zoom_out(self):
        print("Zooming out")
        # In real app, this would zoom the PDF view
    
    def fit_to_page(self):
        print("Fitting to page")
        # In real app, this would adjust the view

class PharmaGoFrontendV6:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PharmaGo - Version 6 (Complete UI)")
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
        main_frame = tk.Frame(self.root, bg="#D5F5E3")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(main_frame, text="Welcome to PharmaGo", 
                font=("Arial", 50, "bold"), bg="#D5F5E3", fg="#1E8449").pack(pady=20)
        
        tk.Label(main_frame, text="Version 6 - Complete Frontend UI", 
                font=("Arial", 20), bg="#D5F5E3", fg="#2874A6").pack(pady=10)
        
        # Main buttons
        buttons_frame = tk.Frame(main_frame, bg="#D5F5E3")
        buttons_frame.pack(pady=30)
        
        tk.Button(buttons_frame, text="New Customer", 
                 bg="#1E8449", fg="white", font=("Arial", 18), 
                 command=self.open_new_account, width=20).grid(row=0, column=0, pady=10, padx=10)
        
        tk.Button(buttons_frame, text="Existing Customer", 
                 bg="#2874A6", fg="white", font=("Arial", 18),
                 command=self.open_customer_login, width=20).grid(row=0, column=1, pady=10, padx=10)
        
        tk.Button(buttons_frame, text="Pharmacist Portal", 
                 bg="#D35400", fg="white", font=("Arial", 18),
                 command=self.open_pharmacist_portal, width=20).grid(row=1, column=0, pady=10, padx=10)
        
        tk.Button(buttons_frame, text="Help", 
                 bg="#A93226", fg="white", font=("Arial", 18),
                 command=self.open_help, width=20).grid(row=1, column=1, pady=10, padx=10)
        
        # Demo buttons for direct access
        demo_frame = tk.Frame(main_frame, bg="#D5F5E3")
        demo_frame.pack(pady=20)
        
        tk.Label(demo_frame, text="Demo Features:", 
                font=("Arial", 14, "bold"), bg="#D5F5E3").pack()
        
        tk.Button(demo_frame, text="Open Transaction Portal", 
                 bg="#8E44AD", fg="white", font=("Arial", 12),
                 command=lambda: TransactionWindow(self.root, "Demo User")).pack(pady=5, padx=10, side=tk.LEFT)
        
        tk.Button(demo_frame, text="Open PDF Viewer", 
                 bg="#17A589", fg="white", font=("Arial", 12),
                 command=self.open_pdf_viewer).pack(pady=5, padx=10, side=tk.LEFT)
        
        # Exit button
        tk.Button(main_frame, text="Exit", 
                 command=self.root.quit, bg="#2874A6", 
                 fg="white", font=("Arial", 16), width=20).pack(pady=30)
    
    def open_new_account(self):
        NewAccountWindow(self.root)
    
    def open_customer_login(self):
        CustomerLoginWindow(self.root)
    
    def open_pharmacist_portal(self):
        PharmacistPortalWindow(self.root)
    
    def open_help(self):
        HelpWindow(self.root)
    
    def open_pdf_viewer(self):
        PDFViewerWindow(self.root)
    
    def run(self):
        self.setup_ui()
        self.root.mainloop()

if __name__ == "__main__":
    app = PharmaGoFrontendV6()
    app.run()