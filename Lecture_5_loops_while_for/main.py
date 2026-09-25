# count = 0   #0 1 2 3 4 5
# while count < 5:
#     print(count)  #0 1 2 3 4
#     count += 1

# i = 5 # 5 4 3 2 1
# while i > 0:
#     print(i)
#     i -= 1

#sentinel

# passward: Literal[""] = ""
# tries = 0
# while passward != "Python" and tries < 3:
#     passward: str = input("Please enter your password: ")
#     tries += 1

#     if passward != "Python" and tries == 3:
#         print("You enter the wrong password 3 times")
# else:
#     print("You entered the correct password")

# print("You entered the correct password")


# age = -1
# while age < 0 or age > 120:
#     age = int(input("Please enter your age: "))
# print(f"You are {age} years old")

# i = 1
# total = 0  #+1 +2 +3 +4 +5

# while i <= 5: 
#     total += i
#     i += 1

# print(total)

# while True:
#     text = input("Please enter you text: ").strip().lower()

#     if text == "exit":
#         print("Exiting...")
#         break

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)  # 1 2 4 

# print("y" in "Python")

# for i in "Python":
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(5, 11):
#     print(i)

# for i in range(5, 11, 2):
#     print(i)

# for i in range(10, 4, -1):
#     print(i)

# total = 0
# for i in range(1, 6):
#     total += 1
#     print(total)

# for i in range(1, 6):
#     if i  == 3:
#         break
#     print(i)

# for i in range(1, 6):
#     if i ==3:
#         continue
#     print(i)

# for row in range(4):
#     for col in range(3):
#         print("*", end=" ")
#     print()