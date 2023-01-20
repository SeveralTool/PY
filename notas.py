# # #                                                                     ### PYTHON ###
# # #                                   # Fuente:      https://github.com/mouredev/Hello-Python
         
                                                                  
# # print ("Hola, todo bien? :) ")
# # print (str(3)) #para pasar de num a string con str

# # # //////////////////////////////

# # # Operadores

# # my_float = 2.5 * 3
# # print(int(my_float)) # pasamos de float a entero con int
# # print(len("holaaa")) # contar caracteres con len
# # # operadores logicos son : and/or/not

# # # //////////////////////////////

# # # poner variables en una cadena de texto con {} , poniendo f al principio
# # name, apellido, edad = "Nahuel", "Galeano", 23
# # print(f"Mi nombre es {name} y mi apellido {apellido}, tengo {edad} años.")

# # # //////////////////////////////

# # # Poner palabras al reves

# # nom = "Nahuel"
# # rev_nom = nom[::-1]
# # print(rev_nom)

# # # //////////////////////////////

# # # Funciones

# # # .count() = cuenta cuantos caracteres
# # # .isnumeric() = verifica si es numero
# # # .lower() = pasa a minuscula
# # # .upper() = pasa a mayuscula

# # # //////////////////////////////

# # # Listas
 
# # my_lista = [23,234,24, "Nahuel",23]
# # my_other_list = list()
# # print(my_lista[1])
# # my_lista.append("Nahuel Galeano") # agregar elemento al final
# # my_lista.insert(2,"JAJA") # insertar en posicion 1 ese texto
# # my_lista.remove("JAJA") # eliminar ese elemento
# # del my_lista[2] # elimina el elemento 2, pero no retorna nada en console
# # my_lista.clear() # borra la lista
# # my_lista.sort() # orderna la lista

# # # //////////////////////////////

# # # Tuples

# # # No se pueden modificar, se deben transformar a listas y luego a tuplas.....todo un lio..
# # # Estructura fija de valores

# # # //////////////////////////////

# # # Sets

# # # Un set no admite elementos repetidos
# # my_set = set("ok")
# # my_other_Set = {} #esto es un diccionario
# # my_other_Set = {"Nahuel", "Galeano", 23, "Nahuel"}
# # print(len(my_other_Set))
# # new = my_other_Set.union(my_set)
# # print("Nahuel" in my_other_Set) # con esto comprobamos si existe Nahuel en la variable
# # print(new)

# # print(my_other_Set.difference(my_set))

# # # //////////////////////////////

# # # Diccionarios
# # # seria como un objeto JSON
# # my_diccionario = dict()
# # my_other_diccionario = {
# #                         "Nombre":"Nahuel",
# #                         "Apellido":"Galeano",
# #                         "Edad":23,
# #                         "Lenguages": {"JS","Python","Kotlin"},
# #                         1: {"CI:", 834332462}
# #                         }
# # my_other_diccionario["Nombre"] = "SeveralTool" # actualizar valor
# # # .keys() # nos retorna solo el valor de las keys.... nombre, apellido etc
# # # .fromkeys(("Nombre","Apellido"))  # creamos un diccionario nuevo sin valores
# # print(my_other_diccionario["Nombre"])

# # # //////////////////////////////

# # # Condicionales

# # num = 2 * 2
# # if (num < 10 and num > 20):
# #     print("ajsjasjajs")
# # elif (num == 4):
# #     print("Ok, es 4")
# # else :
# #     print("tu madree") 

# # txt = ""
# # if not txt:
# #     print("No existe")
# # else:
# #     print("Existe")

# # # //////////////////////////////

# # # LOOPS

# #         # While
# # cond = 7
        
# # while cond < 10:
# #     cond += 1 # se incrementa con += / -=
# #     print(cond)
# # else:
# #     print("Es mayor o igual a 10") # else en while

# # while cond < 100:
# #     print(cond)
# #     cond += 2   
# #     if cond == 50:
# #         print(cond)
# #         print("Se termino")
# #         break # para parar el bucle si queres

# #         # For

# # lista = [234,234,4,1,1264,5723,856,25,7,6,8,234,625,78,23,878,9,23,26]

# # print("Bucle for")
# # for element in lista:
# #     print(element)
    
# #     if element == 26:
# #         print("Ta")
# #         break
        
# # list = [32,423,5235,6,3,5,2,2525]
# # for n in list:
# #     if n == 2:
# #         print("Ya")
# #         break
# #     else:
# #         print("ok")

# # # //////////////////////////////

# # # Funciones 

# # def operacion(num1, num2):
# #     op = num1 + num2
# #     return op
# # res = operacion(20,20)
# # print(res)

# # def funcion1():
# #     print("Nahuel sabe")

