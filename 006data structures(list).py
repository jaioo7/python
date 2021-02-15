#  #list in python
# #list is an ordered collection of elements enclosed within []
# #list are mutable
# l1=[1, 'a', True]
# print(type(l1))
# print(l1)
# print(l1[0])
# print(l1[1])
# print(l1[2])

# l1[0]=100
# print(l1)
# l1[-1]=False
# print(l1)
# l1[1]=False
# print(l1)

# #extracting individual elements
# l2=['a', 1, 'b', 2, 'c', 3,]
# print(l2[2])
# print(l2[1:5])

# #modifing a list
# # changeing the element of ___ index
# print(len(l2))
# print(l2)
# print(l2)
# l2[1]=5
# print(l2)
# l2[3]='jai'
# l2[4]='jai',
# print(l2)
# #popping the last element_____ pop()
# l3=[2,5,4,9,8,6,3,4]
# print(l3)
# l3.pop()
# print(l3)
# #appending a new element_______append()
# l3.append("jai")
# print(l3)
# l3.pop()
# print(l3)
# print(l3.pop()),print(l3.pop()),print(l3.append("jaisankaru"))
# print(l3)

# #modifying a list
# #Reversing elements of list
# l4=[1, 'a', 2, "b", 3, 'c']
# print(l4)
# l4.reverse()
# print(l4)

# #Inserting element at a specified index
# l4.reverse()
# print(l4)
# l4.insert(1,'cherry')
# print(l4)
# l4.insert(5, "nikki")
# print(l4)

# #sorting a list
# l5=["mango","banana","apple","guava","orange"]
# print(l5)
# l5.sort()
# print(l5)
# l6=["jai","sankaru","bandaru","cherry","nikki"]
# l6.sort()
# print(l6)
# del l6[0]
# print(l6)


a=[2,5,6,8,9,7,5,3,4,6]
print(len(a))
print(max(a))
print(min(a))
a.pop()
print(a)
a.append('jai')
print(a)
a.pop()
print(a)
a.reverse()
print(a)
a.sort()
print(a)
print(a[2:8])
a.insert(2,'sankaru')
print(a)
a[1]=100
print(a)
print(3 in a)
print(9 not in a)
print(9 in a)
print(3 not in a)
for jai in a:
	print(jai)
b=(4,5,6,7)   #tuple to change list
print(list(b))
c=[25,35,45,55,65,75]
c.clear()
print(c)
d=[11,22,33,44,55,66,77,88]
#e=d.copy()
e=d
print(e)
d.remove(11)
print(d)
del d[-1]
print(d)
print(tuple(d))