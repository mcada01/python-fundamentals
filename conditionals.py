# Operadores de comparación
3 > 2 # mayror que, retorna True
5 < 1 # menor que, retorna False
3 >= 5 # mayor o igual que
8 <= 0 # menor o igual que
3 == 3 # igual a, aplica para numeros o strings, retorna True
name = "Meli" # un solo igual es para asignaciones, dar valor a una variable
# Operadores lógicos
x > 2 and x < 10 # operador y
x > 1 or x > 8 # operador o
not(x == y) # operador no, retorna True o False


# Condicionales
# if
x = int(input("Digite un número: "))
if x < 30:
    print("El número es menor que 30")
elif x == 30:
    print("El número es igual a 30")
else:
    print("El número es mayor que 30")


color = input("Ingrese un color: ")
if color == "rojo":
    print("El color es rojo")
elif color == "azul":
    print("El color es azul")
else:
    print("Cualquier color")

# if anidadas
name = "Jhon"
lastname = "Carter"

if name == "Jhon":
    if lastname == "Carter":
        print("Tu eres Jhon Carter")
    else:
        print("Tu no eres Jhon Carter")
else:
    print("Tu no eres Jhon Carter")

if x > 2:
    if x < 10:
        print("x está entre 2 y 10")

if x > 2 and x <= 10:
    print("x es mayor que 2 y menor o igual que 10")

if x > 2 or x <= 20:
    print("x es mayor que 2 o menor o igual que 20")

if (not(x == y)):
    print("x no es igual a y")