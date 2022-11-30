                # Created by SeveralTool.sys

from tkinter import * # Impòrtamos la libreria de Tkinter

ventana = Tk()  #Creamos la ventana grafica
ventana.title("Calculadora by SeveralTool")

#Input
input = Entry(ventana, font = ("Calibri 20")) #Establecemos la fuente del cuadro de texto
input.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 5)

n = 0 # Variable global para no insertar caracteres desde la izquierda

# Funciones

def click_btn(valor): # Funcion para insertar botones en el input
    global n
    input.insert(n, valor)
    n += 1

def delete(): # Funcion para borrar input
    global n
    input.delete(0, END)
    n = 0

def result(): # Funcion para calcular y mostrar resultado
    global n
    ecua = input.get()
    resultado = eval(ecua)
    input.delete(0, END)
    input.insert(0, resultado)
    n = 0
    
     
#Botones

boton1 = Button(ventana,text = "1", width= 5, height= 2, command = lambda: click_btn(1))
boton2 = Button(ventana,text = "2", width= 5, height= 2, command = lambda: click_btn(2))
boton3 = Button(ventana,text = "3", width= 5, height= 2, command = lambda: click_btn(3))
boton4 = Button(ventana,text = "4", width= 5, height= 2, command = lambda: click_btn(4))
boton5 = Button(ventana,text = "5", width= 5, height= 2, command = lambda: click_btn(5))
boton6 = Button(ventana,text = "6", width= 5, height= 2, command = lambda: click_btn(6))
boton7 = Button(ventana,text = "7", width= 5, height= 2, command = lambda: click_btn(7))
boton8 = Button(ventana,text = "8", width= 5, height= 2, command = lambda: click_btn(8))
boton9 = Button(ventana,text = "9", width= 5, height= 2, command = lambda: click_btn(9))
boton0 = Button(ventana,text = "0", width= 15, height= 2, command = lambda: click_btn(0))

boton_sum = Button(ventana,text = "+", width= 5, height= 2, command = lambda: click_btn("+"))
boton_multi = Button(ventana,text = "x", width= 5, height= 2, command = lambda: click_btn("*"))
boton_div = Button(ventana,text = "/", width= 5, height= 2, command = lambda: click_btn("/"))
boton_rest = Button(ventana,text = "-", width= 5, height= 2, command = lambda: click_btn("-"))

boton_del = Button(ventana,text = "DEL", width= 5, height= 2, command = lambda: delete())
boton_res = Button(ventana,text = "=", width= 5, height= 2, command = lambda: result())
boton_point = Button(ventana,text = ".", width= 5, height= 2, command = lambda: click_btn("."))

boton_parentesis1 = Button(ventana,text = "(", width= 5, height= 2, command = lambda: click_btn("("))
boton_parentesis2 = Button(ventana,text = ")", width= 5, height= 2, command = lambda: click_btn(")"))

#Agregar los botones en pantalla

boton_del.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_div.grid(row = 1, column = 3, padx = 5, pady = 5)

boton7.grid(row = 2, column = 0, padx = 5, pady = 5) 
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_multi.grid(row = 2, column = 3, padx = 5, pady = 5)

boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_rest.grid(row = 4, column = 3, padx = 5, pady = 5)

boton0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
boton_point.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_res.grid(row = 5, column = 3, padx = 5, pady = 5)


ventana.mainloop()
