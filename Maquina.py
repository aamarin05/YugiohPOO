from Jugador import *
class Maquina (Jugador):
  def __init__(self):
    super().__init__()
    self.__nombre = "Maquina"
    self.__deck = Deck.crearDeck(self)
    self.__puntos = 4000
    self.__tablero = Tablero()
    self.__mano= [self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop()]