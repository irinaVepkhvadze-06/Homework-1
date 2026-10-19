import csv 
filtered_companies = []
with open("ssl_companies.csv", "r", encoding="utf-8") as file:
    
    reader = csv.DictReader(file)
    for row in reader:
            if int(row["Number of employees"]) > 1000:
                 print(row["Name"])
                 filtered_companies.append({"Name": row ["Name"], 
                                            "Industry": row ["Industry"], 
                                            "Number of employees": row ["Number of employees"]
 })

with open("sorted_companies.csv", "w", encoding="utf-8") as file:
      fieldnames = ["Name", "Industry", "Number of employees"]
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      
      for row in filtered_companies:
        
        writer.writerow(row)

print("Done")
