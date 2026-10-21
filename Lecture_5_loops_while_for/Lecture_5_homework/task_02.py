n = int(input("Please enter a Positive number: "))
total = 0

for n in range(2, n+1, 2):
    total += n
print(f"The sum of even numbers from 1 to {n} is: {total}")