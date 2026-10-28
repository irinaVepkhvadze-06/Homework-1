# num = int(input("Enter a number: "))
# print("after input")

# name: any = irina
# print("hello")


# try:
#     number1 = int(input("Enter a number1: "))
#     number2 = int(input("Enter a number2: "))
#     result = number1 / number2
#     print(result)

# except:
#     print("something went wrong")

# try:
#     for i in range(1000000000000000):
#         print(i)
# except:
#     print("something went wrong")

# try:

#     number1 = float(input("Enter a number1: "))
#     number2 = float(input("Enter a number2: "))

#     # open("file.txt")

#     result: float = number1 / number2

#     print(result)

# except ZeroDivisionError:
#     print("You can't divide by zero")

# except ValueError:
#     print("You must enter a number")


# except Exception as e:
#     print(e)

# try:
#     lst:list[int] = [1, 2, 3, 4, 5, 6,0]

#     for i in lst:
#         if i == 0:
#             raise ValueError("Zero is not allowed")

# except ValueError as e:
#     print(e)


                
# try:
#     number1 = int(input("Enter a number1: "))
#     number2 = int(input("Enter a number2: "))
    
#     result = number1 / number2
#     print(result)

# except Exception as e:
#     print(e)

# else:
#     print("Everything is fine")

# finally:
#     print("The code is done")

# try:
#     raise ArithmeticError("something went wrong") from ZeroDivisionError("division by zero")

# except ArithmeticError as e:
#     print(e)
#     print(e.__cause__)