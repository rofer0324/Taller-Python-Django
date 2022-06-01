"""
Ejercicio 2:
1) Crear una lista con los meses del año
2) Selecciona el mes noveno, y el penúltimo
3) Crea una lista con los meses de verano (septimo a noveno)
4) Crea una lista con los meses de verano en orden inverso
"""

print("1) Crear una lista con los meses del año")
lista = ["Enero","Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Nomviembre", "Diciembre"]
print(lista, "\n")

print("2) Selecciona el mes noveno, y el penúltimo")
print(lista[9:11], "\n")

print("Crea una lista con los meses de verano (septimo a noveno)")
verano = lista[0:3]
print(verano, "\n")

print("4) Crea una lista con los meses de verano en orden inverso")
verano.reverse()
print(verano, "\n")


