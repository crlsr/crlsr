import random
#Definicion de variables y listas.
ps_jugador = 100
ps_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

# (daño, dañodef, nombre ataque)

#Diccionario ataques (jugador).
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
    while ps_jugador>0 and ps_oponente>0: 
    #Turno Jugador:
        ataque_jugador = input("ataque: ")
        ataque_jugador.lower()
        if ataque_jugador == ataques_jugador['ataque_1'][2]: #malicioso
            print('Has usado malicioso... Un ataque de tipo NORMAL ')
            print('La defensa de squirtle bajado')
            defensa_oponente = defensa_oponente - ataques_jugador['ataque_1'][1]
            if defensa_oponente <= 0:
                defensa_oponente = 1
        elif ataque_jugador == ataques_jugador['ataque_2'][2]: #placaje
            print('Has usado placaje... Un ataque de tipo NORMAL')
            print('Los ps de Squirtle han bajado')
            ps_oponente -= ataques_jugador['ataque_2'][0] * (100/defensa_oponente)
        elif ataque_jugador == ataques_jugador['ataque_3'][2]: #ascuas
            print('Has usado ascuas... Un ataque de tipo FUEGO')
            print('Ataque poco efectivo...')
            print('Los ps de Squirtle han bajado poco')
            ps_oponente -= ataques_jugador['ataque_3'][0]
        else:
            print('Que estas haciendo? Tus ataques son placaje, malicioso y ascuas siuuuu' ) 
            continue
        #Turno Oponente:
        ataque_oponente = random.randrange(1,3+1)
        if ataque_oponente == 1: #latigo
            print('Squirtle ha usado latigo... Un ataque de tipo NORMAL')
            print('La defensa de Charmander ha bajado')
            print('Charmander ha perdido vida!')
            ps_jugador -= 10
            defensa_jugador -= 10
            if defensa_jugador <= 0:
                defensa_jugador = 1
        elif ataque_oponente == 2:
            print('Squirtle ha usado placaje... Un ataque de tipo NORMAL')
            print('Charmander ha perdido vida!')
            ps_jugador -= 35 * (defensa_jugador/100) #placaje
        elif ataque_oponente == 3:
            print('Squirtle ha usado Pistola Agua... Un ataque de tipo AGUA')
            print('Ataque crítico')
            print('Charmander ha perdido mucha vida!')
            ps_jugador -= 40 #pistola de agua.
        #Revisión de vida post turno
        if ps_jugador < 0: 
            ps_jugador = 0
            print('Has perdido!')
        elif ps_oponente < 0:
            ps_oponente = 0
            print('Has ganado!')
        print(f'Charmader {ps_jugador}ps')
        print(f'Squirtle {ps_oponente}ps')
elif elección == 2:
    print('Bien bello pues, te asustaste chico?')
    quit()
else: 
    print('??')
    quit()
    
    
