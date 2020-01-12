# Porción de código donde pasamos parámetros, los procesa y puede o no retornar un resultado
# Es reutilizable

# Funciones predefinidas
# print("hola") # imprime en pantalla
# dir(x) # muestra posibles operaciones
# type(12) # definición del tipo de objeto
# len("hello") # retorna la longitud de un objeto


# Funciones personalizadas
def hello(name="person"): #parámetro por defecto
    print("Hello ", name) # para concatenar respuesta puedo hacerlo con coma o con el signo mas

hello("Meli")
hello("Ryan")
hello()

def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10,30))

# Funciones lambda
# Funciones anónimas que toman argumentos, se escriben en una sola expresión
add = lambda numberOne, numberTwo: numberOne + numberTwo
print(add(10,30))