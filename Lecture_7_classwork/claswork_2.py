try:
    password = input("Enter your password: ")
    if len(password) < 6:
        raise ValueError("Password is too short!")
        
    print("Password is valid")

except ValueError as e:
    print(e)