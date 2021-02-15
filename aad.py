# Python Number Mthods (int, long, float, complex)
a=10
b=25.25
c=25+8j
print(type(a))
print(type(b))
print(type(c))
# Python type conversion
# print(float(a))
# print(int(b))
# print(complex(a))
d=float(a)
print(d)
print(type(d))

d=complex(a)
print(d)
print(type(d))

e=int(b)
print(e)
print(type(e))

# abs any negative change to positive value
f=-9
print(abs(f))
# ceil  (import math )
g=2.8
import math
print(math.ceil(g))
# floor 
import math
print(math.floor(g))
# Power of (pow)
h=5
i=6
print(h**i)
print(pow(h,i))
# Maximum, Minumam, Sort (max, min, )
J=[4,5,6,9,8,7,4,3,2,1]
print(min(J))
print(max(J))
# Round (round)
k=25.365987561
print(round(k,2))
print(round(k,1))
print(round(k,3))
# sqrt 
l=24
import math
print(math.sqrt(l))
