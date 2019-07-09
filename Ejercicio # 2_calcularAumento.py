def main():
    categoria= int(input("ingrese la categoria que es : "))
    saldo= float(input("ingrese el saldo: "))
    if(categoria==1):
        sf=saldo*.15 + saldo
    elif(categoria==2):
        sf=saldo*.10 + saldo
    elif(categoria==3):
        sf=saldo*.08 + saldo
    elif(categoria==4):
        sf=saldo*.07 + slado
    print("el saldo del trabajador es:", sf)    
    
if __name__== "__main__":
    main()