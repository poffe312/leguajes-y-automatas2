#nombre : poeraciones.py
#objetivo: muestra como trabajar los metodos p funciones
#autor:
#fecha:
#-----------------------------------
#funcion para sumar dos enteros
#-----------------------------------
def suma(num1,num2):
    return num1+num2
#-----------------------------------
#funcion para restar dos enteros
#-----------------------------------    
def resta(num1,num2):
    return num1-num2
#-----------------------------------
#funcion para multipricacion dos enteros
#-----------------------------------    
def mul(num1,num2):
    return num1*num2
#-----------------------------------
#funcion para divicion dos enteros
#-----------------------------------    
def div(num1,num2):
    return num1/num2  
#-----------------------------------
#funcion para comparar dos enteros
#-----------------------------------    
def comparar(num1,num2):
    if(num1>num2):
        print("el mayor es num1", num1)

    elif(num2>num1):
         print("el mayor es num2",num2) 
    else: 
         print("los numero son iguales ", num1," , ", num2)         


#-----------------------------------
#funcion para hacer un ciclo con for
#----------------------------------- 
def cuenta(num1,num2):
    if(num2>=num1):
        for i in range(num1,num2+1):
         print("valor de i:",i)
    if(num1>num2):   
        for i in range(num2,num1):
            print("valor de i:",i) 

#funcion main 
def main():
    #variable para el while
    ciclo=True
    while (ciclo==True): 
      
        print ("--operaciones vasicas-- ")
        print("\n")
        num1=int (input("ingresa el primer numero:"))
        num2=int (input("ingresa el segundo numero:"))
        #invocamos las funciones 
        print("la suma es:"+ str (suma(num1,num2)))  
        print("la resta es:"+ str (resta(num1,num2)))   
        print("la multipicacion es:"+ str (mul(num1,num2)))   
        print("la divicion es:"+ str (div(num1,num2)))  
        comparar(num1, num2) 
        cuenta(num1,num2)

        cad= input("otro cálculo (s/n)?")
        if(cad=="S" or cad =="s"):
           ciclo =True
        else:
            ciclo=False        


if __name__ == "__main__":
    main()