# Nesting Lists,Tuples & Dictionaries
# A. Similar data structure Nesting:

# 1. List of List
a=[[1,2],[3,4],[5,6,8]]
''' single index or One -demensional index accessing'''
print(a[0])
print(a[1])
print(a[2])
''' double index or Two-dimensional index accessing'''
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1])
print(a[2][2])

# 2. Tuple of Tuple
b=((1,2),(3,4),(5,6,8))
''' single index or One -demensional index accessing'''
print(b[0])
print(b[1])
print(b[2])
''' double index or Two-dimensional index accessing'''
print(b[0][0])
print(b[0][1])
print(b[1][0])
print(b[1][1])
print(b[2][0])
print(b[2][1])
print(b[2][2])

# 3. dict of dict
d={'details':{'name':'jai','age':12},'work':{'school':'study','ground':'playing game'}}
print(d)
c={'name':'jai','age':12,'work':{'school':'study','ground':'playing game'}}
''' single index or One -demensional index accessing'''
print(c['name'])
print(c['age'])
print(c['work'])
''' double index or Two-dimensional index accessing'''
print(c['work']['school'])
print(c['work']['ground'])
print(c['work'])



# B. Disimilar data structure Nesting:

# 1. List of Tuple
e=[(1,2),(3,4),(5,6,8)]
''' single index or One -demensional index accessing'''
print(e[0])
print(e[1])
print(e[2])
''' double index or Two-dimensional index accessing'''
print(e[0][0])
print(e[0][1])
print(e[1][0])
print(e[1][1])
print(e[2][0])
print(e[2][1])
print(e[2][2])

# 2. List of dict
f=[{'name':'jai','age':25},{'name':'cherry','age':16},{'name':'nikki','age':13}]
''' single index or One -demensional index accessing'''
print(f[0])
print(f[1])
print(f[2])
''' double index or Two-dimensional index accessing'''
print(f[0]['name'])
print(f[0]['age'])
print(f[1]['name'])
print(f[1]['age'])
print(f[2]['name'])
print(f[2]['age'])

# 3. Tuple of dist
g=({'name':'jai','age':25},{'name':'cherry','age':16},{'name':'nikki','age':13})
''' single index or One -demensional index accessing'''
print(g[0])
print(g[1])
print(g[2])
''' double index or Two-dimensional index accessing'''
print(g[0]['name'])
print(g[0]['age'])
print(g[1]['name'])
print(g[1]['age'])
print(g[2]['name'])
print(g[2]['age'])

# 4. Dict of List
h={'name':['raga','lalitha','shalu'],'age':[37,25,30]}
''' single index or One -demensional index accessing'''
print(h['name'])
print(h['age'])
''' double index or Two-dimensional index accessing'''
print(h['name'][0])
print(h['name'][1])
print(h['name'][2])
print(h['age'][0])
print(h['age'][1])
print(h['age'][2])
print(h['name'][0],h['age'][0])
print(h['name'][1],h['age'][1])
print(h['name'][2],h['age'][2])

# 5. dict of tuple
i={'name':('raga','lalitha','shalu'),'age':(37,25,30)}
''' single index or One -demensional index accessing'''
print(i['name'])
print(i['age'])
''' double index or Two-dimensional index accessing'''
print(i['name'][0])
print(i['name'][1])
print(i['name'][2])
print(i['age'][0])
print(i['age'][1])
print(i['age'][2])
print(i['name'][0],h['age'][0])
print(i['name'][1],h['age'][1])
print(i['name'][2],h['age'][2])

# 6. tuple of list
j=([1,2],[3,4],[4,5,8])
''' single index or One -demensional index accessing'''
print(j[0])
print(j[1])
print(j[2])
''' double index or Two-dimensional index accessing'''
print(j[0][0])
print(j[0][1])
print(j[1][0])
print(j[1][1])
print(j[2][0])
print(j[2][1])
print(j[2][2])