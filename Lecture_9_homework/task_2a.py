def add_task(task_name, task_list = []):
    task_list.append(task_name)
    print(task_list)

add_task("Study English")
add_task("Study Python")
add_task("Clean the house") 
#ყოველ გამოძახებაზე ცარიელ ლისტს არ გვიქმნის, რაც არასწორი მიდგომაა 
# ყოველ გაშვებაზე ცარიელი უნდა იყოს ლისტი ამიტომ უნდა გამოვიყენოთ task_list = None