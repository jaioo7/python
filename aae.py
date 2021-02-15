# Python String Methods
name='jai' or "jai" or '''jai'''
print(name)
print(type(name))
print(name.replace('j','J'))
# Operators ( +, *, [], [:], in, not in, {}, %)
firstname='jai'
lastname='sankaru'
fullname=(firstname+lastname)
print(fullname)
print(firstname,lastname)
print(firstname+lastname)
print(firstname*8)
print(firstname[0])
print(firstname[0:2])
full="Bandaru Jai Sankaru"
print('Jai' in full)
print('cherry' in full)
print('Jai' not in full)
print('nikki' not in full)
print(full[0])
print(full[0:7])

name1='jai'
name2='Sankaru'
name3='bandaru'

print('My name {} {} {}'.format(name1,name2,name3))
print('my name',name1,name2,name3)

jai='jai'
age=25
hight= 7.5
print('My Name',jai,'My age',age, 'Hight',hight,'feet')
print('My Name {} My age {} Hight {} feet'.format(jai,age,hight))

name4="Jai Sankaru"
# Find
print(name4.find('S'))
# lengh
print(len(name4))
# lower and upper
print(name4.lower())
print(name4.upper())
# lstrip and rstrip
name5='    jai'
print(name5)
print(name.lstrip())
name6='jai     '
print(name6)
print(name.rstrip())
# split
word= "Checking the network cables, modem, and router"
print(word.split())
print(word.split(','))
# swapcase
name7= 'Bandaru Jai Sankaru'
print(name7.swapcase())
