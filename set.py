# coleccion desordenada que no tiene indice
# se utiliza para datos que no se quieren ordenar
colors = {'Red','Green','Blue'}

print(type(colors))

print('Red' in colors) # buscar un elemento en la coleccion
print(colors.add('Violet')) # adiciona un elemento
print(colors.remove('Red')) # elimina un elemento
colors.clear() # limpia la colección
del colors
