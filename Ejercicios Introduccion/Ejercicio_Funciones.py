"""
Ejercicio: Funciones
1) Crear una función que calcule el número de días de un mes (ejercicio anterior).
2) Crear una función que reciba un argumento, y si se trata de un cadena retorne “Es un string: nombre”. Si el argumento es erróneo debe devolver “Error”
3) Crea una función que reciba un número y devuelva el mes en esa posición
"""

import enum


def calcDia(meses, mes):
    return meses[mes]

print("1) Crear una función que calcule el número de días de un mes (ejercicio anterior).")

meses = {"Enero" : 31, "Febrero" : 28, "Marzo": 31, "Abril" : 30, "Mayo" : 31, "Junio" : 30
    , "Julio" : 31, "Agosto" : 31, "Septiembre" : 30, "Octubre" : 31, "Nomviembre": 30, "Diciembre" : 31}

#mes = input("\nIntroduzca el mes para saber el numero de dias que tiene: ")

# Fue comentareada la linea 19 solo para colocar un valor estatico y que la ejecucion del programa sea mas rápida.
print(calcDia(meses, "Enero"), "\n") 


def cad(cadena):
    result = "Error!"
    if isinstance(cadena, str):
        result = print(f"Es una cadena => {cadena}")
    return result

print("2) Crear una función que reciba un argumento, y si se trata de un cadena retorne “Es un string: nombre”. Si el argumento es erróneo debe devolver “Error”")

print(cad(10)) #Cambiar el dato para hacer la prueba de la funcion.


def obtener_mes(meses, pos):
    for i, mes in enumerate(meses.items()):
        if i == pos:
            return mes

print("3) Crea una función que reciba un número y devuelva el mes en esa posición")
print(obtener_mes(meses, 8), "\n")
