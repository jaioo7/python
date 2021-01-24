# Dictionary in Python
#Dictionary is an unordered collection of key-value pairs enclosed with _____ {}
#Diction is mutable
fruits={"apple":10,"orang":58, "banana":60}
print(fruits)
#extracting keys
print(fruits.keys())
#extracting values
print(fruits.values())
#adding a new element
fruits["mango"]=90
print(fruits)
#changing an existing element
fruits["apple"]=250
print(fruits)
#update one dictinary's elements with another
fruit1={"apple":40,'orange':30, 'banana':60}
fruit2={'guova':45, 'kiwi':35, 'grapes':75}
fruit1.update(fruit2)
print(fruit1)
fruit2.update(fruit1)
print(fruit2)
#pop an element
fruit2.pop('grapes')
print(fruit2)
