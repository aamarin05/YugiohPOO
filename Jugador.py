from Deck import *
from Tablero import *

class Jugador:
  def __init__(self,nombre):
    self.__nombre = nombre
    self.__deck = Deck.crearDeck()
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
  def __str__(self):
    if self.__nombre=="Maquina":
      print(f"{self.__nombre} - Lp:{self.__puntos}\nEspeciales: [{self.__cartasjugador[1][0].__str__()}] [{self.__cartasjugador[1][1].__str__()}] [{self.__cartasjugador[1][2].__str()}]\nMonstruo: [{self.__cartasjugador[0][0].__str__()}] [{self.__cartasjugador[0][1].__str__()}] [{self.__cartasjugador[0][2].__str__()}]")  
    else:
      print(f"Monstruo: [{self.__cartasjugador[0][0].__str__()}] [{self.__cartasjugador[0][1].__str__()}] [{self.__cartasjugador[0][2].__str__()}]\nEspeciales: [{self.__cartasjugador[1][0].__str__()}] [{self.__cartasjugador[1][1].__str__()}] [{self.__cartasjugador[1][2].__str__()}]\n{self.__nombre} - Lp:{self.__puntos}")  
  def tomarCarta(self):
    carta=self.__deck.pop()
    self.__mano.append(carta)
    print(f"Tomaste la carta {carta.getNombre()}")
  def manoImprimir(self):
    mostrar= ""
    for carta in self.__mano:
      mostrar+= "1."+ carta.__str__()
    print(f"Usted tiene en su mano:\n{mostrar}")
  def seleccionarCartaMano(self,indice):
    return self.__mano[indice]
 
  def agregarCartaTablero(self,carta):
    pos= input("Mandar carta boca arriba o abajo?:").lower()
    if pos=="arriba":
      carta.setOrientacion(Orientacion.ARRIBA)
      modo= input("Jugar carta en Ataque o en defensa:").lower()
      if modo=="ataque":
        carta.setAtaque(Posicion.VERTICAL)
        if isinstance(carta,CartaMonstruo):
          if None in self.__tablero.__cartasjugador[0]:
            indice= self.__tablero.__cartasjugador[0].index(None)
            self.__tablero.__cartasjugador[0][indice]= carta
          else:
            print("Espacio para carta tipo Monstruo lleno en el tablero")
        elif isinstance(carta,CartaMagica) or isinstance(carta,CartaMonstruo):
          if None in self.__tablero.__cartasjugador[1]:
            indice= self.__tablero.__cartasjugador[1].index(None)
            self.__tablero.__cartasjugador[1][indice]= carta
          else:
            print("Espacio para cartas tipo Magica o Trampa lleno en el tablero")
      if modo=="defensa":
        carta.setDefensa(Posicion.HORIZONTAL)
        if isinstance(carta,CartaMonstruo):
          if None in self.__tablero.__cartasjugador[0]:
            indice= self.__tablero.__cartasjugador[0].index(None)
            self.__tablero.__cartasjugador[0][indice]= carta
          else:
            print("Espacio para carta tipo Monstruo lleno en el tablero")
        elif isinstance(carta,CartaMagica):
          if None in self.__tablero.__cartasjugador[1]:
            indice= self.__tablero.__cartasjugador[1].index(None)
            self.__tablero.__cartasjugador[1][indice]= carta
          else:
            print("Espacio para cartas tipo Magica lleno en el tablero")
        elif isinstance(carta,CartaTrampa):
          if None in self.__tablero.__cartasjugador[1]:
            indice= self.__tablero.__cartasjugador[1].index(None)
            self.__tablero.__cartasjugador[1][indice]= carta
          else:
            print("Espacio para cartas tipo Trampa lleno en el tablero")
    elif pos=="abajo":
      carta.setOrientacion(Orientacion.ABAJO)
      if None in self.__tablero.__cartasjugador[1]:
            indice= self.__tablero.__cartasjugador[1].index(None)
            self.__tablero.__cartasjugador[1][indice]= carta
    
      