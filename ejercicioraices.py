import math
print('CALCULO DE RAICES')
a = float(input('Introduzca el valor a: '))
b = float(input('Introduzca el valor b: '))
c = float(input('Introduzca el valor c: '))

if a == 0: 
    print('INDETERMINADO') 
elif (b**2 - 4*a*c) < 0:
    print('No hay soluciones reales.')
else:
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    if x1 == x2:
        print(f'Hay un solo resultado real:\nx1 y x2 = {x1}')
    elif x1 != x2:
        print(f'Hay 2 resultados reales:\nx1 = {x1}\nx2 = {x2}')
    
