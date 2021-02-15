# Python List Methods
lst=[4,3,5,6,7,8,9]
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])
print(lst[5])
print(lst[6])
for l in lst:
	print(l)
print(lst[2:7])
lst[1]=99
print(lst)
del lst[0]
print(lst)
lst1=['jai','sankaru','bandaru']
lst1.insert(0,'Jai')
print(lst1)
# Repetition
lst2=[2,3,4,5]
print(lst2*3)
lst3=[5,6,7,8]
print(lst2+lst3)
#membership  (in, not in)
print (9 in lst3)
print(9 not in lst3)

print(len(lst3))
print(max(lst3))
print(min(lst3))

print(tuple(lst3))

lst4=[25,35,45,'jai']
lst4.append('sankaru')
print(lst4)

lst4.clear()
print(lst4)

lst5=[25,35,45,'jai',55,65]
lst5.remove('jai')
print(lst5)
del lst5[0]
print(lst5)

lst6=[25,35,45,55,65,75,85]
lst6.reverse()
print(lst6)
print(lst6.sort())
print(lst6)