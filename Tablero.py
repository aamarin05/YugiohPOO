from Carta import *
from Jugador import *
class Tablero:
  def init(self):
    self.__cartasjugador = [["No hay Carta", "No hay Carta", "No hay Carta"], ["No hay Carta", "No hay Carta", "No hay Carta"]] 
  def _str_(self):
    print(f"Tablero
            \nMonstruo: [{self.__cartasjugador[0][0].__str__()}] [{self.__cartasjugador[0][1].__str__()}] [{self.__cartasjugador[0][2].__str__()}]
            \nEspeciales: [{self.__cartasjugador[1][0].__str__()}] [{self.__cartasjugador[1][1].__str__()}] [{self.__cartasjugador[1][2].__str__()}]
            ")
    
  def seleccionarCarta(self,indice):
    print(self._str_())
    return self.__cartasjugador[1,indice]#Retorna la Carta del indice indicado
  def removerCarta(self,carta):
    for f,c in self.__cartasjugador:
      if self.__cartasjugador[f][c] == carta:
        self.__cartasjugador[f][c]= "No hay Carta"