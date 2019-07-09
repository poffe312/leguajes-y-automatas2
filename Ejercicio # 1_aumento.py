# programa en python que dado como dato elsueldo de un trabajador ,
# le aplique un aumento del 15% si su sueldo es inferior a $1000.00 y de 12%

def main():
    a=float(input("introduce sueldo: "))
    if(a<1000):
        sf=a*.15 + a
    elif(a>=1000):
        sf=a*.12 + st
    print ("el sueldo final es: ", sf)    
if __name__ == "__min__" :
    main()