from gestion.zona import Zona

class Animal: 
    _totalAnimales=0
    _zona=[]
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        Animal._totalAnimales+=1

    def getTotalAnimales(self):
        return self._totalAnimales

    def setTotalAnimales(self, totalAnimales):
        self._totalAnimales=totalAnimales

    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre=nombre

    def getEdad(self):
        return self._edad

    def setEdad(self,edad):
        self._edad=edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat=habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero=genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona=zona

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return f"Mamiferos : {Mamifero.cantidadMamiferos()}\nAves : {Ave.cantidadAves()}\nReptiles : {Reptil.cantidadReptiles()}\nPeces : {Pez.cantidadPeces()}\nAnfibios : {Anfibio.cantidadAnfibios()}"
     
    def toString(self):
        if self._zona==[]:
            return "Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad)+", habito en "+self._habitat+" y mi genero es "+self._genero
        else: 
            return "Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad)+", habito en "+self._habitat+" y mi genero es "+self._genero+", la zona en la que me ubico es: "+self._zona.getNombre(),"el zoologico es: "+ Zona.getZoo().index(0).getNombre()
