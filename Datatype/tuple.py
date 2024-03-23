# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Accessing elements of a tuple
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])
print("Last element:", my_tuple[-1])

# Slicing a tuple
print("Slice from index 2 to 4:", my_tuple[2:5])

# Tuple unpacking
x, y, z, *rest = my_tuple
print("Unpacked values:")
print("x:", x)
print("y:", y)
print("z:", z)
print("Rest:", rest)

# Immutable nature of tuples - you can't modify them
# This would cause an error:
# my_tuple[0] = 5

# Length of a tuple
print("Length of the tuple:", len(my_tuple))

# Count occurrences of an element in a tuple
print("Number of occurrences of 'a':", my_tuple.count('a'))

# Finding the index of an element in a tuple
print("Index of 'b':", my_tuple.index('b'))
