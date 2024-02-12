#Definición de los tipos de vehiculos
class VehiculoAereo:
    def __init__(self, marca, color, precio, tipo):
        self.marca = marca
        self.color = color
        self.precio = str(precio) + 'M$'
        self.tipo = tipo
        
class VehiculoTerrestre:
    def __init__(self, marca, color, precio, modelo):
        self.marca = marca
        self.color = color
        self.precio = precio + '$'
        self.modelo = modelo
        
class VehiculoMarino:
    def __init__(self, marca, color, precio, tipo):
        self.marca = marca
        self.color = color
        self.precio = precio + '$'
        self.tipo = tipo
        

avion1 = VehiculoAereo('United Airlines', 'Plateado', 320, 'Avión Comercial')
avion2 = VehiculoAereo('Boeing Defense', 'Gris', 150, 'Avión de Combate')
avion3 = VehiculoAereo('McDonnell Douglas Aircraft Corporation', 'Plateado', 88.4, 'Avión Cisterna')

carro1 = VehiculoTerrestre('Audi', 'Naranja', '161,395', 'r8')
carro2 = VehiculoTerrestre('Nissan', 'Azul', '113,929', 'GT-R R35')
carro3 = VehiculoTerrestre('Ferrari', 'Rojo', '	282.724', 'F40')

barco1 = VehiculoMarino('BAE Systems Maritime - Naval Ships', 'Gris', '4.200M', 'Buque de Guerra')
barco2 = VehiculoMarino('Amels', 'Blanco', '117,551,922', 'Yate')
barco3 = VehiculoMarino('Beneteau', 'Blanco', '945.000', 'Barco de Pesca' )
        
        
print(carro3.marca)
        