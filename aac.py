#python Arithmatic operators ( +, -, /, //, *, **, %,)

a=5
b=2
# Addition  operator (+)
print(a+b)
# Subtraction operator (-)
print(a-b)
# Division operator (/)
print(a/b)
# Floor Dvision operator (//)
print(a//b)
# Multiplication operator (*)
print(a*b)
# Exponent operator (**) Power of
print(a**b)
# Remainder operator (%)
print(a%b)

# Python Comparison Operators ( ==, !=, <=, >=, <>, >, <) (Result True or Flase)
c=30
d=20
# Equel to (==)
print(c==d)
# Not Equel to (!=)
print(c!=d)
# Less than (<)
print(c<d)
# Greater than (>)
print(c>d)
# Greater than or Equel to (>=)
print(c>=d)
# Less than or Equel to (<=)
print(c<=d)

#Pythn Assignment Operators( =, +=, -=, *=, %=, **=, //=)
e=9
f=2
print(e+f)
e += f 		 # e= e+f
print(e)
print(e-f)
e -= f 		 # e= e-f
print(e)
print(e*f)
e *= f 		 # e= e*f
print(e)
print(e**f)
e **= f 		 # e= e**f
print(e)
print(e//f)
e //= f 		 # e= e//f
print(e)
print(e%f)
e %= f 		 # e= e%f
print(e)

# PYthon Logical Operators (and &, or |,)
f=50
g=70
h=60
print((f>g)&(f>h))
print((f>g)|(f>h))
print((f<g)&(f<h))
print((f<g)|(f<h))

# Bitwise operator
print(f & g)
print(bin(f&g))

#Python Membershiip Operators ( in, not in)
i=10
j=[20,30,40,50,60]
print(i in j)
print(i not in j)

#Python Identity Operators ( is, is not)
k=10
l=10
m=20
print(id(k))
print(id(l))
print(id(m))
print(k is l)
print(k is m)
print(k is not l)
print(k is not m)