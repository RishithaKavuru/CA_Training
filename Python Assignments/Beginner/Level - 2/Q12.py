#Q12

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    retype_password = input("Re-Type password: ")
    
    if password != retype_password:
        print("Passwords do not match. Please try again.")
        return login()
    
    attempts = 3
    while attempts > 0:
        entered_password = input("Enter your password to login: ")
        if entered_password == password:
            print("Login successful!")
            return
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts left.")
    
    print("Too many failed attempts. Access denied.")

login()
