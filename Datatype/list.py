# .................................LIST..................................
# 1-create empty list
# 2-list with some values
# 3-indexing
# 4-slicing
# 5-count list items
# 6-append
# 7-pop
# 8-insert
# 9-extend
# 10-sort
# 11-reverse
# 12-Nested list
# 13-list comprehension
# 14-copy
# 15-length of list





list1=[]

print(type(list1))#list(empty list)

list2=[10,'ankit',True,10.6,'ankush',10]
print(list2)

#-----------create list using function------------#

list3=list()
print(type(list3))

#------------indexing in python---------------#

print(list2[1])#--O/P-ankit---#

#------------list slicing-----------------#

print(list2[1:4])#--O/P-['ankit', True, 10.6]---#

#---------count frequnecy of element------#

print(list2.count('ankit'))
print(list2.count(10))
print(list2.count(20))
print(list2.count(10.6))
#-------------index------------------#

print(list2.index(10.6))
print(list2.index(10))
print(list2.index('ankit'))
print(list2.index(10,1))#----O/P-5-----

#---------------insert(add element at particular postion)----------------

list2.insert(2,"Ashish")
print(list2)

#---------------pop(delete 1 element at only end)--------------

list2.pop()
print(list2)

#--------------extend-------------

list3=["Ram","Shyam"]
list2.extend(list3)
print(list2)

#-------------copy----------------

list3=list2.copy()
print(list3)

list4=list2[:]
print(list4)

#-------------sort(ascending to descending)----------------

list5=[10,0,8,34,20]

list5.sort()
print(list5)

#-------------sort(descending to ascending)----------------

list5.sort(reverse=True)
print(list5)

#-------------reverse----------------------

list6=[10,0,8,34,20]
list6.reverse()
print(list6)

#-------------print list element with specific condition-----------#

list2=["ankush","ankit","noman","rohit"]

a = [word for word in list2 if word.startswith("a")]
print(a)

list2=["ankush","ankit"]
n1,n2=list2
print(n1)
print(n2)

