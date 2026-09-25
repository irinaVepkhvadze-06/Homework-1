# temperature = 32
# if temperature >=30:
#     print("It's hot  today")
# else:
#     print("It's cold today")

# print("We have some weather")


# # bad example 

# if temperature >=30:
#     print("it's hot today")
# if temperature < 30:
#     print("it's cold today")


# score = 83

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >=60:
#     print("D")
# else:
#     print("f")

# # Wrong Example
# if score >= 60:
#     print("D")
# elif score >= 70:
#     print("C")
# elif score >= 80:
#     print("B")
# elif score >= 90:
#     print("A")


# if score >= 90:
#     print("A")
# if score >= 80:
#     print("B")
# if score >= 70:
#     print("C")



# age = 22
# has_id = True
# has_certificate = True

# if age >=18 and has_id and has_certificate:
#     print("You can vote")
# else:
#     print("You can't vote")


# print(True and True)
# print(True and False)
# print(True and True and False)


# print(True or True)
# print(True or False)
# print(True or True or False)
# print(False or True)
# print(False or False)


# is_admin = False
# is_moderator = True

# if is_admin or is_moderator:
#     print("You can delete this post")
# else: 
#     print("You can't delete this post")


# print(not True)
# print(not False)


# is_raining = False

# if not is_raining:
#     print("The weather is good")
# else:
#     print("The weather is Bad")

# name: str = input("Enter your name: ")
# if not name:
#     print("Please enter your name")
# else:
#     print(f"hello {name}")


# logical operators priorities
# 1. not
# 2. and
# 3. or


# age = 18
# country = "GE"
# has_ticket = True

# if age >= 18 and country =="GE" or country == "US" and has_ticket:
    # print("You can enter")   #bad example 

# if age >= 18 and (country == "GE" or country == "US") and has_ticket:
#     print("You can enter")
# else:
#     print("You can't enter")

# age = 16
# has_id = True
# has_ticket = True

# if age >=18:
#     if has_id and has_ticket:
#         print("You can enter")
#     else:
#         print("You can't enter")
# else:
#     print("You are underage")
# bad examle 
# if age >= 18 and has_ticket and has_id:
#     print('You can enter')
# else:
#     print("You can't enter")


# age = 25 
# has_id = True
# has_ticket = True

# if age >= 18:
#     if has_ticket:
#         if has_id:
#             print("You can enter")
#         else:
#             print("You have not id")
#     else: 
#         print("You haven't ticket")
# else:
#     print("You are underage")


# print(True and False or True) #False or True
# print(True and (False or True))
# print(True and(True and False))
# print(not True or False)
