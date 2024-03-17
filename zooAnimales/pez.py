from zooAnimales import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    def cantidadPeces():
        cantidadPeces = 0
        for pez in listado:
            cantidadPeces += 1
        return cantidadPeces

    def movimiento():
        return "nadar"
    
    def crearSalmon( nombre, edad, genero):
        pez = Pez(nombre, edad, "oceano" , genero, "rojo", 6)
        _listado.append(pez)
        salmones += 1

    def crearBacalao( nombre, edad, genero):
        pez = Pez(nombre, edad, "oceano" , genero, "gris", 6)
        _listado.append(pez)
        bacalaos += 1
    
    @classmethod
    def  getListado(cls):
        return cls.listado
    @classmethod
    def setListado(cls,listado):
        cls._listado = listado
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas = colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self,cantidadAletas):
        self._cantidadAletas = cantidadAletas