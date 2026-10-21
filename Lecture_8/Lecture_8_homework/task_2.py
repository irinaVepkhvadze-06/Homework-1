student: dict = {
    "name": "Ana",
    "contact": {
        "email": "ana@gmail.com",
        "phone": "123-456-78910"
    },
    "courses": {"Python": 51, 
               "Passed": False,
               "Java": 90, 
               "Passed": True,
               "Web": 40, 
               "Passed": False}
}
print(student["contact"] ["email"])
print(student["courses"]["Python"])

student["courses"]["Web"] = {"score": 65, 
         "Passed": True
}
print(student["courses"])


del student["contact"]["phone"]
print(student)

