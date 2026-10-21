def add_task(task_name, task_list = None):
    if task_list is None:
        task_list = []
    task_list.append(task_name)
    print(task_list)

add_task("Study English")
add_task("Study Python")
add_task("Clean the house") 

# აქ უკვე ყოველი გაშვებისას თავიდან ქმნის ცარიელ ლისტს