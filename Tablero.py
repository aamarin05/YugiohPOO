from Carta import *
from Jugador import *
class Tablero:
  def init(self):
    self.__cartasjugador = [["No hay carta", "No hay carta", "No hay carta"], ["No hay carta", "No hay carta", "No hay carta"]] 

  def getCartasMonstruo(self):
    return self.__cartasjugador[0]
  def getCartasTrampaoMagica(self):
    return self.__cartasjugador[1]
  def seleccionarCarta(self,indice):
    print(self._str_())
    return self.__cartasjugador[1,indice]#Retorna la Carta del indice indicado
  def _str_(self):
    print(f"Tablero
            \nMonstruo: [{self.__cartasjugador[0][0].__str__()}] [{self.__cartasjugador[0][1].__str__()}] [{self.__cartasjugador[0][2].__str__()}]
            \nMagicas: [{self.__cartasjugador[1][0].__str__()}] [{self.__cartasjugador[1][1].__str__()}] [{self.__cartasjugador[1][2].__str__()}]
            ")
