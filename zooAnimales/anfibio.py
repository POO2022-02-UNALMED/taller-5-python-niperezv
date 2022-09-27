from zooAnimales.animal import  Animal

class Anfibio(Animal):
    _listado=[]
    ranas=0
    salamandras=0
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso

    @classmethod
    def getListado(cls):
        return cls._listado  

    @classmethod
    def setListado(cls, listado):
        cls._listado=listado

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso=venenoso
        
    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel=colorPiel

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana=Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas +=1
        cls._listado.append(rana)
        return rana
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra=Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras +=1
        cls._listado.append(salamandra)
        return salamandra