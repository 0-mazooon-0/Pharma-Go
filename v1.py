import tkinter as tk
from PIL import Image, ImageTk

class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PharmaGo - Version 1")
        self.root.configure(bg="#D5F5E3")
        self.root.geometry('1024x1024')
        
    def setup_ui(self):
        # Background image
        try:
            background_image = Image.open("111.jpg")
            background_image = background_image.resize((1024, 1024), Image.Resampling.LANCZOS)
            self.background_photo = ImageTk.PhotoImage(background_image)
            background_label = tk.Label(self.root, image=self.background_photo)
            background_label.place(relwidth=1, relheight=1)
        except:
            print("Background image not found, using solid color")
        
        # Main label
        tk.Label(self.root, text="Welcome to PharmaGo", 
                font=("Arial", 50, "bold"), bg="#D5F5E3", fg="#1E8449").pack(pady=100)
        
        # Buttons with placeholder commands
        tk.Button(self.root, text="New Customer", 
                 bg="#1E8449", fg="white", font=("Arial", 20), 
                 command=self.new_customer_placeholder).pack(pady=20)
        
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
    
    def new_customer_placeholder(self):
        print("New Customer clicked - UI only")
    
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
    app = MainMenu()
    app.run()