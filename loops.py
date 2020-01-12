# Utilizado para bucles o iteraciones
foods = ['apples','bread','cheese','milk','bananas','graves']

print(foods[0])
print(foods[1])
print(foods[2])

# for recorre todos los elementos
for food in foods:
    if food == 'cheese':
        print("Tienes que comprar esto")
        break # parar el for
        if food == 'bread':
            continue # sigue la ejecución
    print(food)
   
# recorrer un rango
for number in range(1,8):
    print(number)

# recorrer un string
for letter in "Hello":
    print(letter)

# while recorre mediante un condicional
count = 4
while count <= 10:
    print(count)
    count = count + 1 # sin esta línea el bucle será infinito