# # # if funcion1:
# # #     print("Mi funcion existe")


# # def suma(num1, num2):
# #     print(num1 + num2)
    
# # suma(10,5)    
# # suma(40,30)

# # str = "".join("holaaa")                     # .join se usa para agregar contenido
# # print(str)

# # def name(nombre, apellido, alias = "SeveralTool"):
# #     print(f"{nombre} {apellido} {alias}")
    
# # name("Nahuel", "Galeano")


# # def print_text(*text):  # CON ESTE * PODES PASARLE CUALQUIER PARAMETRO QUE QUIERAS
# #     print(text)

# # print_text("AJAJSJJAS"," hola todo bien")

# # # //////////////////////////////

# # # Clases

# # class Persona:    # los nombres de las clases no e usa el snake case..... en mayus y todo junto
# #     pass        # pass evita el error de que la funcion/clases este vacia

# # print(Persona)


# # class MiPersona:
# #     def __init__(self, name, surname, heigth, alias = "SeveralTool"):   #esto no es funcion... es un constructor de clase
# #      self.name = name 
# #      self.surname = surname
# #      self.heigth = heigth  
# #      self.alias = alias

# #     def caminar(self):  # debemos llamar a self en una funcion dentro de una clase
# #         print(f"{self.name} esta caminando...")


# # yo = MiPersona("Nahuel","Galeano",1.78)
# # print(f"{yo.name} {yo.surname} mide {yo.heigth}")

# # yo.caminar()

# # # # //////////////////////////////

# # print("# # /////////////Excepciones (control de errores)/////////////////")

# # # Excepciones (control de errores)

# # try:
# #     print(5 + "5")

# # except TypeError as err:     #esto se ejecuta si hay un error en try  HAY MUCHOS TIPOS DE ERRORES: ValueError/TypeError/Exception...
# #     print("error")
# #     print(err)  # Ver info del error
    
# # else:   # esto se ejecuta si no hay una excepcion
# #     print("Sin errores")

# # finally:     # esto se ejecuta siempre
# #     print("todo controlado")

# # # # //////////////////////////////

# # # Modulos

# # # import Passs
# # # Passs.ok()

# # # from Passs import ok
# # # ok()

# # # import math
# # # print(int(math.exp(4)))

# # # from math import exp as Exponente
# # # print(Exponente(5))

# # # import random

# # # num = random.random()
# # # print(num)


# # # # //////////////////////////////

# #     # delay

# # # import time

# # # print("jajsajs")
# # # time.sleep(2)
# # # print("holaaaaaa")


# # # # //////////////////////////////

# # # Dates (fechas)

# from datetime import datetime

# now = datetime.now()

# # print(now.day)
# # print(now.hour)
# # print(now.minute)
# # print(now.month)
# # print(now.year)

# timestamp = now.timestamp()


# def view_date(date):
#     print(date.day)
#     print(date.hour)
#     print(date.minute)
#     print(date.month)
#     print(date.year)
#     print(date.timestamp())
    
# year_2023 = datetime(2023,1,7)
# # view_date(year_2023)    

# from datetime import time

# current_time = time()

# # print(current_time.hour)
# # print(current_time.min)
# # print(current_time.second)


# from datetime import date
# from datetime import timedelta #modificar fechas

# current_date = date.today()
# current_date2 = date(2022,12,12) #otra forma de pasar parametros

# # print(f"{current_date.year}-{current_date.month}-{current_date.day}")

# modyear = int(current_date.year) + 1
# # print(modyear)

# # Ejercicio by SeveralTool

# fecha1 = date.today()
# mañana = fecha1 + timedelta(days=1)  # MEJOR FORMA PARA SUMAR Y RESTAR FECHAS Y TIEMPO
# next_month = fecha1 + timedelta(hours=800)
# print(f"{fecha1.year}-{fecha1.month}-{mañana}")
# print(next_month)

# time_delta = timedelta()

# init_delta = timedelta(200,120,30,weeks=10)
# init_delta2 = timedelta(400,100,50,weeks=20)

# # print(init_delta2 - init_delta)
# # print(init_delta2 + init_delta)

# # # # //////////////////////////////
# print(" /////////////# List Comprension/////////////////")
# # List Comprension

# init_list = [0,1,2,3,4,5,6,7,8,9]

# my_list = [i for i in range(10)]
# print(my_list)

# my_list1 = [i * 2 for i in range(10)]
# print(my_list1)

# my_list2 = [i * 2 for i in range(10)]
# print(my_list2)

# def sum(num):
#     return num + 5

# print(sum(5))

# my_list3 = [sum(i) for i in range(10)]
# print(my_list3)

# # # # //////////////////////////////

#                         # RETO
# print(" /////////////# EJERCICIOS/////////////////")
# # Ejercicio 1

