correct_username = "admin"
correct_password = "1234"
username_access = False
password_access = False
attempts = 0
max_attempts = 4
while attempts < max_attempts:
    if not username_access:
        username = input("Enter username: ")
        attempts += 1
        if username == correct_username:
            username_access = True
            attempts = 0
        else:
            if attempts == max_attempts:
                print("Account locked.")
                break
            else:
                print("Incorrect username. Try again.")
    elif not password_access:
        password = input("Enter password: ")
        attempts += 1
        if password == correct_password:
            print("Login successful!")
            break
        else:
            if attempts == max_attempts:
                print("Account locked.")
                break
            else:
                print("Incorrect password. Try again.")