#You can return a range of characters by using the slice syntax.

b="Hello, World!"
print(b[2:5])

#Slice from start 
#Get the characters from the start to position 5 (not included):

b="Hello World!"
print(b[:5])

#Slice To the End
#By leaving out the end index, the range will go to the end:

b="Hello World!"
print(b[2:])

#Negative Indexing
#Use negative indexes to start the slice from the end of the string:

b="Hello,World!"
print(b[-5:-2])

