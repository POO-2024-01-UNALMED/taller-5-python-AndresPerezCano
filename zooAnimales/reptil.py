from zooAnimales import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    def cantidadReptiles():
        cantidadReptiles = 0
        for reptil in listado:
            cantidadReptiles += 1
        return cantidadReptiles

    def movimiento():
        return "reptar"
    
    def crearIguana( nombre, edad, genero):
        reptil = Reptil(nombre, edad, "humedal" , genero, "verdes", 3)
        _listado.append(reptil)
        iguanas += 1

    def crearSerpiente( nombre, edad, genero):
        reptil = Reptil(nombre, edad, "jungla" , genero, "blanco", 1)
        _listado.append(reptil)
        serpientes += 1
    
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
    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self,largoCola):
        self._largoCola = largoCola