# Personalizados
# Reutilizar los de intenet
# Bibliotecas de python que se descargan desde internet

# Modulos de python
# importando todo el modulo
import datetime

print(datetime.date.today()) # retorna la fecha actual
print(datetime.timedelta(minutes=100)) # retorna la cantidad de tiempo en horas, minutos y segundos, segun minutos

# importando sólo un método de la librería
from datetime import timedelta, date
print(timedelta(minutes=70))
print(date.today())

# importar mi propio módulo
# importa el módulo completo
import fmath 

fmath.add(1,2)
fmath.substract(1,2)

# importar métodos especificos
from fmath import add, substract

add(1,2)
substract(1,2)

# módulos descargados de internet
# descargar módulo colorama pip install colorama
import colorama
from colorama import Fore, Style, init
init(convert=True)

print("Hello world")
print(Fore.RED + "Hello world")