from Carta import *
from Jugador import *
class Tablero:
  def init(self):
    self.__cartasjugador = [[None, None, None], [None, None, None]] 
  def _str_(self):
    print(f"Tablero
            \nMonstruo: [{self._cartasjugador[0][0]}] [{self.cartasjugador[0][1]}] [{self._cartasjugador[0][2]}]
            \nMagicas: [{self._cartasjugador[1][0]}] [{self.cartasjugador[1][1]}] [{self._cartasjugador[1][2]}]
            ")
  def seleccionarCarta(self,indice):
    print(self._str_())
    return self.__cartasjugador[1,indice]#Retorna la Carta del indice indicado