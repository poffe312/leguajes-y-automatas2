# Script para simular una calculador básica

import tkinter as tk
from tkinter import *
def imprimir():
    lblsaludar= Entry(None, text=txtC1.get(), font=("agency fb", 14)).place(x=10, y=110)
def borrar():
     lblsaludar=text=" "
# Funcion para salir de la app
def salir():
    wv.destroy()

# Programa principal

# Creamos las ventana
wv = tk.Tk()
# Modificamos el tamaño de la ventana
wv.geometry("500x400")
# Titulo de la ventana
wv.title("ventana")

# Creamos la etiqueta
l1 = Label(None, text="mensaje:")

#Creamos los botones
bI = Button(None, text='imprimir', command=imprimir)
br = Button(None, text='borrar', command=borrar)
bq = Button(None, text= 'Salir', command=salir)

# creamos los campos de texto
txtC1 = Entry(wv)

# Alineamos los widgets
l1.grid(row=1, column=10)
# campos de texto
txtC1.grid(row = 1, column=15)
#txtC2.grid(row=2, column=20)
# Botones
bI.grid(row = 4, column=5)
br.grid(row = 4, column=10)
bq.grid(row = 4, column=35)


# Ciclo de espera de eventos
wv.mainloop()
