#data structures set in python
# set is an unordered and unindexed collection of elements enclosed with    {}
#Duplicates are ot allowed in set
s={1,1,1,2,2,2,3,3,3,3,4,4,4,4,}
print(s)
print(type(s))
#update one dictionary's elementss with another
s1={1,'a', True, 2, 'b',False}
print(s1)
s1.add('Hello')
print(s1)
#Removing an element
s1.remove('a')
print(s1)
#Updating multiple elements
s1.update([25,35,45, 3+56j])
print(s1)
#set functions
#union of two sets 
s2={1,2,3,4,5,6}
s3={'a','b','c','d','e','f'}
print(s2.union(s3))
print(s2)
print(s3.union(s2))
#intersection of two sets
s4={1,2,3,4,5,6,7,8,9}
s5={4,5,6,7,8,9,10,11,12}
print(s4.intersection(s5))