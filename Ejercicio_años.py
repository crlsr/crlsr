
#Border cases (errores de logica del programador en los condicionales).
#(then = :). 

#Bug = Error del programa a causa del programador.

'''
#Ejercicio años (Condicionales):
años = int(input('Diga un año entre 1900 y 2199: '))
contador_años = int()

if años >= 1900 and años <= 2199:
        contador_años += (años - 1900)//4
        if años == 2100:
            contador_años -= 1
else:
    print('Valor no valido')
       
print(contador_años)
'''

#Ejercicio años (bucles)
años = int(input('Diga un año entre 1900 y 2199: '))
if años < 1900 and años > 2199:
    print('Esta fuera del rango')
else:
    contador = 0
    for i in range(1900, años + 1):
        if i%4 != 0 or i%100 == 0 and i%400 != 0:
            continue 
        contador += 1
print(f'La cantidad de años viciestos desde 1900 hasta {años} es igual a {contador}')

#Hacer programa que calcule con la resolvente y arreglar codigo de ejercicio.py (concatenarlo todo en un mismo codigo).