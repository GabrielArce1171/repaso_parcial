"""
Un taxi cobra $35 de banderazo y $9 por kilómetro recorrido. Los viajes de más de 20 km tienen 10% de 
descuento. Se necesita mostrar el importe del viaje.
"""
#PROBLEMA:
# Se necesita mostrar el importe del viaje de un taxi, considerando el banderazo, el costo por kilómetro y un descuento para viajes largos.

#ENTRADAS: 
# distancia

#SALIDAS: 
# Importe del viaje

#REGLAS Y SUPUESTOS: 
# - El banderazo es de $35.
# - El costo por kilómetro es de $9.
# - Los viajes de más de 20 km tienen un 10% de descuento.

#ALGORITMO:
# 1. Leer la distancia del viaje.
# 2. Calcular el costo total sin descuento: costo_total = banderazo + (costo_por_km * distancia)
# 3. Si la distancia es mayor a 20 km, aplicar el descuento: costo_total = costo_total * 0.9
# 4. Mostrar el costo_total.

#CASOS DE PRUEBA:  
# 5, 20, 21 y 30 km ->  80, 155, 162 y 195

#RESTRICCIONES PARA EL AGENTE: 
# - No utilizar bibliotecas externas, solo funciones básicas de Python.

#CONTRATO DE FUNCIONES: 
# leerKilometros -> lee los kilometros del viaje
# calcularImporte -> calcula el importe del viaje
# mostrarImporte -> muestra el importe del viaje

def leerKilometros():
    while True:
        try:
            distancia = float(input("Ingrese la distancia del viaje en kilómetros: "))
            if distancia < 0:
                print("La distancia no puede ser negativa. Intente nuevamente.")
                continue
            return distancia
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def calcularImporte(distancia):
    banderazo = 35
    costo_por_km = 9
    costo_total = banderazo + (costo_por_km * distancia)
    if distancia > 20:
        costo_total *= 0.9
    return costo_total

def mostrarImporte(importe):
    print(f"El importe del viaje es: ${importe:.2f}")
