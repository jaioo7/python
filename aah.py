# Python Dictionary Methods {}
dt={'name':'jai','age':25,'salary':125000,'company':'google'}
print(type(dt))

# Accessing Dictionary Data:
print(dt['name'])
print(dt['age'])
print(dt['salary'])
print(dt['company'])

# Updating Dictionary Data
dt["name"]='sankaru'
print(dt)

# Dictionary keys() values()
print(dt.keys())
print(dt.values())

# Deleting Dictionary  data
del dt['age']
print(dt)

# Iterating Dictionary dta
for i in dt:
	print(i)

for i in dt.values():
	print(i)

for i in dt.items():
	print(i)

for i,j in dt.items():
	print(i,j)
	print(i)
	print(j)

# dict(clear())
dt1={'name':'jai','age':25,'salary':125000,'company':'google'}
dt1.clear()
print(dt1)

# dict(copy())
dt1={'name':'jai','age':25,'salary':125000,'company':'google'}
b=dt1.copy()
print(b)

# dict(items())
dt1={'name':'jai','age':25,'salary':125000,'company':'google'}
b=dt1.items()
print(b)
# dict(items())
dt1={'name':'jai','age':25,'salary':125000,'company':'google'}
dt1.items()
print(dt1)

# dict(values())
dt1={'name':'jai','age':25,'salary':125000,'company':'google'}
d=dt1.values()
print(d)
# dict(values())
dt1={'name':'jai','age':25,'salary':125000,'company':'google'}
print(dt1.values())

# dict(keys())
dt1={'name':'jai','age':25,'salary':125000,'company':'google'}
d=dt1.keys()
print(d)
# dict(keys())
dt1={'name':'jai','age':25,'salary':125000,'company':'google'}
print(dt1.keys())

# updating 
dt2={'nam':'sankaru','ag':45,'salar':150000,'compan':'microsoft'}
dt1.update(dt2)
print(dt1)

#list of list nesting 
lst=[['name','jai'],['work','it']]
k=dict(lst)
print(k)
#tuple of tuple
tup=(('name','jai'),('work','it'))
l=dict(tup)
print(l)