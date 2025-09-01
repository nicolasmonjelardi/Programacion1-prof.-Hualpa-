#Ejercicio 1: Clasificación de impuestos

#Pedir:
nombre=input("Ingrese su nombre completo: ")
edad=int(input("Ingrese su edad: "))
ingresos_anuales=float(input("Sus ingresos anuales: "))

#Salida:
print(f"Nombre: {nombre}")
print (f"Edad: {edad}")
print(f"Ingresos anuales: {ingresos_anuales}")

#Reglas:
if ingresos_anuales<500000:
    print("No paga impuestos")
elif ingresos_anuales>=500000 and ingresos_anuales<2000000:
    if edad>65:
        print(f"(impuesto 10%) impuesto final: {(ingresos_anuales * 0.1)/2}")
    else:
        print(f"(impuesto 10%) impuesto final: {ingresos_anuales * 0.1}")
elif ingresos_anuales>=2000000 and ingresos_anuales<5000000:
    if edad>65:
        print(f"(impuesto 20%) impuesto final: {(ingresos_anuales*0.2)/2}")
    else:
        print(f"(impuesto 20%) impuesto final: {ingresos_anuales*0.2}")
elif ingresos_anuales>=5000000:
    if edad>65:
        print(f"(impuesto 35%) impuesto final: {(ingresos_anuales*0.35)/2}")
    else:
        print(f"(impuesto 35%) impuesto final: {ingresos_anuales*0.35}")

#Ejercicio 2: Sistema de clasificaciones con promoción

#Pedir:
nombre=input("Ingrese su nombre: ")
legajo=input("Ingrese su legajo: ")
nota1=int(input("Ingrese la primer nota: "))
nota2=int(input("Ingrese la segunda nota: "))
nota3=int(input("Ingrese la tercer nota: "))
estado=" "

#Reglas:
if (nota1>=0 and nota1<=10)and(nota2>=0 and nota2<=10)and(nota3>=0 and nota3<=10):
    if nota1<4 or nota2<4 or nota3<4:
        estado="Desaprobado"
    elif ((nota1+nota2+nota3)/3)<6:
            estado="Desaprobado"
    elif ((nota1+nota2+nota3)/3)>=6 and ((nota1+nota2+nota3)/3)<=7:
            estado="Aprobado con final"
    elif ((nota1+nota2+nota3)/3)>=8:
            estado="Promocionado"
else: 
    print("Por favor, ingrese una nota válida")
    exit

#Salida:
print(f"\033[94mNombre: {nombre}\033[0m")
print(f"\033[33mLegajo: {legajo}\033[0m")
print(f"\033[94mPrimer Nota: {nota1}\033[0m")
print(f"\033[32mSegunda Nota: {nota2}\033[0m")
print(f"\033[36mTercer Nota: {nota3}\033[0m")
print(f"Estado Académico: {estado}")

#Ejercio 3: Simulador de cajero automatico

#pedir
usuario=input("Ingrese su nombre de usuario: ")
pin_correcto="1234"
saldo_inicial=50000
intentos=0
pin=""

#Validar el pin
while intentos <3:
    pin=input("Ingrese su pin: ")
    if pin==pin_correcto:
        break
    else:
        print("Pin incorrecto")
        intentos+=1
if pin!= pin_correcto:
    print("Intentos de acceso agotados!")
    exit

print(f"Bienvenido {usuario}")
print(f"su saldo es de: {saldo_inicial}")

#Reglas 
while True:
    retiro=input("Ingrese el monto que desea retirar.(Escriba cancelar para finalizar)")
    if retiro.lower()=="cancelar":
        break
    if not retiro.isdigit():
        print("Por favor, ingrese solo valores numéricos")
        continue
    
    monto=int(retiro)
    if monto%1000 !=0:
        print("El monto del retiro debe ser multiplo de 1000")
        continue
    if monto>saldo_inicial:
        print("Saldo insuficiente")
        continue
    
    comision=0
    if monto>20000:
        comision=int(monto*0.02)
        print("(comision del 2%): {comision}")
    
    total=monto+comision
    if total>saldo_inicial:
        print("Saldo insuficiente!")
        continue
    saldo_inicial-=total
    print(f"Acaba de retirar: ${monto}")
    print(f"Saldo restante: {saldo_inicial}")

print(f"Saldo final: ${saldo_inicial}")

#Ejercicio 4: Categoría de conductores

#Pedir
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
experiencia=int(input("Ingrese sus años de experiencia conduciendo: "))

#Reglas:
if edad<18:
    print("Usted no puede conducir")
elif edad>=18 and experiencia<1:
    print("Usted es un conductor principiante")
elif edad>=21 and (experiencia>=1 and experiencia<5):
    print("Usted es un conductor intermedio")
elif edad>=30 and experiencia>10:
    print("Usted es un conductor profesional")
else:
    print("Usted es un conductor estandar")

#Ejercicio 5: Simulador de carrito de compras

#Pedir:
nombre=input("Ingrese su nombre: ")
cantidad_productos=int(input("Ingrese la cantidad de productos que lleva"))

#Reglas:
if cantidad_productos<0:
    print("Por favor, ingrese un valor positivo")
else:
    exit