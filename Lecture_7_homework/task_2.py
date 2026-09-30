try:
    age = int(input("Please enter your age: "))
    if  age < 0:
        raise ValueError("Age cannot be negative!")
    elif age < 18:
        raise ValueError("User must be at least 18 years old to register.")
    
    print("Registration is available")

except ValueError as e:
    print(e)

finally:
    print("Registration process completed.")