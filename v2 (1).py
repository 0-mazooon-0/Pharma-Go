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