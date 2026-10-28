# empty_dict: dict = {}
# print(type(empty_dict))

# scores: dict = {
#     "Python": 97,
#     "Java": 90,
#     "C++": 80
# }
# print(scores)

# scores = dict(python=97, java=90, c=80)
# print(scores)

# person: dict [str] = {
#     "name":"John",
#     "age": 20,
#     "city": "Tbilisi",
#     "scores": [78, 90, 86],
#     "is_active": True,
#     "hobbies": ("coding", "reading", "skiing")

# print(person["name"])
# print(person["scores"])

# first_name : None = person.get("name")
# print(first_name)

# country = person.get("country", "Not found")
# print(country)

# person["country"] = "Georgia"
# print(person)

# # scores: dict[str, int] = {
# #     "Python": 97,
# #     "Java": 90
# }

# scores["C++"] = 85
# print(scores)

# scores.clear()
# print(scores)

# del scores["Java"]
# print(scores)

# removed: int = scores.pop("Java")
# print(removed)
# print(scores)

# removed = scores.pop("C++", None)
# print(removed)
# print(scores)

# print(scores.keys())
# print(scores.values())
# print(scores.items())

# print(len(scores))
# print("Python" in scores)

# scores: dict[str, int] = {
#     "Python": 97,
#     "Java": 90,
#     "C++": 80
# }

# for i in scores:
#     print(i)

# for i in scores.values():
#     print(i)

# for key, value in scores.items():
#     print(f"key: {key}, value: {value}")

# lst = [i for i in range(1, 6)]
# print(lst)

# dct = {i: i ** 2 for i in range(1, 6) if i % 2 == 0}
# print(dct)
    
person: dict = {
    "name": "Anna",
    "age": 20,
    "scores": {
        "Python": 97,
        "Java": 90
    }
}
scores = person["scores"]
print(scores)