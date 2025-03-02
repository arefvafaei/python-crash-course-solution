# ------------- 9-1
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} is beautiful restaurant!")

    def open_restaurant(self):
        print(f"{self.name} is {self.cuisine_type} restaurant!")


restaurant_0 = Restaurant("gol", "pizza")
restaurant_1 = Restaurant("mr.john", "italian food")

print(f"The {restaurant_1.name} is {restaurant_1.cuisine_type} restaurant")
print(f"The {restaurant_0.name} is {restaurant_1.cuisine_type} restaurant")
restaurant_0.describe_restaurant()
restaurant_1.open_restaurant()

# ------------- 9-2
restaurant_2 = Restaurant("aref", "iranian")
restaurant_3 = Restaurant("mohammad", "beef")
restaurant_4 = Restaurant("flowers", "vegetarian")


# ------------- 9-3
class User:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    def describe_user(self):
        print(f"your full name is: {self.first_name}{self.last_name}")

    def greet_user(self):
        print(f"hello {self.first_name}{self.last_name}")


user_0 = User("anna", "johnny")
user_1 = User("john", "hossein")
user_2 = User("aref", "vafaei")
user_1.describe_user()
user_2.greet_user()
print(f"firstname : {user_0.first_name} lastname : {user_0.last_name}")


# ------------- 9-4
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} is beautiful restaurant!")

    def open_restaurant(self):
        print(f"{self.name} is {self.cuisine_type} restaurant!")

    def set_number_served(self, number_served):
        self.number_served = number_served
        return number_served

    def increment_number_served(self, number_served):
        self.number_served = number_served
        return print(f"we served {number_served} a day of business!")

    def read_number_served(self):
        print(f"you served {self.number_served}!")


restaurant_0 = Restaurant("aref", "italian")
restaurant_0.read_number_served()

restaurant_0.number_served = 2
restaurant_0.read_number_served()

restaurant_0.set_number_served(8)
restaurant_0.read_number_served()

restaurant_0.increment_number_served(22)


# ------------- 9-5
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


user_0 = User("ali", "molaei")
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(user_0.login_attempts)
user_0.reset_login_attempts()
print(user_0.login_attempts)


# ------------- 9-6
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} is beautiful restaurant!")

    def open_restaurant(self):
        print(f"{self.name} is {self.cuisine_type} restaurant!")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"number of flavors: {self.flavors}")


ice_cream_stand_0 = IceCreamStand("aref", "italian", 12)
ice_cream_stand_0.display_flavors()


# ------------- 9-7
class Admin(User):
    def __init__(self, first_name, last_name, admin):
        super().__init__(first_name, last_name)
        self.admin = admin

    def show_privileges(self):
        print(f"mr.{self.last_name} can add/delete post and ban user")


admin_0 = Admin("aref", "vafaei", True)
admin_0.show_privileges()


# ------------- 9-8
class Admin(User):
    def __init__(self, first_name, last_name, admin):
        super().__init__(first_name, last_name)
        self.admin = admin
        self.privileges = Privileges()

    def show_privileges(self):
        print(f"mr.{self.last_name} can add/delete post and ban user")


class Privileges:
    def __init__(self):
        self.privileges = ["can ban", "can send message", "ETC"]

    def show_privileges(self):
        print(self.privileges)


test = Admin("morteza", "mohammadi", True)
test.privileges.show_privileges()


# ------------- 9-9
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_describe_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # Create an instance of Battery


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        self.battery_size = 65
        self.get_range()


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_describe_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()

# ------------- 9-13
from random import randint, random, choice


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


six_side = Die()
for _ in range(10):
    print(f"6 side roll: {six_side.roll_die()}")
print(28 * "--")

six_side = Die(10)
for _ in range(10):
    print(f"10 side roll: {six_side.roll_die()}")
print(28 * "--")

six_side = Die(20)
for _ in range(10):
    print(f"20 side roll: {six_side.roll_die()}")

# ------------- 9-14
lottery = ["233j", "e393h", "938ejj", "ej3emi9"]
winner = choice(lottery)
print(winner)

# ------------- 9-15
count = 0
while True:
    i = randint(1, 1000)
    count = count + 1
    if i == 400:
        break
print(count)

# ------------- 9-16
# just do it!
