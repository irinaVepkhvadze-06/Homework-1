names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

zipped_data = list(zip(names, prices, ratings))
print(zipped_data)

sorted_by_price = sorted(zipped_data, key=lambda s:s[1], reverse = True)

print(sorted_by_price)

products_by_rating = sorted(zipped_data, key=lambda s:s[2])

print(products_by_rating)