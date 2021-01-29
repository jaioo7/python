#variables
#string, int flot bool
#operators tuple(),list[],Dictionary{},set{},
# if else elif
a=10
b=20
c=30
if (a>b)&(a>c):
	print("A is Greatest")
elif (b>a)&(b>c):
	print("B is Greatest")
else:
	print("C is Greatest")
# if else with tuple
A=(1,2,3,4,5)
if 8 in A:
	print("8 is present")
else:
	print("8 is not present")
#if else with list
B=['a','b','c','d']
if B[3]==("d"):
	B[3]=250
	print(B)