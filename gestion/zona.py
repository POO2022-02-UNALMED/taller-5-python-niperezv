class Zona:
    def __init__(self, nombre, zoo=None):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=[]
        
    #metodos zoo
    def getZoo(self):
        return self._zoo

    def setZoo(self,zoo):
        self._zoo=zoo

    #metodos nombre
    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre=nombre

    #metodos animales
    def getAnimales(self):
        self._animales
    
    def setAnimales(self, animales):
        self._animales.append(animales)
    
    #metodo cantidadAnimales
    def cantidadAnimales(self):
        return len(self._animales)

    #metodo agregar
    def agregarAnimales(self, animal):
        self._animales.append(animal)
