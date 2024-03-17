class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    def cantidadAnfibios():
        cantidadAnfibios = 0
        for Anfibio in listado:
            cantidadAnfibios += 1
        return cantidadAnfibios

    def movimiento():
        return "saltar"
    
    def crearRana( nombre, edad, genero):
        anfibio = Anfibio(nombre, edad, "selva" , genero, "rojo", True)
        _listado.append(anfibio)
        ranas += 1

    def crearSalamandra( nombre, edad, genero):
        anfibio = Anfibio(nombre, edad, "selva" , genero, "negro y amarillo", False)
        _listado.append(anfibio)
        salamandras += 1
    
    @classmethod
    def  getListado(cls):
        return cls.listado
    @classmethod
    def setListado(cls,listado):
        cls._listado = listado
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self,colorPiel):
        self._colorPiel = colorPiel
    def getVenenoso(self):
        return self._venenoso
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso