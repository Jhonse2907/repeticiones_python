a=int(input("Escriba un numero entero: "))
if a>0:
    copia_a=a
    contador_cifra=0
    suma_cifra=0
    while copia_a>0:
        cifra=copia_a%10
        copia_a=copia_a//10
        suma_cifra=suma_cifra+cifra
        contador_cifra=contador_cifra+1
    print("La cantidad de cifras del numero " ,a, " es " ,contador_cifra)
    print("La sumatoria de las cifras es ",suma_cifra)
else:
    print("No es un numero positivo")