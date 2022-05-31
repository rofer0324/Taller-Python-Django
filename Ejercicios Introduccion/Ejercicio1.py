#Para resolver cada punto del Ejercico 1, es necesario quitar las lineas de comentario de las lineas de codigo.

"""
Ejercicio 1:
1) Rellenar la cadena del abecedario con el símbolo # hasta completar 30 caracteres.
2) Mirar la longitud de la cadena abecedario.
3) Poner en mayúsculas y en minúsculas la cadena.
4) Buscar en la cadena abecedario la letra R y saber su posicion
5) Crea otra cadena con las 5 letras que van después de la n
6) Reemplazar la letra Z por Hola.
7) Obtener una lista de la cadena abecedario y separarla por la letra i
8) Unir la lista anterior con el símbolo “-” usando ‘-’.join(lista).
"""

import string

"""string.ascii_letters #Impresion de todas las letras del abecedario.
abecedario = string.ascii_lowercase #Abecedario en minuscula.
abecedario = string.ascii_uppercase #Abecedario en mayuscula.
del abecedario #se borra el contenido de la variable (libera memoria)"""

print("1) Rellenar la cadena del abecedario con el símbolo # hasta completar 30 caracteres.")
abecedario = string.ascii_lowercase
print(abecedario)
#print(len(abecedario))
abecedario = abecedario + '#'*4
print(len(abecedario))
print(abecedario, "\n")

del abecedario

print("2) Mirar la longitud de la cadena abecedario.")
abecedario = string.ascii_lowercase
abecedario = abecedario + '#'*4
print(len(abecedario) , "\n")

del abecedario

print("3) Poner en mayúsculas y en minúsculas la cadena.")
abecedario = string.ascii_uppercase
print(abecedario, "\n")
abecedario = string.ascii_lowercase
print(abecedario, "\n")

del abecedario

print("4) Buscar en la cadena abecedario la letra R y saber su posicion")
abecedario = string.ascii_uppercase
print(abecedario)
print(abecedario.find('R'), "\n")

del abecedario

print("5) Crea otra cadena con las 5 letras que van después de la n")
abecedario = string.ascii_uppercase
print(abecedario.find('N'))

#Despliega la subcadena que hay entre N y N+5. #Tambien es llamado a esto Slicing.
cadena = abecedario[abecedario.find('N'): abecedario.find('N')+5]
print(cadena, "\n")

del abecedario

print("6) Reemplazar la letra Z por Hola.")
abecedario = string.ascii_uppercase