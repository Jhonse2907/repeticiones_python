can_termi=int(input("Ingrese la cantidad de terminos a generar: "))
ter=1
con_num=0
continuar=True
while continuar:
    print(ter)
    ter=ter+2
    con_num=con_num + 1
    continuar=con_num<=can_termi-1