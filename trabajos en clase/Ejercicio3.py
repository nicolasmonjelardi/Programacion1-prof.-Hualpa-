#Ejercicio 3-Evaluación de crédito bancario
nombre_apellido=input("ingrese su nombre y a pellido: ")
cuit=input("ingrese su cuit con el formato: 20-43272459-3: ")
if len(cuit)==13:
    pass
    ingresos=int(input("ingrese sus ingresos mensuales: "))
    if ingresos < 200000:
        print("ingresos insuficientes")
        exit
    else:
        antiguedad=int(input("ingrese sus años de antigüedad: "))
        historial=input("ingrese su historial crediticio bueno/regular/malo: ").lower()
        if historial=="malo":
            print("rechazado")
            exit
        else:
            if antiguedad < 2:
                print(f"cliente: {nombre_apellido}")
                print(f"cuit: {cuit}")
                print(f"ingresos: {ingresos}")
                print(f"antigüedad: {antiguedad}")
                print(f"historial: {historial}")
                print("monto aprobado: $500.000")
            elif antiguedad>=2 and historial=="regular":
                print(f"cliente: {nombre_apellido}")
                print(f"cuit: {cuit}")
                print(f"ingresos: {ingresos}")
                print(f"antigüedad: {antiguedad}")
                print(f"historial: {historial}")
                print("monto aprobado:  $1.000.000")
            else:
                print(f"cliente: {nombre_apellido}")
                print(f"cuit: {cuit}")
                print(f"ingresos: {ingresos}")
                print(f"antigüedad: {antiguedad}")
                print(f"historial: {historial}")
                print("monto aprobado: $3.000.000")
else:
    print("cuit inválido")
    exit