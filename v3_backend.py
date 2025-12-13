from v2 import *

def load_pharmacist_credentials():
    """Load pharmacist credentials from JSON file"""
    if os.path.exists(pharmacist_credentials_file):
        with open(pharmacist_credentials_file, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    else:
        return {}

def save_pharmacist_credentials():
    """Save pharmacist credentials to JSON file"""
    with open(pharmacist_credentials_file, "w") as file:
        json.dump(pharmacist_credentials, file, indent=4)

# Load credentials at module level
pharmacist_credentials = load_pharmacist_credentials()

def check_pharmacist_credentials(username, password):
    """Verify pharmacist login credentials"""
    if username in pharmacist_credentials and pharmacist_credentials[username] == password:
        print(f"Pharmacist '{username}' verified successfully!")
        return True
    else:
        print("Invalid pharmacist credentials.")
        return False

def add_pharmacist_account(username, password):
    """Add a new pharmacist account"""
    if not username or not password:
        return False, "Username and password are required."
    
    if username in pharmacist_credentials:
        return False, f"Username '{username}' already exists."
    
    pharmacist_credentials[username] = password
    save_pharmacist_credentials()
    
    return True, f"Pharmacist account '{username}' created successfully."

def remove_pharmacist_account(username):
    """Remove a pharmacist account"""
    if username in pharmacist_credentials:
        del pharmacist_credentials[username]
        save_pharmacist_credentials()
        return True, f"Pharmacist account '{username}' removed."
    else:
        return False, f"Pharmacist account '{username}' not found."

def list_pharmacist_accounts():
    """List all pharmacist accounts"""
    if not pharmacist_credentials:
        return "No pharmacist accounts found."
    
    result = "Pharmacist Accounts:\n"
    for username in pharmacist_credentials:
        result += f"Username: {username}\n"
    
    return result

def initialize_default_pharmacist():
    """Initialize with a default pharmacist account if none exists"""
    if not pharmacist_credentials:
        success, message = add_pharmacist_account("admin", "1234")
        print(f"Default pharmacist created: {message}")
        return success, message
    return True, "Pharmacist accounts already exist."

if __name__ == "__main__":
    print("=== Testing Pharmacist Authentication ===\n")
    
    # Initialize default pharmacist
    init_result = initialize_default_pharmacist()
    print(f"Initialization: {init_result[1]}")
    
    # Test adding pharmacist accounts
    print(f"\nAdding pharmacists:")
    result1 = add_pharmacist_account("pharmacist1", "pass123")
    print(f"  - {result1[1]}")
    
    result2 = add_pharmacist_account("pharmacist2", "pass456")
    print(f"  - {result2[1]}")
    
    # Test authentication
    print(f"\nTesting authentication:")
    auth1 = check_pharmacist_credentials("admin", "1234")
    print(f"  - admin/1234: {'✓' if auth1 else '✗'}")
    
    auth2 = check_pharmacist_credentials("pharmacist1", "wrongpass")
    print(f"  - pharmacist1/wrongpass: {'✓' if auth2 else '✗'}")
    
    # List accounts
    print(f"\n{list_pharmacist_accounts()}")
    
    # Test account management integration
    print("\n=== Testing Customer Account Integration ===")
    create_account("Test Customer", "5551234", "9999", "Giza", "Pyramid St", "Near Sphinx")
    print(f"Customer accounts: {len(personal_info)}")