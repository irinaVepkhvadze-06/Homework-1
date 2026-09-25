Pin: str = ""
tries = 0

while Pin != "1234" and tries < 3:
        Pin: str = input("Please enter your Pin: ")
        tries += 1

        if Pin == "1234":
            print("Access granted!")
            break

        if Pin != "1234" and tries < 3:
            print(f"Incorrect PIN. Remaining attempts: {3 - tries}")
           
else:
        print("Card blocked!")






