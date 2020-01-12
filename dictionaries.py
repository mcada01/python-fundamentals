# define un dato a partir de claves y valores
producto = {
    "name":"book",
    "cantidad":3,
    "precio":4.99
}

person = {
    "primer_nombre": "Melissa",
    "apellido":"Cadavid"
}

print(type(producto))
print(dir(person))
print(person.keys()) # obtiene el nombre de las llaves
print(person.items()) # obtiene llave  y detalle

del person # elimina el dictionario
person.clear() # limpia el elemento retorna {}
print(person)  

products = [
    {"name": 'book',"precio" : 3.33},
    {"name": 'laptop',"precio" : 5.28}
] # dictionarios dentro de una lista

print(products) 