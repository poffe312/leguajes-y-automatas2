datosAlumno={"numero de contro":"16460108", "nombre":"fernando cardenas", "carrera":"sistemas computacionales",
             "telefono":"3121329590"}
def buscarC():
    g= input("que clave decea buscar")
    print(datosAlumno[g])
def modificar():
    f=input("que clave le quiere modificar: ")
    d=input("nueva corresion: ")
    datosAlumno[f]= d
    print(datosAlumno)
def main():
    ciclo= True
    while ciclo == True:       
        print("---Script--")
        print("1.--- buscar con clave")
        print("2.- modificar--")
        opc=int (input("elija una opcion entre 1 y 2: "))
        if(opc==1):
            buscarC()
        elif (opc==2):
            modificar()
        respuesta= input("desea hacer otro consulta: (s/n)?")
        if (respuesta == "S" or respuesta == "s"):
             ciclo= True            
        else:
            ciclo= False 
    print(datosAlumno)          
    
if __name__ == "__main__":
    main()
