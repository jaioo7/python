# Python  Tupnle Methods
tp=(5,8,9,69, 'jai',5.9)
tp1=(5,7,8,9,3,1,4,5,6,8)

# Iteration
for t in tp:
	print(t)

# Tuple Indexing & Tuple Slicing ([])	
print(tp[0])
print(tp[-1])
print(tp[0:4])

# Tuple lengh, Maximum,minumum 
print(len(tp))
print(max(tp1))
print(min(tp1))

# Repetition (*)
print(tp*3)

# Concatenation (+)
print(tp+tp1)

# Membership (in, not in)
print('jai' in tp)
print('jai' in tp1)
print('jai' not in tp)
print('jai' not in tp1)

# sequence 
lst=[2,4,5,8,7,6,9,2.5,True,False,'jai']
print(tuple(lst))

'''
int()
float()
str()
tuple()
list()
dict()
'''