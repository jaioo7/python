 #3 operators
#relationall operators, arthmetic operators, logical operators
#arthmetic operators (+, -, /, *, %, //, **)
#Assignment Operators ( =, +=, -=, *=, /=, %=, //=, **=)
# Logical Operators( and, or, not)
#Bitwise Operators ( &, |, ~, ^, <<, >>)
# ex

'''a=10
b=20
print(a)
print(a+b)
print(a-b)
print(a/b)
print(a*b)

#relational operators (<, >, ==, !=, >=, <=, <>)
print(a,b)
print(a<b)
print(a>b)
print(a==b)
print(a!=b)

#logical operators  ( &, |) (and, or, not)
a= True
b= False
print (a&b)
c=False
d=True
print(c&d)
e=False
f=False
print(e&f)
g=True
h=True
print(g&h)
i=True
j=False
print(i|j)
k=False
l=True
print(k|l)
m=False
n=False
print(m|n)
o=True
p=True
print(o|p)'''

a=20
b=10
# Python Arithmetic Operators
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)
print(a//b)
print(a**b)
# Python Comparison Operators
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a<b)
print(a>b)
# Python Assignment Operators

#a += b  # a = a+b
print(a)
#a -= b  # a = a-b
print(a)
#a *= b  # a = a*b
print(a)
#a /= b  # a = a/b
print(a)
#a %= b  # a = a%b
print(a)
#a **= b  # a = a**b
print(a)
a //= b  # a = a//b
print(a)

# Python Logical Operators
x=10
y=20
z=30
print((x<y) & (x<z))
print((y<x) and (y<z))
print((z<x) & (z<y))
print((x>y) and (x>z))
print((y>x) & (y>z))
print((z>x) and (z>y))
print((x<y) | (x<z))
print((y<x) or (y<z))
print((z<x) | (z<y))
print((x>y) or (x>z))
print((y>x) | (y>z))
print((z>x) or (z>y))
v=True
u=False
print(not(v))
print(not(u))

#Python Membership Operators tuple(), List[]
a=[25,35,45,65,55,75]
print(25 in (a))
print(33 in (a))
print(25 not in (a))
print(33 not in (a))

#Python Identiry Operators 
a=10
b=10
print(id(a))
print(id(b))
print(a is b)
print(a is not b)
x=10
y=20
print(id(x))
print(id(y))
print(x is y)
print(x is not y)

#Python Type Conversion
a=56 #Integer data type
print(type(a))
print(float(a))
print(complex(a))
b=8.4 #float data type
print(type(b))
print(int(b))
print(complex(b))
#Complex data type (didn't chamge int, float,data)
c=5+6j
print(type(c)) 

# Function or Method Description
# abs (-) value cange (+)
a=-9
print(abs(a))
# cell is next higher value indicate (import math) function
b=5.8
import math
print(math.ceil(b))
# floor is next higher value indicate (import math) function
b=5.8
import math
print(math.floor(b))
#pow mean **
print(pow(5,3))
print(5**3)
#min, Max
c=(45,25,3,69,78,85,99)
print(min(c))
print(max(c))
# Round
d=25.235698875
print(round(d,2))
# Sqrt math fanction used (import math) function
e=16
import math
print(math.sqrt(e))