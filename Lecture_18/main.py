class Father:
    eye_color = "brown"

    def sing(self):
        print("Can sing")

class Mother:
    hair_color = "blonde"

    def dance(self):
        print("Can dance")

class Child(Father, Mother):
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def talk(self):
        print(f"Hi my name is {self.name} and i am {self.age} years old")

c = Child("John", 24)
c.talk()