# # def eje1():
# #     for i in range(1,101):    
# #         if (i % 3 == 0 and i % 5 == 0):
# #             print("fizzbuzz") 
# #         elif (i % 3 == 0):
# #             print("fizz")
# #         elif (i % 5 == 0):
# #             print("buzz")
# #         else:
# #             print(i)
# # eje1()


# # Ejercicio 2

# def eje2(txt1, txt2):
#     if txt1.lower() == txt2.lower():
#         return False #si son iguales no me sirve 
#     return sorted(txt2.lower()) == sorted(txt1.lower()) # ordena las palabras...sorted()

# print(eje2("amor","roma"))

# # Palabra al reves

# tx="amor"
# inv = tx [:: -1] #is magic
# print(inv)
    
# # Ejercicio 3

#     #Fibonacci
#     #El siguiente siempre es la suma de los 2 anteriores
    
# def Fibonacci():
#     r = 0
#     r2 = 1
#     for n in range(0,50):
#         print(f"{n}: {r}")
#         fib = r + r2
#         r = r2
#         r2 = fib
    
    
    
# Fibonacci()
# ########################

# # Ejercicio 4
# #   Numeros Primos:

# def is_prime(number):
    
#     for number in range(1,101):
        
#         if number >= 2:
#             is_divisible = False
#             for index in range (2,number):
#                 if number % index == 0:
#                     is_divisible = True
#                     break

#             if not is_divisible:    
#                 print(number)

# is_prime(50)

# #####################
# # Ejercicio 5
# # Invertir cadena de texto


# def reverse(txt):
#     txt_len = len(txt) -1
#     text_reverse = ""
#     for index in range(0, len(txt)):
#         text_reverse += txt[txt_len - index -1]
        
#     return text_reverse

# print(reverse("Hola Nahuel"))
    
    
    
# #################################

# # Lambda
# # Se puede almacenar en una variable

# suma = lambda num1, num2: num1 + num2
# print(suma(2,6))

# ###########################################

# # Funciones de orden superior

# def sum_one(value):
#     return value +1

# def sum_two_values(num1, num2,f_suma):
#     return f_suma(num1+num2)

# print(sum_two_values(5,5, sum_one))

# ##########################################

# #Closures

# def sum_ten():
#     def add(value):
#         return value + 10
#     return add

# add_closure = sum_ten()
# print(add_closure(9))


# ######################

# # Map Modifica valores

# numbers = [2,64,2,7,335,9] 
# def multiply(num1):
#     return num1*2
# print(list(map(multiply,numbers)))
# print(list(map(lambda number: number * 2,numbers))) # Good

# ############################

# # Filter True/Flase en base a los valores

# def filter_num(value):
#     if value > 10:
#         return True
#     return False

# print(list(filter( filter_num, numbers)))
# print(list(filter( lambda num: num > 10, numbers))) # Good x2

# ###############################

# # Reduce Opera con un valor mas el acumulable
# # Ejemplo 5+5+5+20 = 35 (15)+20

# from functools import reduce

# def reduce_values(num1,num2):
#     return num1 + num2

# print(reduce(reduce_values,numbers))
# #print(reduce( lambda num: num < 800 , numbers ))

####################################

# Manejo de Ficheros

# import os

# # .txt file

# # txt = open("test_ficheros.txt", "r+")
# # print(txt.read())
# # print(txt.read(15)) # Imprimir solo 15 caracteres
# # txt.write("\nTambien me gusta JavaSript")
# # txt.close()
# # # os.remove("test_ficheros.txt")

# # .json 
# import json

# json_txt = open("json_ficheros.json", "r+")

# json_test = {
#     "name":"Nahuel",
#     "surname": "Galeano",
#     "age": 23,
#     "Lenguages":["Python","JavaScript","React.js","PHP","MySQL"],
#     "GitHub": "https://github.com/SeveralTool",
# }

# json.dump(json_test, json_txt, indent= 2) # Indent: formato en el que escribe en el archivo 2: Espacios delante de los datos
# json_txt.close()
# cont_json = json.load(open("json_ficheros.json"))
# print(cont_json)

# # .csv
# import csv

# # .xlsx
# # Instalar modulo

# # .xlm
# import xml

#####################################

# Expresiones Regulares

import re

str = "Esto es un ejemplo de str"
str2 = "Esto es un ejemplo de str"
print(re.match("str", str)) # Busca desde el principio
print(re.match("Esto es un ejemplo", str2))

###################################################

################# BACKEND ##################
############################################























    












    
    
    




















# # # # //////////////////////////////
# # # # //////////////////////////////

# # # # //////////////////////////////

# # # # //////////////////////////////

# # # # //////////////////////////////
# # # # //////////////////////////////
# # # # //////////////////////////////
# # # # //////////////////////////////

