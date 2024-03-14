#...............Different type datatype
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType """

#.......1......

x="Hello World"
print(type(x))

#.......2......

x=20
print(type(x))

#.......3......

x=20.5
print(type(x))

#.......4......

x=1j
print(type(x))

#.......5......

x=["apple","Bnana","Orange"]
print(type(x))

#.......6......

x=("apple","banana","Cherry")
print(type(x))

#.......7......

x=range(6)
print(type(x))

#.......8......

x={"name":"jhon","age":36}
print(type(x))

#.......9......

x={"apple","banana","cherry"}
print(type(x))

#.......10......

x=frozenset(("apple","banana","cherry"))
print(type(x))

#.......11......

x=True
print(type(x))

#.......12......

x=b"Hello"
print(type(x))

#.......13......

x=bytearray(5)
print(type(x))