try:

    fruit = ["apple", "banana", "cherry", "orange"]
    selected_fruit = int(input("Please enter the index number: "))

    print(f"selected_fruit: {fruit[selected_fruit]}")

except ValueError:
        print("Invalid input! Please enter a whole number!")

except IndexError:
    print(f"Index out of bounds! Choose an index between 0 and {len(fruit)-1}.")

else:
    print("Successfully retrieved item!")

