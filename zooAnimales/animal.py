class Animal:
    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona ):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona

    def movimiento():
        return "dezplazarse"
    
    def totalPorTipo():
        print("Mamiferos: " + Mamifero.cantidadMamiferos() + "\nAves: " + Ave.cantidadAves() + "\nReptiles: " + Reptil.cantidadReptiles() + "\nPeces: " + Pez.cantidadPeces() + "\nAnfibios: " + Anfibio.cantidadAnfibios()) 

    def __str__():
        string = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y  mi genero es {self._genero}"
        if self._zona != None:
            string += f", la zona en la que me ubico es {self._zona}, en el {self._zoo}"
        return string

    def setNombre(self,nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre
    def setEdad(self,edad):
        self._edad = edad
    def getEdad(self):
        return self._edad
    def setHabitat(self,habitat):
        self._habitat = habitat
    def getHabitat(self):
        return self._habitat
    def setGenero(self,genero):
        self._genero = genero
    def getGenero(self):
        return self._genero
    def setZona(self,zona):
        self.zona = zona
    def getZona(self):
        return self._zona
    @classmethod
    def setTotalAnimales(cls,totalAnimales):
        cls._totalAnimales = totalAnimales
    @classmethod 
    def getTotalAnimales(cls):
        return cls._totalAnimales


    
    





