import csv 

survived_row = []

with open("titanic.csv", "r", encoding="utf-8") as file:
    
    reader = csv.DictReader(file)
    for row in reader:
            if int(row["Survived"]) == 1:
                print(row["Name"])
                survived_row.append(row)


with open("survived.csv", "w", encoding="utf-8", newline="") as file:
    fieldname = reader.fieldnames

    writer = csv.DictWriter(file, fieldnames=fieldname)
    writer.writeheader()
    for row in survived_row:
         
         writer.writerow(row)

print("Done")
         
         
 
        





