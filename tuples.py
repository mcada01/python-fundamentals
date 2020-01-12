# no se pueden alterar
# se definen para datos inmutables que nunca van a cambiar
# debe ser mas de un elemento , sino será tomado como un entero
# es muy aplicable para diccionarios de datos
a = (9,) # tupla de un solo elemento
x = (1,2,3,4,5) # definición básica
print(x)

months = ('enero','febrero','marzo')

y = tuple((1,2,3)) # definición con constructor
print(y)

print(dir(x))

print(x[2]) # ver elemento especifico
del x # elimina la tupla

estudiantes = {
    (1,234):"Meli", # defino key como una tupla
    (2,444):"Diego"
}

