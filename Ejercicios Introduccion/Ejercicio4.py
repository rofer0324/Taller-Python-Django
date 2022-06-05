"""
Ejercicio 4:
1) Crea un diccionario con todos los meses del año, donde la key sea el mes y el valor los días del mes.
2) Mostrar los días que tiene el mes de Marzo
3) Crea una tupla con los keys del diccionario que se ha creado.
4) Crea una tupla con los values del diccionario que se ha creado.
5) Calcula el tamaño del diccionario
6) Borrar del diccionario los meses de Julio y Agosto
7) Recorrer el diccionario y mostrar por pantalla mes con los días del mes.
"""

print("1) Crea un diccionario con todos los meses del año, donde la key sea el mes y el valor los días del mes.")
meses = {"Enero" : 31, "Febrero" : 28, "Marzo": 31, "Abril" : 30, "Mayo" : 31, "Junio" : 30
        , "Julio" : 31, "Agosto" : 31, "Septiembre" : 30, "Octubre" : 31, "Nomviembre": 30, "Diciembre" : 31}

print("2) Mostrar los días que tiene el mes de Marzo")
print(meses["Marzo"], "\n")

print("3) Crea una tupla con los keys del diccionario que se ha creado.")
print(tuple(meses.keys()), "\n")

print("4) Crea una tupla con los values del diccionario que se ha creado.")
print(tuple(meses.values()), "\n")

print("5) Calcula el tamaño del diccionario")
print(len(meses), "\n")

print("6) Borrar del diccionario los meses de Julio y Agosto")
del meses["Julio"]
del meses["Agosto"]
print(meses, "\n")

print("7) Recorrer el diccionario y mostrar por pantalla mes con los días del mes.")
for mes in meses.items():
    print(mes)

#Otra opcion...

for mes, dias in meses.items():
    print(f"El mes {mes} tiene {dias} días.")
    