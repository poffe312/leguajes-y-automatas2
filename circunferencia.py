#nombre : circuferenci.py
#objetivo: calcula el area de diametro de una circuferencia e importar la libreria math
#autor: fernando cardenas larios
#fecha: 01 de julio del 2019

import math as mat
import os 



#--------------------------------------------------------
#funcion para calcular Area
#--------------------------------------------------------
def calculaArea(r):
    area=mat.pi*(mat.pow(r,2)) 
    return area
#--------------------------------------------------------
#funcion para calcular Diametro
#--------------------------------------------------------
def calculaDiametro(d):
    diam=d*2
    return diam




def main():
    ciclo=True 
    while ciclo == True:
        print("-- script para calcular Area de circuferencia--")
        radio=float( input("produce el valor del radio:"))
        #invocar un metodo
        print("el area es: ", calculaArea(radio) )
        print("el diametro es: ",  calculaDiametro(radio))
        respuesta= input("desea hacer otro calculo: (s/n)?")
        if (respuesta == "S" or respuesta == "s"):
            ciclo= True            
        else:
            ciclo= False
        os.system("cls")       

if __name__ == "__main__":   
    main()   