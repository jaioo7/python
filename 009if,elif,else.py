# if, elif, else statement
a=10
b=20
if b>a:
	print("B is greatar than A")

A=10
B=20
if A>B:
	print("A is Greatar than B")
else:
	print("B is Greatar than A")
C=30
if (A>B) & (A>C):
	print("A is the Greatest")
elif (B>A) & (B>C):
	print("B is the greatest")
else:
	print("C is the Greatest")

	#If else with tuple
tup=("a","b","c",)
if "a" in tup:
	print("A is present")
if "d"	in tup:
	print("D is present")
else:
	print("D is not Present")

#If with list
list1=['a','b','c']
if list1[0]=='a':
	list1[0]="jai"
print(list1)
