# # ----------- 10-1
# from pathlib import Path
#
# path = Path('learning_python.txt')
# contents = path.read_text()
# lines = contents.splitlines()
# one_line = ""
# for line in lines:
#     one_line += line
# print(one_line)
#
# # ----------- 10-2
# print(contents.replace("python", "C"))
#
# # ----------- 10-3
# from pathlib import Path
#
# path = Path('learning_python.txt')
# contents = path.read_text()
# lines = contents.splitlines()
# one_line = ""
# for line in lines:
#     one_line += line
# print(one_line)
#
# # ----------- 10-4
# from pathlib import Path
# name = input("what is your name?")
# path = Path("Guest.txt")
# path.write_text(name)
#
# # ----------- 10-5
# from pathlib import Path
#
# path = Path('guest.txt')
#
# prompt = "what's your name?(q =  quit) "
#
#
# guest_names = []
# while True:
#     name = input(prompt)
#     if name == 'q':
#         break
#
#     print(f"Thanks {name}, we'll add you to the guest.")
#     guest_names.append(name)
#
# file_string = ''
# for name in guest_names:
#     file_string += f"{name}"
#
# path.write_text(file_string)
# # ----------- 10-6
# def addiction(num_1,num_2):
#     try:
#         num_1 = int(num_1)
#         num_2 = int(num_2)
#         print(f"num 1 = {num_1} , num 2 = {num_2}")
#     except ValueError:
#         print("you must write number")
# number_1 = input("enter number one:")
# number_2 = input("enter number two:")
# addiction(number_1,number_2)
#
# # ----------- 10-7
# print("q = quit")
#
# while True:
#     try:
#         x = input("Give me a number: ")
#         if x == 'q':
#             break
#         x = int(x)
#
#         y = input("Give me another number: ")
#         if y == 'q':
#             break
#         y = int(y)
#
#     except ValueError:
#         print("Sorry, I really needed a number.")
#
#     else:
#         sum = x + y
#         print(f"The sum is {sum}.")
#
# # ----------- 10-8
# from pathlib import Path
#
# filenames = ['cats.txt', 'dogs.txt']
#
# for filename in filenames:
#     path = Path(filename)
#     try:
#         contents = path.read_text()
#     except FileNotFoundError:
#         print("  Sorry, I can't find that file.")
#     else:
#         print(contents)
#
# # ----------- 10-9
# from pathlib import Path
#
# filenames = ['cats.txt', 'dogs.txt']
#
# for filename in filenames:
#     path = Path(filename)
#     try:
#         contents = path.read_text()
#     except FileNotFoundError:
#         pass
#     else:
#         print(contents)
#
# # ----------- 10-10
# from pathlib import Path
#
# path = Path("common words.txt")
# count = path.read_text()
#
# print(count.lower().count("ali"))
#
# # ----------- 10-11
# import json
# from pathlib import Path
# favorite_number = input("what is your favorite number?")
# path = Path("favorite number.json")
# content = json.dumps(favorite_number)
# path.write_text(content)
#
# path = Path("favorite number.json")
# content = path.read_text()
# favorite_number = json.loads(content)
# print(f"your favorite number is {favorite_number}")
#
# # ----------- 10-12
# import json
# from pathlib import Path
#
# path = Path("favorite number.json")
#
# if path.exists():
#     content = path.read_text()
#     favorite_number = json.loads(content)
#     print(f"your favorite number is {favorite_number}")
# else:
#     favorite_number = input("what is your favorite number?")
#     content = json.dumps(favorite_number)
#     path.write_text(content)
#
# # ----------- 10-13
# from pathlib import Path
# import json
# user_info = {}
# path = Path("user name.json")
# def greet_user():
#     """Greet user by name"""
#     if path.exists():
#         content = path.read_text()
#         user_info = json.loads(content)
#         print(f"welcome back, {user_info}")
#     else:
#         username = input("what is your name?")
#         user_age = input("how old are you?")
#         gender = input("what is your gender?")
#         user_info['user'] = username
#         user_info['age'] = user_age
#         user_info['gender']= gender
#         content = user_info
#         print(content)
#         content = json.dumps(content)
#         path.write_text(content)
#         print(f"i will remember you {username}")
#
# greet_user()
#
# ----------- 10-14
# from pathlib import Path
# import json
#
# user_info = {}
#
# path = Path("user name.json")
# def greet_user():
#     """Greet user by name"""
#     if path.exists():
#         content = path.read_text()
#         user_info = json.loads(content)
#         print(f"welcome back, {user_info}")
#     else:
#         username = input("what is your name?")
#         user_age = input("how old are you?")
#         gender = input("what is your gender?")
#         user_info['user'] = username
#         user_info['age'] = user_age
#         user_info['gender']= gender
#         content = user_info
#         print(content)
#         content = json.dumps(content)
#         path.write_text(content)
#         print(f"i will remember you {username}")
#
# greet_user()
#
#################
# def greet_user():
#     """Greet the user by name."""
#     path = Path('username.json')
#     if username:
#         correct = input(f"Are you {username}? (y/n) ")
#         if correct == 'y':
#             print(f"Welcome back, {username}!")
#             return
#
#     print(f"We'll remember you when you come back, {username}!")
#
#

