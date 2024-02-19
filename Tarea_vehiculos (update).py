import os
#Definición de la clase padre
class Vehiculo:
    def __init__(self, marca, color, precio, tipo):
        self.marca = marca
        self.color = color
        self.precio = str(precio)
        self.tipo = tipo

#Subclases de los vehiculos:
class VehiculoAereo(Vehiculo):
    def __init__(self, marca, color, precio, tipo):
        super().__init__(marca, color, precio, tipo)
        
    def __str__(self):
        return f'Vehiculo: {self.marca} ({self.tipo})\nColor: {self.color}\nPrecio: {self.precio}'
    def __repr__(self):
        return f'{self.marca} ({self.tipo})'
        
class VehiculoTerrestre(Vehiculo):
    def __init__(self, marca, color, precio, tipo):
        super().__init__(marca, color, precio, tipo)
        
    def __str__(self):
        return f'Vehiculo: {self.marca} ({self.tipo})\nColor: {self.color}\nPrecio: {self.precio}'
        
class VehiculoMarino(Vehiculo):
    def __init__(self, marca, color, precio, tipo):
        super().__init__(marca, color, precio, tipo)
        
    def __str__(self):
        return f'Vehiculo: {self.marca} ({self.tipo})\nColor: {self.color}\nPrecio: {self.precio}'

#Creación del catalogo
def menu_vehiculos(tipo1: [object], tipo2: [object], tipo3: [object]):
    print('*'*45, 'Bienvenido al Catalogo de Vehiculos','*'*45)
    while True:
        elección1 = int(input('Nuestro catalogo posee:\n>1. Aviones\n>2. Barcos\n>3. Carros\nElija el número del tipo de vehiculo que desea revisar.\n>(Escriba 0 si desea salir del catalogo).\n>(Escriba un número cualquiera para refrescar el catalogo).\n\n>>> '))
        os.system('clear')
        if elección1 == 1:
            nro = 0
            for i in tipo1:
                nro += 1
                print(f'{nro}.', i, '\n')
        elif elección1 == 2:
            nro = 0 
            for i in tipo2:
                nro += 1
                print(f'{nro}.', i, '\n')
        elif elección1 == 3:
            nro = 0 
            for i in tipo3:
                nro += 1
                print(f'{nro}.', i, '\n')
        elif elección1 == 0:
            break
        else:
            os.system('clear')
    print('Gracias por ojear nuestro catalogo de vahiculos!.')
        
#Creación de instancias:
avion1 = VehiculoAereo('United Airlines', 'Plateado', 320000000, 'Avión Comercial')
avion2 = VehiculoAereo('Boeing Defense', 'Gris', 150000000, 'Avión de Combate')
avion3 = VehiculoAereo('McDonnell Douglas Aircraft Corporation', 'Plateado', 88400000, 'Avión Cisterna')

carro1 = VehiculoTerrestre('Audi', 'Naranja', 161395, 'r8')
carro2 = VehiculoTerrestre('Nissan', 'Azul', 113929, 'GT-R R35')
carro3 = VehiculoTerrestre('Ferrari', 'Rojo', 282724, 'F40')

barco1 = VehiculoMarino('BAE Systems Maritime - Naval Ships', 'Gris', 4200000000, 'Buque de Guerra')
barco2 = VehiculoMarino('Amels', 'Blanco', 117551922, 'Yate')
barco3 = VehiculoMarino('Beneteau', 'Blanco', 945000, 'Barco de Pesca' )
        
#Lista de instancias:
aviones = [avion1, avion2, avion3]
barcos = [barco1, barco2, barco3]
carros = [carro1, carro2, carro3]

#Ejecución  del menú/catalogo de vehiculos.
menu_vehiculos(aviones, barcos, carros)



       

                