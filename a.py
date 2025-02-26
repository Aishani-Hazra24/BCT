from prettytable import PrettyTable
users = []
def sign_up():
    name = input("Enter your name: ")
    email = input("Enter your email ID: ")

  
    for user in users:
        if user["Email"] == email:
            print("Email already registered. Try logging in.")
            return
    
    password = input("Enter your password: ")  
    users.append({"Name": name, "Email": email, "Password": password})
    print("Sign-up successful!")


def log_in():
    email = input("Enter your email ID: ")
    password = input("Enter your password: ")

    for user in users:
        if user["Email"] == email and user["Password"] == password:
            print("Login successful!")
            return True
    print("Login failed! Incorrect email or password.")
    return False


def display_users():
    if not users:
        print("No users found.")
        return

    table = PrettyTable(["Name", "Email"])
    for user in users:
        table.add_row([user["Name"], user["Email"]])
    
    print("\nRegistered Users:")
    print(table)


def delete_user():
    email = input("Enter the email ID of the user to delete: ")

    for user in users:
        if user["Email"] == email:
            users.remove(user)
            print("User deleted successfully!")
            return
    
    print("User not found.")