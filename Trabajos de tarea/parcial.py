titulos = []
ejemplares = []

def mostrar_menu():
    print("""
Opciones Disponibles
1) Agregar títulos
2) Agregar ejemplares
3) Consultar ejemplares disponibles
4) Consultar títulos agotados
5) Modificar títulos
6) Actualizar ejemplares (Préstamo/Devolución)
7) Salir
""")

def agregar_titulos():
    cantidad = input("¿Cuántos títulos desea ingresar? ")
    if not cantidad.isdigit():
        print("Debe ingresar un número válido")
        return
    cantidad = int(cantidad)
    for _ in range(cantidad):
        while True:
            titulo = input("Ingrese el nombre del título: ").lower().strip()
            if titulo == "":
                print("Título inválido")
            elif titulo in titulos:
                print("Este título ya está registrado")
            else:
                titulos.append(titulo)
                ejemplares.append(0)
                break

def agregar_ejemplares():
    if not titulos:
        print("No hay títulos registrados")
        return
    for i, titulo in enumerate(titulos):
        while True:
            cantidad = input(f"Ingrese los ejemplares del título '{titulo}': ")
            if cantidad.isdigit() and int(cantidad) > 0:
                ejemplares[i] = int(cantidad)
                break
            else:
                print("Debe ingresar una cantidad válida")

def consultar_disponibles():
    if not titulos:
        print("No hay títulos registrados")
        return
    for i, titulo in enumerate(titulos):
        print(f"Título: {titulo} - Ejemplares disponibles: {ejemplares[i]}")

def consultar_agotados():
    agotados = [titulos[i] for i in range(len(titulos)) if ejemplares[i] == 0]
    if not agotados:
        print("No hay títulos agotados")
    else:
        print("Títulos agotados:")
        for titulo in agotados:
            print(f"- {titulo}")

def modificar_titulo():
    viejo = input("Ingrese el título a modificar: ").lower().strip()
    if viejo not in titulos:
        print("Título no registrado")
        return
    nuevo = input("Ingrese el nuevo título: ").lower().strip()
    if nuevo == "" or nuevo in titulos:
        print("Título inválido o ya registrado")
        return
    indice = titulos.index(viejo)
    titulos[indice] = nuevo
    print("Título modificado correctamente")

def actualizar_ejemplares():
    if not titulos:
        print("No hay títulos registrados")
        return
    for i, titulo in enumerate(titulos):
        print(f"{i+1}) {titulo} - Ejemplares: {ejemplares[i]}")
    titulo = input("Ingrese el título a actualizar: ").lower().strip()
    if titulo not in titulos:
        print("Título no registrado")
        return
    indice = titulos.index(titulo)
    print("Opciones:\n1) Préstamo\n2) Devolución\n3) Cancelar")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        cantidad = input("¿Cuántos ejemplares se prestaron? ")
        if cantidad.isdigit() and 0 < int(cantidad) <= ejemplares[indice]:
            ejemplares[indice] -= int(cantidad)
            print("Préstamo realizado")
        else:
            print("Cantidad inválida")
    elif opcion == "2":
        cantidad = input("¿Cuántos ejemplares se devolvieron? ")
        if cantidad.isdigit() and int(cantidad) > 0:
            ejemplares[indice] += int(cantidad)
            print("Devolución realizada")
        else:
            print("Cantidad inválida")
    elif opcion == "3":
        print("Operación cancelada")
    else:
        print("Opción inválida")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")
    match opcion:
        case "1": agregar_titulos()
        case "2": agregar_ejemplares()
        case "3": consultar_disponibles()
        case "4": consultar_agotados()
        case "5": modificar_titulo()
        case "6": actualizar_ejemplares()
        case "7":
            print("Saliendo...")
            break
        case _: print("Opción inválida")