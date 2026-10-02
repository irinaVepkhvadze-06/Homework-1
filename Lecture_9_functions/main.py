# def calculate_sum():
#     print(5+3)
# calculate_sum()

# def calculate_sum():
#     x = 5
#     y = 3
#     print(x + y)
# calculate_sum()
# calculate_sum()
# calculate_sum()
# print("Hello")
# calculate_sum()

# def calculate_sum():
#     x = 5
#     y = 3
#     print(x + y)
# calculate_sum()

# def calculate_sum(x, y):
#     print(x + y)
# calculate_sum(5, 3)
# calculate_sum(10, 4)

# def full_name(first_name, last_name):
#    print(f"{first_name} {last_name}")

# full_name("Ana", "Smith")

# full_name(last_name="Doe", first_name="John")

# def full_name(first_name, last_name, age, status="student", ):
#    print(f"{first_name} {last_name}")
#    print(f"Age: {age}, status: {status}")

# f_name: str = input("Enter your first name: ").capitalize()
# l_name: str = input("Enter your last name: ").capitalize()

# full_name(f_name, l_name, status="teacher", age=30)

# def append_item(item, lst=[]):
#     lst.append(item)
#     print(lst)

# append_item("Python")
# append_item("Java")
# append_item("JavaScript", ["HTML", "CSS"])

# def append_item(item, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(item)

#     print(lst)

# append_item("Python", ["HTML", "CSS"])
# append_item("Java")

# def full_name(first_name, last_name):
#     return f"{first_name} {last_name}"

# f_name: str = input("Enter your first name: ").capitalize()
# l_name: str = input("Enter your last name: ").capitalize()

# # print(full_name(f_name, l_name))

# name:str = full_name(f_name, l_name)
# print(name)


# def check_age(age):
#     if age < 0:
#         return "Invalid age"
#     if age < 18:
#         return "You are younger than 18"
#     else:
#         return "You are older than 18"

# # print(check_age(-10))
# print(check_age(15))


# def divmod(a, b):
#     return a // b, a % b

# # print(divmod(10, 3))

# floor_division, modulus = divmod(10, 3)
# print(floor_division)
# print(modulus)

# def sum():
#     x = 5
#     y = 3
#     return x + y

# print(x)


# def student(name, age, *args):
#     return f"{name} is {age} years old, {args}"

# print(student("John", 20, "Tbilisi", "Reading"))

# def student(name, age, *kwargs):
#     return f"{name} is {age} years old, {kwargs}"

# print(student("John", 20, hobby="Reading", city="Tbilisi"))