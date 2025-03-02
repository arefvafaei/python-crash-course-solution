# ------------------4-1
from PIL.ImImagePlugin import number
from Tools.scripts.summarize_stats import print_title

pizzas = ["Pepperoni pizza", "Vegetable pizza", "Italian pizza"]
for i in pizzas:
    print(f"i love {i}")
print("\ni can eat pizza every day!")

# ------------------4-2
animals = ["lion", "cat", "chita"]
for animals in animals:
    print(f"{animals} can run fast!")
print("\nfelines")

# ------------------4-3
for number in range(1, 21):
    print(number)

# ------------------4-4
# numbers = list(range(1, 1000001))
# for numbers in numbers:
# print(numbers)

# ------------------4-5
summing_a_million = list(range(1, 1000001))
print(min(summing_a_million))
print(max(summing_a_million))
print(sum(summing_a_million))

# ------------------4-6
odd_number = list(range(1, 20, 2))
for odd_number in odd_number:
    print(odd_number)

# ------------------4-7
threes = []
for i in range(3, 30):
    threes.append(i ** 3)
for threes in threes:
    print(threes)

# ------------------4-8
for cubes in range(1, 10):
    cubes = cubes ** 3
    print(cubes)

# ------------------4-9
print_cubes = []
for cubes in range(1, 10):
    print_cubes.append(cubes ** 3)
print(print_cubes)

# ------------------4-10
slices_first = []
for slices_first in print_cubes[:3]:
    print(f"i love {slices_first} number")

slices_middle = []
for slices_middle in print_cubes[1:4]:
    print(f"i love {slices_middle} number")

slices_end = []
for slices_end in print_cubes[4:]:
    print(f"i love {slices_end} number")

# ------------------4-11
friend_pizzas = pizzas[:]
pizzas.append("american pizza")
friend_pizzas.append("cheese pizza")
print(pizzas)
print(friend_pizzas)

# ------------------4-12
my_foods = ["pizza", "falafel", "carrot cake"]
friend_food = my_foods[:]
print("my favorite foods are:")
for my_foods in my_foods:
    print(my_foods)
print("my friend's favorite foods are:")
for friend_food in friend_food:
    print(friend_food)

# ------------------4-13
buffet = ("chess", "egg", "sandwich", "cake", "rice")
for buffet in buffet:
    print(buffet)
# buffet[0]= "kebab"
print("new menu")
buffet = ("kebab", "egg", "sandwich", "chicken", "rice")
for buffet in buffet:
    print(buffet)

# ------------------4-13
# https://python.org/dev/peps/pep-0008

# ------------------4-13
#???????