# ------------- 9-10
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} is beautiful restaurant!")

    def open_restaurant(self):
        print(f"{self.name} is {self.cuisine_type} restaurant!")


