a=int(input("Escriba el número a analizar: "))
if a>0:
    con_cifras=0
    cop_a=a
    while True:
        cifra = cop_a%10
        cop_a=cop_a//10
        con_cifras=con_cifras+1
        if cop_a==0:
            break

    suma_cifra=0
    cop_a=a
    while True:
        cifra = cop_a%10
        cop_a=cop_a//10
        suma_cifra=suma_cifra+cifra**con_cifras
        if cop_a==0:
            break

    if a==suma_cifra:
        print(a, "es un número de Armstrong.")
    else:
        print(a, "no es un número de Armstrong.")
else:
    print("Debe escribir un entero positivo.")