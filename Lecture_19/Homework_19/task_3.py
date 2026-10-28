def create_contact():
    phonebook = {
        "Giorgi": "123-456",
        "Ana": "234-789",
        "Nika": "125-365",
        "Mari": "456-095"
    }
    print(phonebook.get("Gio", "Not found"))

create_contact()