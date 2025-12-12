import json
import os

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

# File paths for storing credentials
pharmacist_credentials_file = "pharmacist_credentials.json"
customer_credentials_file = "customer_credentials.json"

# Global data structures
personal_info = []  # List to store customer accounts
cart = []  # List to store cart items for the current session

# Medicine database
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

def initialize_system():
    """Initialize the system with default data"""
    print("System initialized with data structures")
    print(f"Total medicines: {len(medicines)}")
    print(f"Customer accounts: {len(personal_info)}")
    
    return {
        "medicines_count": len(medicines),
        "customers_count": len(personal_info)
    }

if __name__ == "__main__":
    # Test the data structures
    result = initialize_system()
    print(f"System test completed: {result}")