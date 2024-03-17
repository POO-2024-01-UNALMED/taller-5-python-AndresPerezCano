from zooAnimales import Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas

    def cantidadMamiferos():
        cantidadMamiferos = 0
        for mamifero in listado:
            cantidadMamiferos += 1
        return cantidadMamiferos
    
    def crearCaballo( nombre, edad, genero):
        mamifero = Mamifero(nombre, edad, "pradera" , genero, True, 4)
        _listado.append(mamifero)
        caballos += 1

    def crearLeon( nombre, edad, genero):
        mamifero = Mamifero(nombre, edad, "selva" , genero, True, 4)
        _listado.append(mamifero)
        leones += 1
    
    @classmethod
    def  getListado(cls):
        return cls.listado
    @classmethod
    def setListado(cls,listado):
        cls._listado = listado
    def isPelaje(self):
        return self._pelaje
    def setPelaje(self,pelaje):
        self._pelaje = pelaje
    def getPatas(self):
        return self._patas
    def setPatas(self,patas):
        self._patas = patas
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

    

