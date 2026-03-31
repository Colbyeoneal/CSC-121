# Below is what was asked for in 9-5 Login attempts the copied code from 9-3 was 
# moved to lower in the block

# USER COLBY
class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.city}.")

    def greet_user(self):
        print(f"{self.first_name} {self.last_name}, welcome.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Colby", "Oneal", 29, "Black Mountain")

user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
user1.increment_login_attempts()

print(f"Login attempts: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")

# USER 2 Marcus
user2 = User("Marcus", "Wallace", 35, "Greenville")
user2.describe_user()
user2.greet_user()

user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()

print(f"Login attempts: {user2.login_attempts}")

user2.reset_login_attempts()

print(f"Login attempts after reset: {user2.login_attempts}")

# USER JOHNNY 
user3 = User ("John", "Linder", 52, "Night City")

user3.reset_login_attempts()

user3.describe_user()
user3.greet_user()

user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()

print(f"Login attempts: {user3.login_attempts}")

user3.reset_login_attempts()

print(f"Login attempts after reset: {user3.login_attempts}")
