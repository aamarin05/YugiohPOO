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
  def setNombre (self, nombre):
    self.__nombre = nombre
  def getDeck (self):
    return self.__deck
  def setDeck (self, deck):
    self.__deck = deck
  def getPuntos (self):
    return self.__puntos
  def setPuntos (self, puntos):
    self.__puntos = puntos
  def getMano (self):
    return self.__mano

  def tomarCarta(self):
    return self.__deck.pop()
  def contar_cartas_tipo(self, tipo):
    for carta in self.__mano:
      return sum(isinstance(carta, tipo))
  def agregarCartaTablero(self,carta):
    if (len(self.__tablero)<=6):
      if isinstance(carta,CartaMonstruo):
        if self.contar_cartas_tipo(CartaMonstruo) < 3:
          self.__tablero.__cartas.append(carta)
          self.__mano.remove(carta)
        elif isinstance(carta, (CartaMagica, CartaTrampa)):
          if self.contar_cartas_tipo(CartaMagica) + self.contar_cartas_tipo(CartaTrampa) < 3:
            self.__tablero.__cartas.append(carta)
            self.__mano.remove(carta)
  def seleccionarCartaTablero(self,indice):
    return self.__tablero()[indice]