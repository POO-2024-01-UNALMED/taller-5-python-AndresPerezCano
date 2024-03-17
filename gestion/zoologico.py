class Zoologico:
    def __init__(self, nombre, ubicacion, zonas):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
    
    def agregarZonas(self,zona):
        self._zonas.append(zona)
    
    def cantidadTotalAnimales():
        cantidadTotalAnimales = 0
        for zona in zonas:
            cantidadTotalAnimales += zona.cantidadAnimales()
        return cantidadTotalAnimales
    
    def setNombre(self,nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setUbicacion(self,ubicacion):
        self._ubicacion = ubicacion

    def getUbicacion(self):
        return self._ubicacion

    def setZonas(self,zonas):
        self._zonas = zonas

    def getZonas(self):
        return self._zonas


