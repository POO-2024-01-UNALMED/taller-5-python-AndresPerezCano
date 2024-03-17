from zooAnimales.animal import Animal

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
        Pez._listado.append(pez)
        Pez.salmones += 1
        return pez

    def crearBacalao( nombre, edad, genero):
        pez = Pez(nombre, edad, "oceano" , genero, "gris", 6)
        Pez._listado.append(pez)
        Pez.bacalaos += 1
        return pez
    
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
    def getNombre():
        return super().getNombre()
    def setNombre(nombre):
        super().setNombre(self,nombre)
    def getEdad():
        return super().getEdad()
    def setEdad(edad):
        super().setEdad(self,edad)
    def getHabitat():
        return super().getHabitat()
    def setHabitat(habitat):
        super().setHabitat(self,habitat)
    def getGenero():
        return super().getGenero()
    def setGenero(genero):
        super().setGenero(self,genero)