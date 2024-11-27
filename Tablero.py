from Carta import *
from Jugador import *
class Tablero:
  def __init__(self):
    self.__cartasMonstruo = []
    self.__cartasEspeciales = []
    self.__cartasJugador = [self.__cartasMonstruo, self.__cartasEspeciales]

  def _str_(self):
    monstruos = []
    especiales = []

    for i in range(3):
        if i < len(self.__cartasMonstruo):
            monstruos.append(str(self.__cartasMonstruo[i]))
        else:
            monstruos.append("No hay cartas")

    for i in range(3):
        if i < len(self.__cartasEspeciales):
            especiales.append(str(self.__cartasEspeciales[i]))
        else:
            especiales.append("No hay cartas")


    tablero = (
        f"Tablero\n"
        f"Monstruo: [{monstruos[0]}] [{monstruos[1]}] [{monstruos[2]}]\n"
        f"Especiales: [{especiales[0]}] [{especiales[1]}] [{especiales[2]}]"
    )
    return tablero



      
  def seleccionarCarta(self,indice):
    print(self._str_())
    return self.__cartasJugador[1,indice]#Retorna la Carta del indice indicado
  def removerCarta(self,carta):
    for f,c in self.__cartasJugador:
      if self.__cartasJugador[f][c] == carta:
        self.__cartasJugador.remover(self.__cartasJugador[f][c])
  def getMonstruos(self):
    return self.__cartasMonstruo
  def getEspeciales(self):
    return self.__cartasEspeciales
  def getCartas(self):
    return self.__cartasJugador