demo_list = [1,'hola',1.34,True,[1,2,3]]
colors = ['red','green','blue']

numbers_list = list((1,2,3,4)) #para imprimir una lista debo ponerlo como tupla
print(numbers_list)

r = list(range(1,101))
print(r)

print(type(colors))
print(dir(colors)) # imprime todas las operaciones que puedo realizar con el tipo de dato colors(list en este caso)

print(len(colors)) # 3
print(colors[1]) # green
print(colors[-1]) # blue
print('green' in colors) # True
colors[1]='yellow'
print(colors) # cambiar datos en la lista

colors.append('violet') # agrega un nuevo elemento a la lista colors
colors.extend(('red','yellow')) # puede ser con tupla o lista
print(colors)

colors.insert(1,'pink') # inserta un elemento en el índice 1
colors.insert(len(colors),'orange') # inserta en la ultima posicion
print(colors)

colors.pop() # elimina el ultimo elemento de la lista
colors.pop(2) # elimina el elemento que esta en el indice 2
print(colors)

colors.remove('green') # elimina un elemento especifico de la lista
print(colors)

colors.clear() # para limpiar la lista, quedaria asi []

colors.sort() # ordena los elementos
colors.sort(reverse=True) # ordena a la inversa la lista

colors.index('red') # obtiene el indice de un elemento, los indices inician desde cero
colors.count('red') # cuantas veces esta un elemento en la lista
