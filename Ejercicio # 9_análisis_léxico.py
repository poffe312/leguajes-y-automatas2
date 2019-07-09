# script para analizar léxicmente la sentencia printf en ansi c
#autor:
#fecha
def lexico(inst):
    f=inst[0:6]
    print("la palabra reselvada:", f)
    d=inst[6]
    print("el parentesis de apertura: ", d)
    e=inst.find(")")
    a=inst[e]
    t=inst[7:e]
    print("la cadena de caracteres: ", t)  
    print("El parentesis d cierre: ", a)   
    i=inst.find(";")
    j=inst[i]
    print("El simbolo de fin de sentencia: ", j)
    
def main():
    print("análisi léxico de la sentaci printf--")
    sentencia=input("introduce la sentencia con printf")
    lexico(sentencia)
    #esprecion regular 
    #sentencia = pr parentesisApertura String | id parentesisCerradura sfin
    #pr= printf
    #parentesisApertura= (
    #String ="+caracter"
    #caracter= a|b|c..A|B|C..|*|+|0,1,2,3..9|space
    #id=identificador ó varible 
    #parentesisCerradura=)
    #sfin=;
    
if __name__ =="__main__":
    main()