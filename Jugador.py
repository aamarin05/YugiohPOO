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
    return self.__deck.pop()
  def agregarCartaTablero(self,indice):
      carta = self.getMano()[indice]
      if isinstance(carta,CartaMonstruo):
        if len(self.__tablero.getMonstruos()) < 3:
          self.__tablero.getMonstruos().append(carta)
          print(f"Se ha agregado la carta monstruo {carta} al tablero")
        else:
          print("Espacio para carta tipo Monstruo lleno en el tablero")
      elif isinstance(carta,CartaMagica) or isinstance(carta,CartaMonstruo):
        if len(self.__tablero.getEspeciales()) < 3:
          self.__tablero.getEspeciales().append(carta)
          print(f"Se ha agregado la carta especial {carta} al tablero")
        else:
          print("Espacio para cartas tipo Magica o Trampa lleno en el tablero")