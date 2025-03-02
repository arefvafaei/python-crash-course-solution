# ------------7-1
car = input("what car do you want: ")
if car == "bmw":
    print(f"here is your {car}")
else:
    print("sorry we don't have!")

# ------------7-2
dinner_table = int(input("how many people are in your dinner group?"))

if dinner_table >= 8:
    print("sorry there is no table!")
else:
    print("your table is ready!")

# ------------7-3
message = int(input("Enter a number: "))
if message % 10 == 0:
    print("it's a multiple of 10")
else:
    print("number is not multiple of ten!")

------------7 - 4
while 1 == 1:
    topping = input("what do you want?(write done to end)")
    if topping == "done":
        break
    print(f"{topping} added to your list.")

# ------------7-5
while True:
    age = int(input("how old are you?"))
    if age <= 3:
        print("your ticket is free!")
    elif 3 < age <= 12:
        print("12 dollars please")
    else:
        print("15 dollars please!")

# ------------7-6
while 1 == 1:
    topping = input("what do you want?(write done to end)")
    if topping == "quit":
        break
    print(f"{topping} added to your list.")

while True:
    age = int(input("how old are you?"))
    if age == "quit":
        break
    age = int(age)
    if age <= 3:
        print("your ticket is free!")
    elif 3 < age <= 12:
        print("12 dollars please")
    else:
        print("15 dollars please!")

# ------------7-7
while 1 == 1:
    print("hello")

# ------------7-8
sandwich_order = ["berger", "chicken burger", "rat burger"]
finished_sandwiches = []
while sandwich_order:
    sandwich = sandwich_order.pop()
    finished_sandwiches.append(sandwich)
    print(f"your {sandwich} is ready!")

print(finished_sandwiches)

# ------------7-9
sandwich_order = ["pastrami", "berger", "pastrami", "chicken burger", "rat burger", "pastrami"]
print("out of pastrami")
while "pastrami" in sandwich_order:
    sandwich_order.remove("pastrami")
finished_sandwiches = []
while sandwich_order:
    sandwich = sandwich_order.pop()
    finished_sandwiches.append(sandwich)
    print(f"your {sandwich} is ready!")

print(finished_sandwiches)

# ------------7-10
activation = True
user_list = {}
while activation:
    name = input("what is your name?")
    location = input("where do you want to go?")
    question = input("do you want to continue?y/n")
    user_list[name] = location
    if question == "n":
        activation = False
print(user_list)
for k, v in user_list.items():
    print(f"{k} you will visit {v} soon!")
