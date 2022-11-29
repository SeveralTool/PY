                                                                    ### PYTHON ###
                                  # Fuente:      https://github.com/mouredev/Hello-Python
                                                                    
# print ("Que andas la concha de tu madre :) ")
# print (str(3)) #para pasar de num a string con str

# //////////////////////////////

# Operadores

# my_float = 2.5 * 3
# print(int(my_float)) pasamos de float a entero con int
# print(len("holaaa")) contar caracteres con len
# operadores logicos son : and/or/not

# //////////////////////////////

#poner variables en una cadena de texto con {} , poniendo f al principio
# name, apellido, edad = "Nahuel", "Galeano", 23
# print(f"Mi nombre es {name} y mi apellido {apellido}, tengo {edad} años.")

# //////////////////////////////

# Poner palabras al reves

# nom = "Nahuel"
# rev_nom = nom[::-1]
# print(rev_nom)

# //////////////////////////////

# Funciones

# .count() = cuenta cuantos caracteres
# .isnumeric() = verifica si es numero
# .lower() = pasa a minuscula
# .upper() = pasa a mayuscula

# //////////////////////////////

# Listas
 
# my_lista = [23,234,24, "Nahuel",23]
# my_other_list = list()
# print(my_lista[1])
# my_lista.append("Nahuel Galeano") # agregar elemento al final
# my_lista.insert(2,"JAJA") # insertar en posicion 1 ese texto
# my_lista.remove("JAJA") # eliminar ese elemento
# del my_lista[2] # elimina el elemento 2, pero no retorna nada en console
# my_lista.clear() # borra la lista
# my_lista.sort() # orderna la lista

# //////////////////////////////

# Tuples

# No se pueden modificar, se deben transformar a listas y luego a tuplas.....todo un lio..
# Estructura fija de valores

# //////////////////////////////

# Sets

# Un set no admite elementos repetidos
# my_set = set("ok")
# my_other_Set = {} #esto es un diccionario
# my_other_Set = {"Nahuel", "Galeano", 23, "Nahuel"}
# print(len(my_other_Set))
# new = my_other_Set.union(my_set)
# print("Nahuel" in my_other_Set) # con esto comprobamos si existe Nahuel en la variable
# print(new)

# print(my_other_Set.difference(my_set))

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

print(my_other_diccionario["Nombre"])




# //////////////////////////////

# //////////////////////////////

# //////////////////////////////

# //////////////////////////////

# //////////////////////////////


# //////////////////////////////

# //////////////////////////////

# //////////////////////////////

# //////////////////////////////

# //////////////////////////////

# //////////////////////////////
# //////////////////////////////

# //////////////////////////////

# //////////////////////////////

# //////////////////////////////
# //////////////////////////////
# //////////////////////////////
# //////////////////////////////



# num = 2

# if (num < 10) : print("ajsjasjajs")
# else : print("tu madree")