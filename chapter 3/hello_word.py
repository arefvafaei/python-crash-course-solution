# -------------------3-1
friends = ["sara", "ali", "aref", "mohammad"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

# -------------------3-2
friends = ["sara", "ali", "aref", "mohammad"]
print("hello ", friends[0])
print("hello ", friends[1])
print("hello ", friends[2])
print("hello ", friends[3])

# -------------------3-3
transportation = ["bike", "buss", "train"]
print(f"I have a {transportation[0]}")
print(f"My dad has a {transportation[1]}")
print(f"I love a {transportation[2]}")

# -------------------3-4
invitation = ["sara", "ali", "john"]
print(f"hello {invitation[0]} please join my party at 12am")
print(f"hello {invitation[1]} please join my party at 12am")
print(f"hello {invitation[2]} please join my party at 12am")

# -------------------3-5
print("ALI CAN NOT COME")
invitation[1] = "alice"
print(f"hello {invitation[1]} please join my party at 12am")

# -------------------3-6
print("REZA IMAN MOHAMMAD2 ARE MY NEW GUESTS")
invitation.insert(0, "reza")
invitation.insert(3, "iman")
invitation.append("mohammad2")
print(f"hello {invitation[0]} please join my party at 12am")
print(f"hello {invitation[3]} please join my party at 12am")
print(f"hello {invitation[5]} please join my party at 12am")

# -------------------3-7
print("sorry guys i have only two spaces")
print(f"sorry {invitation[5]} you can't join us")
invitation.pop()
print(f"sorry {invitation[4]} you can't join us")
invitation.pop()
print(f"sorry {invitation[3]} you can't join us")
invitation.pop()
print(f"sorry {invitation[2]} you can't join us")
invitation.pop()
del invitation[1]
del invitation[0]
print(invitation)

# -------------------3-8
places = ["tehran", "oman", "persian gulf", "dubai", "thailand"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

# -------------------3-9
print(len(places))

# -------------------3-10
things_i_love = ["my self", "my body", "uae", "persian gulf"]
print(f"i love {things_i_love[0]} alot!")
print(f"i love {things_i_love[1]} alot!")
print(f"i love {things_i_love[2]} alot!")
print(f"i love {things_i_love[3]} alot!")
things_i_love[3] = "my family"
print(f"i love {things_i_love[3]} alot!")
things_i_love.insert(2, "my_brain")
things_i_love.append("my parents")
print(things_i_love)
things_i_love.pop()
del things_i_love[3]
print(things_i_love)
things_i_love.reverse()
print(things_i_love)
things_i_love.sort()
print(things_i_love)
things_i_love.sort(reverse=True)
print(things_i_love)

# -------------------3-11
# print(things_i_love[4]) ///just delete # and you are good  to go

