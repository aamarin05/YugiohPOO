from Carta import *
from Jugador import *
class Tablero:
  def __init__(self):
    self.__cartasMonstruo = ["No hay Carta", "No hay Carta", "No hay Carta"]
    self.__cartasEspeciales = ["No hay Carta", "No hay Carta", "No hay Carta"]
    self.__cartasJugador = [self.__cartasMonstruo, self.__cartasEspeciales]
  def _str_(self):
    print(f"Tablero\nMonstruo: [{self.__cartasJugador[0][0]}] [{self.__cartasJugador[0][1]}] [{self.__cartasJugador[0][2]}]\nEspeciales: [{self.__cartasJugador[1][0]}] [{self.__cartasJugador[1][1]}] [{self.__cartasJugador[1][2]}]")
    
  def seleccionarCarta(self,indice):
    print(self._str_())
    return self.__cartasJugador[1,indice]#Retorna la Carta del indice indicado
  def removerCarta(self,carta):
    for f,c in self.__cartasJugador:
      if self.__cartasJugador[f][c] == carta:
        self.__cartasJugador[f][c]= "No hay Carta"
  def getMonstruos(self):
    return self.__cartasMonstruo
  def getEspeciales(self):
    return self.__cartasEspeciales
  def getCartas(self):
    return self.__cartasJugador