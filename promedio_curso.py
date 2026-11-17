can_estu=int(input("Ingrese la cantidad de estudiantes: "))
sum_not=0
su=1
apro=0
repro=0
while su<=can_estu:
    nota=int(input(f"Ingrese la nota del estudiante {su}: "))
    sum_not=sum_not+nota
    su+=1
    if nota>=3.0:
        apro+=1
    else:
        repro+=1
prom=sum_not/can_estu
print("La cantidad de estudiantes que reprobaron fueron: ",repro)
print("La cantidad de estudiantes que aprobaron fueron: ",apro)
print("El promedio del curso es de: ", prom)