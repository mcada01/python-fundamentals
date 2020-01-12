myStr = "Hello World"

print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Hello','bye'))
print(myStr.count('l'))
print(myStr.startswith('hola'))
print(myStr.endswith('d'))
print(myStr.split())
print(myStr.split(','))
print(myStr.find('o')) #retorna el indice de la coincidencia
print(len(myStr))
print(myStr.index('e'))
myStr.isnumeric()
myStr.isalpha()
myStr[4] #o
myStr[-5] #W es el inverso

print("My name is " + myStr)
print(f"My name is {myStr}") #concatenar con una variable anterior, disponible apartir de version 3.6
print("My name is {0}".format(myStr))