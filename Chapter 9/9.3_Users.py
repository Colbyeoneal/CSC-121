class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.city}.")

    def greet_user(self):
        print(f"{self.first_name} {self.last_name}, welcome.")

user1 = User("Colby", "Oneal", 29, "Black Mountain")
user2 = User("Marcus", "Wallace", 35, "Greenville")
user3 = User ("John", "Linder", 52, "Night City")
user1.describe_user()
user2.describe_user()
user3.describe_user()
user1.greet_user()
user2.greet_user()
user3.greet_user()