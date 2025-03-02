# ---------------- 6-1
person = {"first_name": "erica", "last_name": "amiran", "age": 20, "city": "new york"}

# ---------------- 6-2
favorite_numbers = {"ali": 8, "mohammad": 5, "javad": 9}
print("ali's favorite number is ", favorite_numbers["ali"])
print("mohammad's favorite number is ", favorite_numbers["mohammad"])
print("javad's favorite number is ", favorite_numbers["javad"])

# ---------------- 6-3
glossary = {"print": "show a message", "comment": "a prompt", "if": "second == 3", "else": "if", "elif": "else"}
print("print", glossary["print"])
print("\ncomment", glossary["comment"])
print("\nif", glossary["if"])
print("\nelse", glossary["else"])
print("\nelif", glossary["elif"])

# ---------------- 6-4
for key, value in glossary.items():
    print(f"{key} = {value}")

# ---------------- 6-5
rivers = {"nile": "egypt", "tahoe": "california", "eric": "ohio", "michigan": "chicago"}
for k, v in rivers.items():
    print(f"the {k} runs through {v}")

for key in rivers.keys():
    print(f"{key}")

for value in rivers.values():
    print(f"{value}")

# ---------------- 6-6
people = ["sara", "mohammad", "iman", "aref"]
favorite_language = {"sara": "pyhon", "iman": "js", "faraz": "c++"}

for people in people:
    if people in favorite_language:
        print(f"{people} thanks!")
    else:
        print(f"{people} peak a language!!!")

# ---------------- 6-7
people = {"sara":
              {"first": "sara",
               "last": "sara1",
               "age": 23},
          "aref":
              {"first": "aref",
               "last": "aref1",
               "age": 20}
          }
for person_i_know, information in people.items():
    full_name = f"{information['first']} {information['last']}"
    print(f"{person_i_know} fullname is {full_name}"
          f"\nshe/he is {information['age']} years old")

# ---------------- 6-8
pets = {"cat": {
    "name": "tom",
    "age": 3,
    "owner": "mike"},
    "dog": {
        "name": "larry",
        "age": 5,
        "owner": "aref"}
}
for pet, info in pets.items():
    print(f"{pet}\nname = {info['name']}\nage = {info['age']}\nowner = {info['owner'].title()}")

# ---------------- 6-9
favorite_places = {
    "sara": {
        "one": "us",
        "two": "uk",
        "three": "california"},
    "ali": {
        "one": "paris",
        "two": "german",
        "three": "dubai"
    }
}
for person, places in favorite_places.items():
    print(f"{person} loves {places['one'], places['two'], places['three']}")

# ---------------- 6-10
favorite_numbers = {
    "ali": {
        "one": 22,
        "two": 42,
        "three": 33},
    "aref": {
        "one": 55,
        "two": 88,
        "three": 1
    }
}
for person, favorite_numbers in favorite_numbers.items():
    print(f"{person} favorite number is {favorite_numbers['one'], favorite_numbers['two'], favorite_numbers['three']}")

# ---------------- 6-11
cities = {
    "california": {
        "country": "us",
        "population": 103000,
        "fact": "its beautiful"},
    "dubai": {
        "country": "uae",
        "population": 130000,
        "fact": "its expensive"
    }}

for cities,infos in cities.items():
    print(f"{cities.title()} country = {infos['country'].title()} population {infos['population']} people.\nfun fact = {infos['fact'].upper()}")

# ---------------- 6-12
cities = {
    "california": {
        "country": "us",
        "population": 103000,
        "fact": "its beautiful"},
    "dubai": {
        "country": "uae",
        "population": 130000,
        "fact": "its expensive"
    }}

for cities,infos in cities.items():
    print(f"{cities.title()} is in {infos['country'].title()} and has {infos['population']} people.\nfun fact = {infos['fact'].upper()}")
