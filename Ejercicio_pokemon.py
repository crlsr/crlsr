import random
#Definicion de variables y listas.
ps_jugador = 100
ps_oponente = 100
defensa_oponente = 100
defensa_jugador = 100
at_jugador = ['malicioso','placaje', 'ascuas']

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
        if ataque_jugador == at_jugador[0]: #malicioso
            print('Has usado malicioso...')
            print('La defensa de squirtle bajado')
            defensa_oponente = defensa_oponente - 10
            if defensa_oponente <= 0:
                defensa_oponente = 1
        elif ataque_jugador == at_jugador[1]: #placaje
            print('Has usado placaje...')
            print('Los ps de Squirtle han bajado')
            ps_oponente -= 35 * (100/defensa_oponente)
        elif ataque_jugador == at_jugador[2]: #ascuas
            print('Has usado ascuas...')
            print('Ataque poco efectivo')
            print('Los ps de Squirtle han bajado poco')
            ps_oponente -= 20
        else:
            print('Que estas haciendo? Tus ataques son placaje, malicioso y ascuas siuuuu' ) 
            continue
        #Turno Oponente:
        ataque_oponente = random.randrange(1,3+1)
        if ataque_oponente == 1: #latigo
            print('Squirtle ha usado latigo...')
            print('La defensa de Charmander ha bajado')
            defensa_jugador -= 10
            if defensa_jugador <= 0:
                defensa_jugador = 1
        elif ataque_oponente == 2:
            print('Squirtle ha usado placaje...')
            print('Charmander ha perdido vida!')
            ps_jugador -= 35 * (defensa_jugador/100) #placaje
        elif ataque_oponente == 3:
            print('Squirtle ha usado Pistola Agua...')
            print('Ataque crítico')
            print('Charmander ha perdido mucha vida!')
            ps_jugador -= 40 #pistola de agua.
        #Revisión de vida post turno
        if ps_jugador < 0 or ps_oponente < 0:
            ps_jugador = 0
            ps_oponente = 0
        print(f'Charmader {ps_jugador}ps')
        print(f'Squirtle {ps_oponente}ps')
elif elección == 2:
    print('Bien bello pues, te asustaste chico?')
else: 
    print('??')
    quit()
    

    
        