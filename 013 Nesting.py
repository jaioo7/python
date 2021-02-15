#Similar Data Structure Nesting:

# list of lists
a=[[1,2],[3,4],[5,6]]
""" Single index or One-dimensional index accessing """
print(a[0])
print(a[1])
print(a[2])
""" Double index or Tow-dimensional index accessiong"""
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1])

#Tuple of Tuples
b=((1,2),(3,4),(5,6))
""" Single index or One-dimensional index accessing """
print(b[0])
print(b[1])
print(b[2])
""" Double index or Tow-dimensional index accessiong"""
print(b[0][0])
print(b[0][1])
print(b[1][0])
print(b[1][1])
print(b[2][0])
print(b[2][1])

# Dict of Dicts
c={'name':'siva','age':19,'work':{'school':'study','ground':'playing'}}
""" Single index or One-dimensional index accessing """
print(c['name'])
print(c['age'])
print(c['work'])
""" Double index or Tow-dimensional index accessiong"""
print(c['work']['school'])
print(c['work']['ground'])

#List of Tuple
d=[(1,2),(3,4),(5,6)]
""" Single index or One-dimensional index accessing """
print(d[0])
print(d[1])
print(d[2])
""" Double index or Tow-dimensional index accessiong"""
print(d[0][0])
print(d[0][1])
print(d[1][0])
print(d[1][1])
print(d[2][0])
print(d[2][1])

#List of Dict,s
e=[{'name':'sriram','age':29},{'name':'siva','age':25},{'name':'lalitha','age':26}]
""" Single index or One-dimensional index accessing """
print(e[0])
print(e[1])
print(e[2])
""" Double index or Tow-dimensional index accessiong"""
print(e[0]['name'])
print(e[0]['age'])
print(e[1]['name'])
print(e[1]['age'])
print(e[2]['name'])
print(e[2]['age'])

#Tuple of Lists
f=([1,2],[3,4],[5,6])

""" Single index or One-dimensional index accessing """
print(f[0])
print(f[1])
print(f[2])
""" Double index or Tow-dimensional index accessiong"""
print(f[0][0])
print(f[0][1])
print(f[1][0])
print(f[1][1])
print(f[2][0])
print(f[2][1])

#Tuple of Dict's
g=({'name':'sriram','age':29},{'name':'siva','age':25},{'name':'lalitha','age':26})
""" Single index or One-dimensional index accessing """
print(g[0])
print(g[1])
print(g[2])
""" Double index or Tow-dimensional index accessiong"""
print(g[0]['name'])
print(g[0]['age'])
print(g[1]['name'])
print(g[1]['age'])
print(g[2]['name'])
print(g[2]['age'])

#Dict's of List
""" Single index or One-dimensional index accessing """
h={'name':['sriram','siva','lalitha'],'age':[29,25,26]}
print(h['name'])
print(h['age'])
""" Double index or Tow-dimensional index accessiong"""
print(h['name'][0])
print(h['name'][1])
print(h['name'][2])
print(h['age'][0])
print(h['age'][1])
print(h['age'][2])

#Dict's of Tuple
""" Single index or One-dimensional index accessing """
h={'name':('sriram','siva','lalitha'),'age':(29,25,26)}
print(h['name'])
print(h['age'])
""" Double index or Tow-dimensional index accessiong"""
print(h['name'][0])
print(h['name'][1])
print(h['name'][2])
print(h['age'][0])
print(h['age'][1])
print(h['age'][2])