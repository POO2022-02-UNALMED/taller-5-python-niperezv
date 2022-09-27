class Zoologico:
    _zonas=[]
    def __init__(self, nombre, ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion

    #metodos nombre
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre=nombre

    #metodos ubicacion
    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion=ubicacion

    #metodos zona
    def getZona(self):
        return self._zonas

    def setZona(self, zonas):
        self._zonas=zonas

    #metodo agregarZona
    def agregarZonas(self,zona):
        self._zonas.append(zona)

    #metodoCantidadTotal
    def cantidadTotalAnimales(self):
        cant=0
        for zona in self._zonas:
            cant=cant+zona.cantidadAnimales()
        return cant