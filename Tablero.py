from Carta import *
from Jugador import *
from CartaMonstruo import*
from CartaMagica import *
from CartaTrampa import *
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


  def removerCarta(self,carta):
    if isinstance(carta, CartaMonstruo):
      if carta in self.__cartasMonstruo:
        self.__cartasMonstruo.remove(carta)
    else:
      if carta in self.__cartasEspeciales:
          self.__cartasEspeciales.remove(carta)

  def getMonstruos(self):
    return self.__cartasMonstruo
  def getEspeciales(self):
    return self.__cartasEspeciales
  def getCartas(self):
    return self.__cartasJugador