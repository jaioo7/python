#strings are sequence of characters enclosed within single quotes('') double quotes ("") triple quotes (''' ''')
# Examples

str1='a'
print(str1)
print(type(str1))
str2="jai sankaru"
print(str2)
print(type(str2))
str3= '''hello
jai
sankaru
where'''
print(str3)
#Extracting Individual Characters
my_string= "jovy loves pizza"
print(my_string[0])
print(my_string[-1])
#Finding length of string
print(len(my_string))
#converting string to lower case
print(my_string.lower())
#converting string to upper case
print(my_string.upper())
#replacing a substring
print(my_string.replace('ovy','ai'))
# Number of occurrences of substing
new_string="hello hello world"
print(new_string.count("l"))
#finding the index of substring starting point
print(new_string.find("world"))
#splitting a string
fruits="I like apple, mango, banana, apple"
print(fruits.split(','))
date='21.12.2004'
print(date.split('.'))


##strings
# a="Jai, Sankaru, Bandaru, Tirupati"
# print(len(a))
# print(min(a))
# print(max(a))
# print(a.replace("Jai","Nikki"))
# print(a.lower())
# print(a.upper())
# print(a.split(','))
# print(a.count("a"))
# print(a.find('Bandaru'))
# print(a[0])
# print(a[-1])
# print(a[4:12])

# (+)
a='Jai'
b='Sankaru '
c=(a+b)
print(c)
# (*)
print(c*3)

a='jai'
b=25
c=7.8
print("My Name is",a,"My Age is",b,"hight",7.8)
print("My Name is {} My Age is {} years hight {} feet".format(a,b,c))
#lstrip {fist gap delet} see the deference below
a="     jai"
b="jai       "
print(a)
print(a.lstrip())
print(b)
print(b.rstrip())
print('R' in b)
print('j' in b)
print(b.replace('jai','sankaru')) #same meaing
print(b.replace(b,'bandaru')) #same meaing
#swapcase means (lower letter change upper & upper letter change lower)
c=("My Name Is Jai Sankaru" )
print(c.swapcase())