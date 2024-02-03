import random
#Definicion de variables y listas:

#Definición ataques:
def placaje(ps, defensa):
    ps = ps - 35 * (100/defensa)
    if ps < 0:
        ps = 0
    return ps, defensa

def malicioso (ps, defensa):
    defensa = defensa - 10
    if defensa <= 0:
        defensa = 1
    return ps, defensa

def ascuas(ps, defensa):
    ps = ps - 20
    if ps < 0:
        ps = 0
    return ps, defensa
    
def latigo(ps, defensa):
    defensa = defensa - 10
    ps = ps - 10
    if ps < 0:
        ps = 0
    elif defensa <= 0:
        defensa = 1
    return ps, defensa

def pistola_agua(ps, defensa):
    ps = ps - 40
    if ps < 0:
        ps = 0
    return ps, defensa

#Definición atributos: (vida, defensa)
atributo_jugador = 100,100
atributo_oponente = 100,100

#Definición nombres jugadores:
nombre_jugador = input('Introduce tu nombre entrenador: ')
nombre_oponente = input(f'Elige a tu oponente {nombre_jugador}: ')


#Elección Inicio.
elección = int(input(f'Hola! soy {nombre_oponente}, estas listo para esta batalla pokemon? \nSeleccione su decisión eligiendo un número\n1~ Si.\n2~ No.\n'))

if elección == 1: #Comienza la batalla!
    print(f'Ok {nombre_jugador} preparate para esta batalla pokemon!')
    print("Tu pokemon es: Charmander \nEl pokemon de tu enemigo es: Squirtle \n")
    while atributo_jugador[0]>0 and atributo_oponente[0]>0:
    #Turno Jugador:
        ataque_jugador = input("Escriba su ataque: ") #Elección de ataque
        ataque_jugador.lower()
        if ataque_jugador == 'placaje': #Placaje
            print('Has usado placaje... Un ataque de tipo NORMAL')
            print('Los ps de Squirtle han bajado')
            atributo_oponente = placaje(atributo_oponente[0], atributo_oponente[1])
        elif ataque_jugador == 'malicioso': #Malicioso
            print('Has usado malicioso... Un ataque de tipo NORMAL ')
            print('La defensa de squirtle bajado')
            atributo_oponente = malicioso(atributo_oponente[0], atributo_oponente[1])
        elif ataque_jugador == 'ascuas': #Ascuas
            print('Has usado ascuas... Un ataque de tipo FUEGO')
            print('Ataque poco efectivo...')
            print('Los ps de Squirtle han bajado poco')
            atributo_oponente = ascuas(atributo_oponente[0], atributo_oponente[1])
        else:
            print('Que estas haciendo? Tus ataques son placaje, malicioso y ascuas siuuuu' ) 
            continue
    #Turno Oponente:
        ataque_oponente = random.randrange(1,3+1)
        if ataque_oponente == 1: #Latigo
            print('Squirtle ha usado latigo... Un ataque de tipo NORMAL')
            print('La defensa de Charmander ha bajado')
            print('Charmander ha perdido vida!')
            atributo_jugador = latigo(atributo_jugador[0], atributo_jugador[1])
        elif ataque_oponente == 2: #Placaje
            print('Squirtle ha usado placaje... Un ataque de tipo NORMAL')
            print('Charmander ha perdido vida!')
            atributo_jugador = placaje(atributo_jugador[0], atributo_jugador[1])
        elif ataque_oponente == 3: #Pistola Agua
            print('Squirtle ha usado Pistola Agua... Un ataque de tipo AGUA')
            print('Ataque crítico')
            print('Charmander ha perdido mucha vida!')
            atributo_jugador = pistola_agua(atributo_jugador[0], atributo_jugador[1])
    
    #Revisión de vida post turno
        if atributo_jugador[0] == 0: 
                print('Has perdido!')
        elif atributo_oponente[0] == 0:
                print('Has ganado!')
        print(f'Charmader {atributo_jugador[0]}ps')
        print(f'Squirtle {atributo_oponente[0]}ps')
elif elección == 2: #Niegas la batalla
    print('Bien bello pues, te asustaste chico?')
    quit()
else: #Caracter incorrecto
    print('??')
    quit()
