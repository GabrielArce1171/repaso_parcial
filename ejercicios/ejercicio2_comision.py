"""
Un vendedor gana 5% de comisión sobre sus ventas del mes. Si vende $10,000 o más, la comisión es de 
8%. Si vende más de $50,000, recibe además un bono de $1,000. Se necesita mostrar la comisión, el bono 
y el total a pagar. 
"""
#PROBLEMA:
# Se necesita mostrar la comisión, el bono y el total a pagar de un vendedor, considerando sus ventas del mes.

#ENTRADAS: 
# ventas

#SALIDAS: 
# Mostrar la comisión del vendedor
# Mostrar el bono del vendedor
# Mostrar el total a pagar al vendedor

#REGLAS Y SUPUESTOS: 
# - Gana 5% de comisión sobre sus ventas del mes.
# - Si vende $10,000 o más, la comisión es de 8%.
# - Si vende más de $50,000, recibe además un bono de $1,000.

#ALGORITMO:
# 1. Leer las ventas del vendedor.
# 2. Calcular la comisión: si ventas < 10000 -> 5%, si ventas >= 10000 -> 8%
# 3. Si ventas > 50000, agregar bono de 1000.
# 4. Mostrar la comisión, el bono y el total a pagar.

#CASOS DE PRUEBA:  
# $5,000, $10,000, $50,000 y $50,001 -> $250, $800, $4,000 y $5,000

#RESTRICCIONES PARA EL AGENTE: 
# - No utilizar bibliotecas externas, solo funciones básicas de Python.

#CONTRATO DE FUNCIONES: 
# leerVentas -> Leer las ventas del vendedor
# calcularComision -> calcular la comisión del vendedor segun el monto vendido
# calcularBono -> calcular el bono del vendedor segun el monto vendido
# mostrarPago |-> mostrar la comisión, el bono y el total a pagar al vendedor

def leerVentas():
    ventas = float(input("Ingrese las ventas del vendedor: "))
    return ventas
    
def calcularComision(ventas):
    if ventas < 10000:
        comision = ventas * 0.05
    else:
        comision = ventas * 0.08
    return comision

def calcularBono(ventas):
    if ventas > 50000:
        bono = 1000
    else:
        bono = 0
    return bono

def mostrarPago(ventas):
    comision = calcularComision(ventas)
    bono = calcularBono(ventas)
    total = comision + bono
    print("Comisión: ${:.2f}".format(comision))
    print("Bono: ${:.2f}".format(bono))
    print("Total a pagar: ${:.2f}".format(total))