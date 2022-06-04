"""
Ejercicio 3:
1) Crear una tupla con los meses del año
2) Selecciona el mes noveno, y el penúltimo
3) Selecciona todos los meses después de Agosto (no incluido)
"""

print("1) Crear una tupla con los meses del año")
tupla = ("Enero","Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Nomviembre", "Diciembre")
print(type(tupla))
print(isinstance(tupla, tuple))  #Es tupla? => True
#print(isinstance(tupla, list))  #Es lista? => False

print("2) Selecciona el mes noveno, y el penúltimo")
print(tupla[9] + ", " + tupla[11])

print("3) Selecciona todos los meses después de Agosto (no incluido)")
print(tupla[8:12]) #Slicing