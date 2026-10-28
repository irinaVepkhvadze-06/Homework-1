import json

data: dict = {
    "name": "John",
    "age": 24,
    "scores": [98, 96, 100]
}

print(data)
print(type(data))

json_str = json.dumps(data)
print(json_str)
print(type(json_str))