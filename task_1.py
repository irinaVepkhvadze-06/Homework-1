with open("qoutes.txt", "w") as file:

    My_qoutes = input("Enter your favourite author and qoute: ")

    file.write(My_qoutes)

with open("qoutes.txt", "r") as file:
    data = file.read()
    print(data)

print()