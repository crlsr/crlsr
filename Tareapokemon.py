import random
#Definicion de variables y listas.
#Atributos jugador: (vida, defensa)

atributo_jugador = 100,100
atributo_oponente = 100,100

#Diccionario ataques (jugador). Atributos ataques: (daño, dañodef, nombre ataque).
ataques_jugador = {
    'ataque_1' : (0, 10, 'malicioso'),
    'ataque_2' : (35, 0, 'placaje'),
    'ataque_3' : (20, 0, 'ascuas')
}

#Nombres.
nombre_jugador = input('Introduce tu nombre entrenador: ')
nombre_oponente = input(f'Elige a tu oponente {nombre_jugador}: ')

#Elección Inicio.
elección = int(input(f'Hola! soy {nombre_oponente}, estas listo para esta batalla pokemon? \nSeleccione su decisión eligiendo un número\n1~ Si.\n2~ No.\n'))

if elección == 1:
    print(f'Ok {nombre_jugador} preparate para esta batalla pokemon!')
    print("Tu pokemon es: Charmander \nEl pokemon de tu enemigo es: Squirtle \n")
    while atributo_jugador[0]>0 and atributo_oponente[0]>0: 
    #Turno Jugador:
        ataque_jugador = input("ataque: ")
        ataque_jugador.lower()
        if ataque_jugador == ataques_jugador['ataque_1'][2]: #malicioso
            print('Has usado malicioso... Un ataque de tipo NORMAL ')
            print('La defensa de squirtle bajado')
            atributo_oponente = atributo_oponente[0], atributo_oponente[1] - ataques_jugador['ataque_1'][1]
            if atributo_oponente[1] <= 0:
                atributo_oponente = atributo_oponente[0], 1
        elif ataque_jugador == ataques_jugador['ataque_2'][2]: #placaje
            print('Has usado placaje... Un ataque de tipo NORMAL')
            print('Los ps de Squirtle han bajado')
            atributo_oponente = atributo_oponente[0] - ataques_jugador['ataque_2'][0] * (100/atributo_oponente[1]), atributo_oponente[1]
        elif ataque_jugador == ataques_jugador['ataque_3'][2]: #ascuas
            print('Has usado ascuas... Un ataque de tipo FUEGO')
            print('Ataque poco efectivo...')
            print('Los ps de Squirtle han bajado poco')
            atributo_oponente = atributo_oponente[0] - ataques_jugador['ataque_3'][0], atributo_oponente[1]
        else:
            print('Que estas haciendo? Tus ataques son placaje, malicioso y ascuas siuuuu' ) 
            continue
        #Turno Oponente:
        ataque_oponente = random.randrange(1,3+1)
        if ataque_oponente == 1: #latigo
            print('Squirtle ha usado latigo... Un ataque de tipo NORMAL')
            print('La defensa de Charmander ha bajado')
            print('Charmander ha perdido vida!')
            atributo_jugador = atributo_jugador[0] - 10, atributo_jugador[1]
            atributo_jugador = atributo_jugador[0], atributo_jugador[1] - 10
            if atributo_jugador[1] <= 0:
                atributo_jugador = atributo_jugador[0], 1
        elif ataque_oponente == 2:
            print('Squirtle ha usado placaje... Un ataque de tipo NORMAL')
            print('Charmander ha perdido vida!')
            atributo_jugador = atributo_jugador[0] - 35 * (atributo_jugador[1]/100), atributo_jugador[1] #placaje
        elif ataque_oponente == 3:
            print('Squirtle ha usado Pistola Agua... Un ataque de tipo AGUA')
            print('Ataque crítico')
            print('Charmander ha perdido mucha vida!')
            atributo_jugador = atributo_jugador[0] - 40, atributo_jugador[1] #pistola de agua.
        #Revisión de vida post turno
        if atributo_jugador[0] < 0: 
            atributo_jugador = 0, atributo_jugador[1]
            print('Has perdido!')
        elif atributo_oponente[0] < 0:
            atributo_oponente = 0, atributo_oponente[1]
            print('Has ganado!')
        print(f'Charmader {atributo_jugador[0]}ps')
        print(f'Squirtle {atributo_oponente[0]}ps')
elif elección == 2:
    print('Bien bello pues, te asustaste chico?')
    quit()
else: 
    print('??')
    quit()
    
    
