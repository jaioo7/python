#set
a={4,5,7,8,96,5,45,45,6,2,8,4,5,1,6,True,False,}
print(a)
print(len(a))
print(max(a))
print(min(a))
print(a)
b={4,58,7,8,7,855,5,6,4,5,2,3,1,89}
print(a.intersection(b))
print(a.union(b))
b.remove(855)
b.add(5555)
print(b)
b.update([222,555,999])
print(b)