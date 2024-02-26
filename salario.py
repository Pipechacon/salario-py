import os 

bandera = True
while bandera:
    print("MENU DE OPCIONES")
    print("1. Calcular salario con aumento")
    print("2. Salir")

    opc = int(input("Seleccione una opción: "))

    if opc == 1:
        print("CALCULAR SALARIO CON AUMENTO")
        codigo = input("Ingrese el código del trabajador: ")
        nombre = input("Ingrese el nombre del trabajador: ")
        apellido = input("Ingrese el apellido del trabajador: ")
        edad = int(input("Ingrese la edad del trabajador: "))
        sueldo = float(input("Ingrese el sueldo del trabajador: "))

        if 18 <= edad <= 30:
            sueldo *= 1.05
        elif 31 <= edad <= 50:
            sueldo *= 1.10
        else:
            sueldo *= 1.15
        
        print("Información del trabajador:")
        print("Código:", codigo)
        print("Nombre:", nombre)
        print("Apellido:", apellido)
        print("Edad:", edad)
        print("Nuevo sueldo:", sueldo)

    elif opc == 2:
        print("HASTA LUEGO")
        bandera = False
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
