#........There are 3 types of number in python.........
#   1. int  2. float 3.complex

#Int
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x=1
y=356214532484211421646
z=-156415

print(type(x))
print(type(y))
print(type(z))

# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x=1.0
y=1.10
z=-35.67

print(type(x))
print(type(y))
print(type(z))

x=35e3
y=12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#Complex
#Complex numbers are written with a "j" as the imaginary part

x=3+5j
y=5j
z=-5j

print(type(x))
print(type(y))
print(type(z))

#...........Type coversion..............

#Note: You cannot convert complex numbers into another number type.

#............Random Number............
import random

print(random.randrange(1,100))

