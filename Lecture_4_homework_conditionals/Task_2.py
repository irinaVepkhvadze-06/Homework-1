cart_total = 50
is_vip = True
is_guest = False
promo_code = "Save10"

# if promo_code exists:

if promo_code:
    print("Promo code exist")
else:
    print("Promo code doesn't exist")
    
# check the user is NOT a guest:

if not is_guest:
    print("The user isn't guest")
else:
    print("The user is guest")

# Free Shipping or not:

if cart_total >= 50 or is_vip: 
    print("Free shipping")
else:
    print("Pay for shipping")

# discount

if promo_code == "Save10" and not is_guest:
    print("10% discount")
else:
    print("Final total price")