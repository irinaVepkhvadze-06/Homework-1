correct_pin = 3434
balance = 300.50
requested_amount = 100.00

user_pin = int(input("Enter your pin: "))

if user_pin == correct_pin:
        if requested_amount <= balance: 
            print(f"Withdrawal successful! Remaining_balance: $ {balance - requested_amount}")
        else: 
            print("Amount of your balance isn't enough")
else:
    print("Incorrect PIN. Access Denied")
   
    