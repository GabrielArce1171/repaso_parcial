"""
Una biblioteca cobra $5 por cada día de retraso en la devolución de un libro. A partir del día 11 de 
retraso, cada día cuesta $10. La multa máxima es de $200. Se necesita mostrar la multa a partir de los 
días de retraso. 
"""
#PROBLEMA:
# Se necesita mostrar la multa a pagar por el retraso en la devolución de un libro.

#ENTRADAS: 
# días de retraso

#SALIDAS: 
# Mostrar la multa a pagar

#REGLAS Y SUPUESTOS: 
# - Cobra $5 por cada día de retraso.
# - A partir del día 11 de retraso, cada día cuesta $10.
# - La multa máxima es de $200.

#ALGORITMO:
# 1. Leer los días de retraso.
# 2. Calcular la multa: si días <= 10 -> $5 por día, si días > 10 -> $10 por día.
# 3. Si la multa > 200, establecer multa = 200.
# 4. Mostrar la multa a pagar.

#CASOS DE PRUEBA:  
# 0 días -> $0
# 10 días -> $50
# 11 días -> $60
# 25 días -> $200
# 40 días -> $200

#RESTRICCIONES PARA EL AGENTE: 
# - No utilizar bibliotecas externas, solo funciones básicas de Python.

#CONTRATO DE FUNCIONES: 
# leerDias -> Leer los días de retraso
# calcularMulta -> Calcular la multa a pagar segun los días de retraso
# mostrarMulta -> Mostrar la multa a pagar

def leerDias():
    dias = int(input("Ingrese los días de retraso: "))
    return dias

def calcularMulta(dias):
    if dias <= 10:
        multa = dias * 5
    else:
        multa = 10 * 5 + (dias - 10) * 10
    if multa > 200:
        multa = 200
    return multa

def mostrarMulta(multa):
    print("La multa a pagar es: ${}".format(multa))