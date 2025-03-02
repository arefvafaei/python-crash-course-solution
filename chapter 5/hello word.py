# -----------------5-1

car = "bmw"
print("is car=='bmw'? i predict true ")
print("is car=='benz'? i predict false ")
fruit = "apple"
print("is fruit=='banana'? i predict false ")
print("is fruit=='apple'? i predict true ")
country = "us"
print("is country=='us'? i predict ture ")
print("is country=='canada'? i predict false ")
city = "new york"
print("is city=='new york'? i predict true ")
print("is city=='mexico city'? i predict false ")
phone = "apple"
print("is phone=='apple'? i predict true ")
print("is phone=='samsung'? i predict false ")

# -----------------5-2
string = "blue"
print(string == "white")
string = "blue"
print(string == "blue")

apple = "Apple"
print(apple.title() == apple)
apple = "Apple"
print(apple.lower() == apple)

print(5 >= 3)
print(5 <= 3)
print(5 < 3)
print(5 > 3)

print((2 > 4 and 3 == 7) == True)
print((2 > 3 or 3 == 7) == True)

names = ["john", "mohammad ", "ali"]
print("ali" in names)
print("sara" in names)

# -----------------5-3
alien_color = "green"
alien_color_fail = "yellow"
if alien_color == "green":
    print("you just earned one point")

# -----------------5-4
alien_color = "green"
if alien_color == "green":
    print("player just earn 5 points for shooting an alien")
else:
    print("player just earn 10 points")

if alien_color == "yellow":
    print("you meet final boss!!!")
else:
    print("you failed!")

# -----------------5-5
alien_color = "green"
if alien_color == "green":
    print("the player earned 5 points!!")
elif alien_color == "yellow":
    print("the player earned 10 points!!")
elif alien_color == "red":
    print("the player earned 5 points!!")

print("one " * 20)

alien_color = "black"
if alien_color == "black":
    print("the player earned 5 points!!")
elif alien_color == "white":
    print("the player earned 10 points!!")
elif alien_color == "blue":
    print("the player earned 5 points!!")

print("two " * 20)

alien_color = "black"
if alien_color == "black":
    print("the player earned 8 points!!")
elif alien_color == "white":
    print("the player earned 11 points!!")
elif alien_color == "blue":
    print("the player earned 15 points!!")

print("three " * 20)

alien_color = "black"
if alien_color == "black":
    print("the player earned 5 points!!")
elif alien_color == "red":
    print("the player earned 10 points!!")
elif alien_color == "purple":
    print("the player earned 5 points!!")

# -----------------5-6
age = 49
if age < 2:
    print("you are a baby!")
elif 2 <= age < 4:
    print("you are a toddler")
elif 4 <= age < 13:
    print("you are a kid!")
elif 13 <= age < 20:
    print("you are a teenage!")
elif 20 <= age < 65:
    print("you are a adult!")
elif age > 65:
    print("you are a elder!")

# -----------------5-7
favorite_fruits = ["banana", "apple", "carrot"]
if "banana" in favorite_fruits:
    print("you like banana!")
elif "coconut" in favorite_fruits:
    print("you like coconut!")

# -----------------5-8
usernames = ["mike", "admin", "john", "mohammad"]
for username in usernames:
    if "admin" in username:
        print("Hello admin\nWould you like to see some reports?")
    else:
        print(f"Welcome back {username}")

# -----------------5-9
usernames.clear()
if usernames:
    print("Hello guys!")
else:
    print("The list is empty")

# -----------------5-10
current_users = ["ali", "mohammad", "john", "sara"]
new_users = ["elon", "ALI", "sara", "alex"]
current_users_lower = []
new_users_lower = []
for current_users in current_users:
    current_users_lower.append(current_users.lower())
for new_users in new_users:
    new_users_lower.append(new_users.lower())

for new_users_lower in new_users_lower:
    if new_users_lower in current_users_lower:
        print(f"{new_users_lower} you should change your username!!")
    else:
        print(f"{new_users_lower} your username is valid.")

# -----------------5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numbers in numbers:
    if numbers == 1:
        print(f"\n{numbers}st")
    if numbers == 2:
        print(f"\n{numbers}nd")
    if numbers >= 3:
        print(f"\n{numbers}rd")

# -----------------5-12
# all done

# -----------------5-13
# wow



