import tkinter as tk
from tkinter import *
#El pimer paso es abrir la conexion a la base de datos
import pymysql

# para esto instale la libreria reportlab 
from reportlab.pdfgen import canvas
import time
#Cadena de conexion al servidor de base de datos
try:
    db = pymysql.connect("localhost", "root", "", "automatas2")
    print('Bien')
except:
    print('mal')

cursor = db.cursor()


# Función para insertar
def insertar():
    # Recuperamos los datos de los campos de texto
    cadsqlinsert = "insert into keyword values("+txtC1.get()+","+"'"+txtC2.get()+"');"
    # ejecuta el SQL query usando el metodo execute().
    cursor.execute(cadsqlinsert)
    #operacion atomica
    db.commit()
# Función para borrar
def Borrar():
    cadsqldel = "delete from KeyWord where Id = " + txtC3.get() + ";"
    # ejecuta el SQL query usando el metodo execute().
    cursor.execute(cadsqldel)
    #operacion atomica
    db.commit()

# Función para modificar
def Modificar():
    cadsqlchange = "UPDATE `KeyWord` SET Nombre = '"+txtC4.get()+"' WHERE Id = "+txtC5.get()+";"
    # ejecuta el SQL query usando el metodo execute().
    cursor.execute(cadsqlchange)
    db.commit()
# Función para consultar y guardar en documento pdf
def consultarPDF():
    j = 740
    # creamos una instancia de la clase canvas.Canvas pasándole como argumento el nombre o la ruta del archivo que queremos generar
    F = canvas.Canvas('Reporte1.pdf')
    F.drawString(10, 830, "empresa fernando")
    F.drawString(10, 760, "Id" + "  " + "Nombre")

    
    cursor = db.cursor()
    cadsqlbuscar = "select * from KeyWord;"
    cursor.execute(cadsqlbuscar)
    result = cursor.fetchall()
    
    for row in result:
        clave = row[0]
        nombre = row[1]
        F.drawString(10, j, "    {0}".format(clave,nombre) + ","+ "   {1}".format(clave,nombre))
        j = j - 10
# guarda efectivamente los cambios en el documento.
    F.save()
#consultar normal
def consultar():  
    cursor = db.cursor()
    cadsqlbuscar = "select * from KeyWord;"
    cursor.execute(cadsqlbuscar)
    result = cursor.fetchall()
    for row in result:
        Id= row[0]
        Nombre = row[1]
        print ("Id = {0}, Nombre = {1}".format(Id,Nombre))

# Funcion para salir de la app
def salir():
    wv.destroy()


# Programa principal

# Creamos las ventana
wv = tk.Tk()
# Modificamos el tamaño de la ventana
wv.geometry("500x400")
# Titulo de la ventana
wv.title("base de datos")

# Creamos la etiqueta
l1 = Label(None, text="ingresa el id: ")
l2 = Label(None, text="ingresa el nombre: ")
l3 = Label(None, text="ingrese el id que quiere eliminar: ")
l4 = Label(None, text="ingresa el nuevo nombre: ")
l5 = Label(None, text="ingresa el id: ")
#Creamos los botones
bI = Button(None, text='insertar', command=insertar)
br = Button(None, text='Borrar', command=Borrar)
bm = Button(None, text='Modificar', command=Modificar)
bC = Button(None, text='consultarPDF', command=consultarPDF)
bcon = Button(None, text='consultar', command=consultar)
bq = Button(None, text= 'Salir', command=salir)

# creamos los campos de texto
txtC1 = Entry(wv)
txtC2 = Entry(wv)
txtC3 = Entry(wv)
txtC4 = Entry(wv)
txtC5 = Entry(wv)
#txtc3 = Entry(wv)

# Alineamos los widgets
l1.grid(row=1, column=10)
l2.grid(row=2, column=10)
l3.grid(row=6, column =10)
l4.grid(row= 9, column=10)
l5.grid(row= 10, column=10)
# campos de texto
txtC1.grid(row = 1, column=15)
txtC2.grid(row = 2, column= 15)
txtC3.grid(row=6, column=15)
txtC4.grid(row=9, column=15)
txtC5.grid(row=10, column=15)
# Botones
bI.grid(row = 4, column=10)
br.grid(row = 7, column=10)
bm.grid(row = 14, column=10)
bC.grid(row = 20, column=10)
bcon.grid(row = 20, column=20)
bq.grid(row = 23, column=35)


# Ciclo de espera de eventos
wv.mainloop()
