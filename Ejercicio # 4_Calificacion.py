#------------------------------------------
# nombre: listaAlumnos.py
# objetivo: permitir capturar en una lista las calificaciones de N alumnos y que permita calcul
# nombre: fernando cardenas larios
# fecha: 04/07/2019
Alumnos= []
def promedio():
    prome=0
    j=0
    for i in Alumnos:
        prome=prome + i
        j=j+1
    prome= prome/j        
    print("el promedio es :", prome)    
def aprobadosResprovados():
    A=0
    j, mayor=0, 0
    porsentajeA=0
    porsetajeR=0
    R=0
    for i in Alumnos:
        j=j+1
        if(i<70):
            R=R+1
        elif(i>=70):
            A=A+1
        elif(i>80):
            mayor=mayor +1
    print("alumnos reprobados: ", R, "alumnos aprobados: ", A) 
    porsentajeA= ((A*100)/j)
    porsetajeR= ((R*100)/j)
    print ("porsentaje de reprobados: ",porsetajeR, "porsentaje de aprobados: ", porsentajeA)
    print ("Número de alumnos cueya calificación fue mayor a 80: ", mayor)

    
def main():
    ciclo= True
    while ciclo == True:
        calificacion=float(input("calificacion del alunmo: "))
        Alumnos.append(calificacion)
        
        respuesta= input("desea hacer otro calificacion: (s/n)?")
        if (respuesta == "S" or respuesta == "s"):
            ciclo= True            
        else:
            ciclo= False 
    promedio()
    aprobadosResprovados()
    
if __name__ == "__main__":
    main()