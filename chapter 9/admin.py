# ------------- 9-11
class User:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"your full name is: {self.first_name}{self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts = 1 + self.login_attempts
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        print(f"hello {self.first_name}{self.last_name}")

class Admin(User):
    def __init__(self, first_name, last_name, admin):
        super().__init__(first_name, last_name)
        self.admin = admin

    def show_privileges(self):
        print(f"mr.{self.last_name} can add/delete post and ban user")

class Privileges:
    def __init__(self):
        self.privileges = ["can ban", "can send message", "ETC"]

    def show_privileges(self):
        print(self.privileges)



