def even_numbers():
    num = 0
    while True:
        yield num 
        num += 2
count = 0
for num in even_numbers():
    count +=1
    print(num, end=",")
    if count == 10:
        break
   