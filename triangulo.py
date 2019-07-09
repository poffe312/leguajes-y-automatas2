#nombre : trinagulo.py
#objetivo: identifica el tipo de trinagulo deacuerdo a sus lados
#autor: fernando cardenas larios
#fecha: 01 de julio del 2019

#------------------------------------------
#funcion para identificar triangulos
#------------------------------------------
def identifica(l1, l2, l3):
    #Equlilatero
    if(l1==l2 and l1==l3):
        print("el triangulo es equilatero", l1,", ", l2,"," ,l3)       
    #isósceles
    elif(l1==l2 or l1==l3 or l2==l3):
        print("el triangulo es isosceles")  
    #escaleno    
    elif(l1 != l2 and l1 != l3):
         print("el triangulo es escaleno")    
def main():
    print("script para identificar triangulos")
    l1=float(input("introduce el lado 1: "))
    l2=float(input("introduce el lado 2: "))
    l3=float(input("introduce el lado 3: "))
    #invocar funcion 
    identifica(l1, l2, l3)

if __name__ == "__main__":
    main()    