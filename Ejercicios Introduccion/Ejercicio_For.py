"""
Ejercicio: Bucle foor
1) Crea una función que devuelva una lista con los números múltiplos de 3 entre el 0 y el 90.
2) Crea una función que recorra los meses y devuelva aquellos que contienen una letra ‘E’.
"""

from unittest import result


def multiplos():
    multiplos = []
    for i in range(1, 91):
        if not i % 3:
            multiplos.append(i)
    return multiplos

print("1) Crea una función que devuelva una lista con los números múltiplos de 3 entre el 0 y el 90.")
print(multiplos(), "\n")

def meses_e(meses):
    resultado = []
    for mes in meses.keys():
        if 'e' in mes:
            resultado.append(mes)
    return resultado

print("2) Crea una función que recorra los meses y devuelva aquellos que contienen una letra ‘E’.")

meses = {"Enero" : 31, "Febrero" : 28, "Marzo": 31, "Abril" : 30, "Mayo" : 31, "Junio" : 30
        , "Julio" : 31, "Agosto" : 31, "Septiembre" : 30, "Octubre" : 31, "Nomviembre": 30, "Diciembre" : 31}
        
print(meses_e(meses), "\n")


###---------------------------Anexo de Ejercicio---------------------------###

"""
Ejercicio: Bucle for + diccionario

A partir de una lista de tuplas con el siguiente formato:

nombres = [ (Alvaro, Salamanca),   (Mario, Madrid),   (Marta, Salamanca),   (Juan, Avila),   
(Pedro, Madrid),   (Susana, Soria),   (Martin, Valladolid),   (Mario, Valladolid),   (Jorge, Palencia) ]

Crea un programa que genere un diccionario de ciudades, y que para cada ciudad almacene los nombres de las distintas personas asociadas a esa ciudad
"""

print("Crea un programa que genere un diccionario de ciudades, y que para cada ciudad almacene los nombres de las distintas personas asociadas a esa ciudad")

nombres = [("Alvaro", "Salamanca"),   ("Mario", "Madrid"),   ("Marta", "Salamanca"),   ("Juan", "Avila"),   
("Pedro", "Madrid"),   ("Susana", "Soria"),   ("Martin", "Valladolid"),   ("Mario", "Valladolid"),   ("Jorge", "Valencia")]

resultado = {}

for nombre, ciudad in nombres:
    if ciudad not in resultado:
        resultado [ciudad] = [nombre]
    else:
        resultado[ciudad].append(nombre)
print(resultado)

###---------------------------Anexo de Ejercicio---------------------------###