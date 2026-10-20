from ejercicios.ejercicio1_taxi import leerKilometros, calcularImporte, mostrarImporte
from ejercicios.ejercicio2_comision import leerVentas, calcularComision, calcularBono, mostrarPago
from ejercicios.ejercicio3_biblioteca import leerDias, calcularMulta, mostrarMulta

def ejecutar_ejercicio1():
    kilometros = leerKilometros()
    importe = calcularImporte(kilometros)
    mostrarImporte(importe)

def ejecutar_ejercicio2():
    ventas = leerVentas()
    comision = calcularComision(ventas)
    bono = calcularBono(ventas)
    mostrarPago(ventas)

def ejecutar_ejercicio3():
    dias = leerDias()
    multa = calcularMulta(dias)
    mostrarMulta(multa)

def mostrar_menu():
    print("Seleccione un ejercicio para ejecutar:")
    print("1. Ejercicio 1: Taxi")
    print("2. Ejercicio 2: Comisión de Ventas")
    print("3. Ejercicio 3: Biblioteca")
    print("4. Salir")

def menus():
    opcion = "" 
    while opcion != "0": 
        mostrar_menu()
        opcion = input("Ingrese el número del ejercicio a ejecutar (1-4): ")

        if opcion == "1":
            ejecutar_ejercicio1()
        elif opcion == "2":
            ejecutar_ejercicio2()
        elif opcion == "3":
            ejecutar_ejercicio3()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        elif opcion != "0": 
            print("Opción no válida.")