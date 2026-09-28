inventory = ["apple", "banana", "orange", "apple", "kiwi", "apple"]
new_items = ["mango", "grapes"]

print(inventory.index("orange"))

print(inventory.count("apple"))

inventory.extend(new_items)
print(inventory[::-1])