# programa para resolver problema 3
def main():
    suma, contador=0, 1
    while contador<=10:
        numero=float(input("salario del trabajador: "))
        suma=numero+suma
        contador +=1
    print("la suma de los 10 salarios es: ", suma)    
if __name__ == "__main__":
    main()