"""
Ejercicio 5: Condicional
Dependiendo del valor que se le asigne a una variable llamada mes nos tendrá que dar el número de días que tiene ese mes en otra variable llamada num_dias.
"""

print("1. Dependiendo del valor que se le asigne a una variable llamada mes nos tendrá que dar el número de días que tiene ese mes en otra variable llamada num_dias.")

meses = {"Enero" : 31, "Febrero" : 28, "Marzo": 31, "Abril" : 30, "Mayo" : 31, "Junio" : 30
        , "Julio" : 31, "Agosto" : 31, "Septiembre" : 30, "Octubre" : 31, "Nomviembre": 30, "Diciembre" : 31}

mes_in = input("\nIntroduzca el mes para saber el numero de dias que tiene: ")
num_dias = 0

for mes, dias in meses.items():
    if mes == mes_in:
        num_dias = dias

print(num_dias)