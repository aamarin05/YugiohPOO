from Deck import *
from Tablero import *

class Jugador:
  def __init__(self,nombre):
    self.__nombre = nombre
    self.__deck = Deck.crearDeck(self)
    self.__puntos = 4000
    self.__tablero = Tablero()
    self.__mano= [self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop()]

  def getNombre(self):
    return self.__nombre
  def getPuntos (self):
    return self.__puntos
  def setPuntos (self, puntos):
    self.__puntos = puntos
  def getMano (self):
    return self.__mano
  def tomarCarta(self):
    self.__mano.append(self.__deck.pop())
  def agregarCartaTablero(self,carta):
      if isinstance(carta,CartaMonstruo):
        if "No hay carta" in self.__tablero.__cartasjugador[0]:
          indice= self.__tablero.__cartasjugador[0].index("No hay carta")
          self.__tablero.__cartasjugador[0][indice]= carta
        else:
          print("Espacio para carta tipo Monstruo lleno en el tablero")
      elif isinstance(carta,CartaMagica) or isinstance(carta,CartaMonstruo):
        if "No hay carta" in self.__tablero.__cartasjugador[1]:
          indice= self.__tablero.__cartasjugador[1].index("No hay carta")
          self.__tablero.__cartasjugador[1][indice]= carta
        else:
          print("Espacio para cartas tipo Magica o Trampa lleno en el tablero")