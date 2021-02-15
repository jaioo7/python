# Python Set Methods

# Accessing set data
months={'jan','mar','feb','apl','may','jun'}
print(type(months))
print(months)

for i in months:
	print(i)

# Adding Set data
months.add('dec')
print(months)

# Adding more than one to set data
months.update(['aug','jul'])
print(months)

# Removing set data
months.remove('jan')
print(months)

# union of set, 
months1={'feb','jan','oct','sep','apl'}
print(months | months1)
print(months.union(months1))

# Intersection of set
print(months.intersection(months1))
print(months & months1)

# conversion  
lst=[1,2,3,4,5,6,1,3,4,5,6]
print(set(lst))
a=set(lst)
print(a)

#Frozenset()
lst1=[2,4,5,8,7,9,6,5,5]
print(lst1)
print(frozenset(lst1))
b=frozenset(lst1)
print(b)

c={5,7,8,9,2}
print(c)
c=frozenset(c)
print(c)