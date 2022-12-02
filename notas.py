#                                                                     ### PYTHON ###
#                                   # Fuente:      https://github.com/mouredev/Hello-Python
                                                                    
print ("Que andas la concha de tu madre :) ")
print (str(3)) #para pasar de num a string con str

# //////////////////////////////

# Operadores

my_float = 2.5 * 3
print(int(my_float)) # pasamos de float a entero con int
print(len("holaaa")) # contar caracteres con len
# operadores logicos son : and/or/not

# //////////////////////////////

# poner variables en una cadena de texto con {} , poniendo f al principio
name, apellido, edad = "Nahuel", "Galeano", 23
print(f"Mi nombre es {name} y mi apellido {apellido}, tengo {edad} años.")

# //////////////////////////////

# Poner palabras al reves

nom = "Nahuel"
rev_nom = nom[::-1]
print(rev_nom)

# //////////////////////////////

# Funciones

# .count() = cuenta cuantos caracteres
# .isnumeric() = verifica si es numero
# .lower() = pasa a minuscula
# .upper() = pasa a mayuscula

# //////////////////////////////

# Listas
 
my_lista = [23,234,24, "Nahuel",23]
my_other_list = list()
print(my_lista[1])
my_lista.append("Nahuel Galeano") # agregar elemento al final
my_lista.insert(2,"JAJA") # insertar en posicion 1 ese texto
my_lista.remove("JAJA") # eliminar ese elemento
del my_lista[2] # elimina el elemento 2, pero no retorna nada en console
my_lista.clear() # borra la lista
my_lista.sort() # orderna la lista

# //////////////////////////////

# Tuples

# No se pueden modificar, se deben transformar a listas y luego a tuplas.....todo un lio..
# Estructura fija de valores

# //////////////////////////////

# Sets

# Un set no admite elementos repetidos
my_set = set("ok")
my_other_Set = {} #esto es un diccionario
my_other_Set = {"Nahuel", "Galeano", 23, "Nahuel"}
print(len(my_other_Set))
new = my_other_Set.union(my_set)
print("Nahuel" in my_other_Set) # con esto comprobamos si existe Nahuel en la variable
print(new)

print(my_other_Set.difference(my_set))

# //////////////////////////////

# Diccionarios
# seria como un objeto JSON
my_diccionario = dict()
my_other_diccionario = {
                        "Nombre":"Nahuel",
                        "Apellido":"Galeano",
                        "Edad":23,
                        "Lenguages": {"JS","Python","Kotlin"},
                        1: {"CI:", 834332462}
                        }
my_other_diccionario["Nombre"] = "SeveralTool" # actualizar valor
# .keys() # nos retorna solo el valor de las keys.... nombre, apellido etc
# .fromkeys(("Nombre","Apellido"))  # creamos un diccionario nuevo sin valores
print(my_other_diccionario["Nombre"])

# //////////////////////////////

# Condicionales

num = 2 * 2
if (num < 10 and num > 20):
    print("ajsjasjajs")
elif (num == 4):
    print("Ok, es 4")
else :
    print("tu madree") 

txt = ""
if not txt:
    print("No existe")
else:
    print("Existe")

# //////////////////////////////

# LOOPS

        # While
cond = 7
        
while cond < 10:
    cond += 1 # se incrementa con += / -=
    print(cond)
else:
    print("Es mayor o igual a 10") # else en while

while cond < 100:
    print(cond)
    cond += 2   
    if cond == 50:
        print(cond)
        print("Se termino")
        break # para parar el bucle si queres

        # For

lista = [234,234,4,1,1264,5723,856,25,7,6,8,234,625,78,23,878,9,23,26]

print("Bucle for")
for element in lista:
    print(element)
    
    if element == 26:
        print("Ta")
        break
        

# //////////////////////////////

# Funciones 

def funcion1():
    print("Nahuel sabe")

# if funcion1:
#     print("Mi funcion existe")


def suma(num1, num2):
    print(num1 + num2)
    
suma(10,5)    
suma(40,30)

str = "".join("holaaa")                     # .join se usa para agregar contenido
print(str)

def name(nombre, apellido, alias = "SeveralTool"):
    print(f"{nombre} {apellido} {alias}")
    
name("Nahuel", "Galeano")


def print_text(*text):  # CON ESTE * PODES PASARLE CUALQUIER PARAMETRO QUE QUIERAS
    print(text)

print_text("AJAJSJJAS"," hola todo bien")

# //////////////////////////////

# Clases

class Persona:    # los nombres de las clases no e usa el snake case..... en mayus y todo junto
    pass        # pass evita el error de que la funcion/clases este vacia

print(Persona)


class MiPersona:
    def __init__(self, name, surname, heigth, alias = "SeveralTool"):   #esto no es funcion... es un constructor de clase
     self.name = name 
     self.surname = surname
     self.heigth = heigth  
     self.alias = alias

    def caminar(self):  # debemos llamar a self en una funcion dentro de una clase
        print(f"{self.name} esta caminando...")


yo = MiPersona("Nahuel","Galeano",1.78)
print(f"{yo.name} {yo.surname} mide {yo.heigth}")

yo.caminar()

# # //////////////////////////////

print("# # /////////////Excepciones (control de errores)/////////////////")

# Excepciones (control de errores)

try:
    print(5 + "5")

except TypeError as err:     #esto se ejecuta si hay un error en try  HAY MUCHOS TIPOS DE ERRORES: ValueError/TypeError/Exception...
    print("error")
    print(err)  # Ver info del error
    
else:   # esto se ejecuta si no hay una excepcion
    print("Sin errores")

finally:     # esto se ejecuta siempre
    print("todo controlado")

# # //////////////////////////////

# Modulos

# import Passs
# Passs.ok()

# from Passs import ok
# ok()

# import math
# print(int(math.exp(4)))

# from math import exp as Exponente
# print(Exponente(5))

# import random

# num = random.random()
# print(num)


# # //////////////////////////////

    # delay

import time

print("jajsajs")
time.sleep(2)
print("holaaaaaa")


# # //////////////////////////////





# # //////////////////////////////

# # //////////////////////////////

# # //////////////////////////////
# # //////////////////////////////

# # //////////////////////////////

# # //////////////////////////////

# # //////////////////////////////
# # //////////////////////////////
# # //////////////////////////////
# # //////////////////////////////



