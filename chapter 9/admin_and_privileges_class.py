# ------------- 9-12
from user_class import User
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

admin_2 = Admin("melika","hassani",True)
admin_2.show_privileges()