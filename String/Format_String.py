#.........We know that , we can not combine string and number,But it is possiblein String format method...#

age=36
txt="my name is John,and I am {}"
print(txt.format(age))

#.........The format() method take unlimited number of arguments , and are placed into respective placeholder

quantity=3
itemno=567
price=49.95

myorder="I want {} piece of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))