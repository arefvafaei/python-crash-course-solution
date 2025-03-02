# ---------------- 8-1
from email.message import Message


def display_message():
    print("hello my friend!")

display_message()

# ---------------- 8-2
def favorite_book(title):
    print(f"your favorite book is {title}")

favorite_book("god of war")

# ---------------- 8-3
def make_shirt(shirt_text,size):
    print(f"your text is {shirt_text} and your size is {size}")

make_shirt("hello",32)
make_shirt(shirt_text="hi",size=44)

# ---------------- 8-4
def make_shirt(shirt_text="i love phyton",size="large"):
    print(f"your text is {shirt_text} and your size is {size}")

make_shirt(size="medium")
make_shirt(size="large")
make_shirt(shirt_text="what's up?")

# ---------------- 8-5
def describe_city(city="california",country="us"):
    print(f"{city} is in {country}")

describe_city("dubai","uae")
describe_city("texas",)
describe_city()

# ---------------- 8-6
def city_country(city,country):
    print(f"{city},{country}")
city_country("tehran","iran")
city_country("california","us")
city_country("dubai","uae")

# ---------------- 8-7

songs = {}
def make_album(artist,album,number_of_songs=None):
    songs[artist] = album
    if number_of_songs != None:
        songs[album] = number_of_songs

make_album("aref","powerful",100)
make_album("aref","successful")
print(songs)

# ---------------- 8-8

active = True
songs = {}
def make_album(artist,album,number_of_songs=None):
    songs[artist] = album
    songs[album] = number_of_songs


while active:
    artists = input("enter artists name: ")
    albums = input("enter album name: ")
    number_song = input("how many songs are in this album?(n -> skip) ")
    if number_song == "n":
        make_album(artists,albums)
    else:
        make_album(artists,albums,number_song)
    activation = input("do you want to continue?(quit to out) ")
    if activation == "quit":
        active = False
print(songs)

# ---------------- 8-9
message = ["hi", "hello","how are you"]
def show_message(lists):
    print(lists)

show_message(message)

 # ---------------- 8-10
message = ["hi", "hello","how are you"]
def show_message(lists):
    print(lists)

def send_message(lists):
    print(lists)

show_message(message)
send_message(message[:])
 # ---------------- 8-11
message = ["hi", "hello","how are you"]
def show_message(lists):
    print(lists)

def send_message(lists):
    print(lists)

show_message(message)
send_message(message[:])

# ---------------- 8-12
from ctypes.macholib.dyld import dyld_default_search
from pdb import find_function


def sandwich_picker(numbers, *spices):
    print("i want ", spices)
    print(f"i want {numbers} number pizaa")


sandwich_picker(3, "salt", "pepper")
sandwich_picker(3, "salt", "pepper")
sandwich_picker(2, 'pepper')


# ---------------- 8-13
def building_profile(first, last, **info):
    info["firstname"] = first
    info["last"] = last
    return info


me = building_profile("aref", "vafaei", location="dubai", age=20)
print(me)


# ---------------- 8-14
def cars(manufacture, model_name, **kwargs):
    kwargs["model"] = model_name
    kwargs["manufacture"] = manufacture
    return kwargs


car = cars("bmw", "i8", color='blue', two_package='True')
print(car)

# ---------------- 8-15
from printing_function import printing

printing()

# ---------------- 8-16
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *


# ---------------- 8-17
def prints():
    """it just prints"""
    print("hi")


def hello():
    """it's just printing hello"""
    print("hello")


def what():
    """it's just prints what"""
    print("what")
