#-----------type-1------------

x=5
y="john"
print(x)
print(y)

#-----------type-2------------

x=4
x="sally"
print(x)

#------------Casting-----------

x=str(3)
y=int(3)
z=float(3)

print(x +" "+str(y)+" "+str(z))

#---------different type of a variable with type() function

x=5
y="jhon"
print(type(x))
print(type(y))

#-----------Multi Word variable name----------------#

#.....1.......(Camel Case)->Each word except first , start with capital letter

myVaribaleName="Jhon"

#.....2.......(Pascal Case)->Each word start with capital letter 

myVaribaleName="Jhon"

#.....3.......(Snake Case)->Each word is separated by an underscore

my_varibale_name="jhon"


#-----------------------------Assign mutiple values -----------------------
#.......many values to multiple varibales................

x,y,z="Orange","Apple","Banana"

print(x)#.....Orange
print(y)#.....Apple
print(z)#.....Banana

#......One value to multiple varibale................

x=y=z="Orange"

print(x)
print(y)
print(z)