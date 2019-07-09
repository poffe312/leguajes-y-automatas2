#nombre : listas.py
#objetivo: muestra el funcionamiento de las listas en python
#autor: fernando cardenas larios
#fecha: 02 de julio del 2019
#-------------------------------------------
lista= []

#---------------------------------------
# función para agregar items a la lista
#----------------------------------------
def agregaItems(dato):
    lista.append(dato)

#---------------------------------------
# función para buscar items a la lista
#----------------------------------------
def buscar():
    dato=input("dato que quiere buscar")
    if(dato in lista):
        print ("si existe en la lista:", dato)
    else:
        print("no eiste en la lista")    


#----------------------------------------
# función para imprimir los elementos de la lista
#----------------------------------------
def imprimir():
    j=0
    for i in lista:
        print("Item: ",j,",", i)
        j+=1
#----------------------------------------
# borrar intem en la lista
#----------------------------------------
def eliminar(dato):
    #buscamos el elemento
    if(dato in lista):
        lista.remove(dato)
        print("dato eliinado")
    else:
        print("item no existe en la lista..")    
def main():
    ciclo= True
    while ciclo == True:
        print("---Script para trabajar con lista--")
        print("1.- agregar un elemento a la lista--")
        print("2.- buscar un elemtento de la lista--")
        print("3.- modificar un elemento de la lista--")
        print("4.- eliminar un elemento de la lista--")
        print("5.- salir--")
        opc=int (input("elija una opcion entre 1 y 6: "))
        if(opc==1):
            item=input("introduce valor del elemento")
            agregaItems(item)
        elif (opc==2):
            buscar()
        elif (opc==3):
            print("opcion3")
        elif (opc==4):
            eliminar()
        elif(opc==5):
            imprimir() 
        elif(opc ==6):
            print("* fin del programa") 
        else:
            print("seleccionar un entero entre 1 y 6")    
        respuesta= input("desea hacer otro consulta: (s/n)?")
        if (respuesta == "S" or respuesta == "s"):
            ciclo= True            
        else:
            ciclo= False                  

    


if __name__ == "__main__":
    main()    