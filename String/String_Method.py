#---------String are Arrays-----------

a="Hello, world!"
print(a[1])

#Looping Through a String
#Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
    print(x)

#...............String length......................

a="Hello World"
print(len(a))

#.............Check String...............
#To check if a certain phrase or character is present in a string, we can use the keyword in.

txt="The best thing in life is free"
print("free" in txt)

txt="The best thing in life are free"
if "free" in txt:
    print("yes,free is present")
else:
    print("No, free is not present")