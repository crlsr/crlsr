print('INGREDIENTES - AREPA')
#Creación de la arepa.
agua = int(input("Cuantas tazas de agua?: "))
harina = int(input("Cuantas tazas de harina?: "))
sal = float(input("Cuantas cucharadas de sal?: "))
aceite = float(input("Cuantas cucharadas de aceite?: "))
boul = agua + harina + sal
budare = aceite + boul 
print(f'Cantidad de arepa {budare}')
print('Que ingrediente deseas ?: ')


#Selección de sabores para la arepa.
sabor = int(input(('Sabores: \n 1- Jamon \n 2- Carne \n 3- Queso \n 4- Aguacate \n 5- Pollo. \n Elija el número de su ingredient.')))
if sabor == 1:
    print(f'Su cantidad de arepas {budare} son de Jamon')
elif sabor == 2:
    print(f'Su cantidad de arepas {budare} son de carne')
elif sabor == 3:
    print(f'Su cantidad de arepas {budare} son de queso')
elif sabor == 4:
    print(f'Su cantidad de arepas {budare} son de aguacate')
elif sabor == 5:
    print(f'Su cantidad de arepas {budare} son de pollo')
else:
    print('No tiene sabor.')
