class User:
    status = "Active"

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def get_info(self):
        print("-" * 40)
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Status: {self.status}")

user1 = User("Ana", "ana@123.com", 25)
user1.get_info()

user2 = User("Irina", "irina@345.com", 20)
user2.get_info()
