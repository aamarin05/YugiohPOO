from Deck import *
from Tablero import *

class Jugador:
  def __init__(self,nombre):
    self.__nombre = nombre
    self.__deck = Deck.crearDeck()
    self.__puntos = 4000
    self.__tablero = Tablero()
    self.__mano= [self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop()]

#GETTERS Y SETTER
  def getNombre(self):
    return self.__nombre
  def getPuntos (self):
    return self.__puntos
  def setPuntos (self, puntos):
    self.__puntos = puntos
  def getMano (self):
    return self.__mano 
  def getTablero(self):
    return  self.__tablero  
  def getDeck(self):
    return self.__deck

#FUNCIONES JUGABLES DE TODOS LOS JUGADORES
  def tomarCarta(self):
    carta=self.__deck.pop()
    self.__mano.append(carta)
    print(f"Jugador la carta {carta.getNombre()}")
  
  def manoImprimir(self):
    mostrar= ""
    for i in range(len(self.__mano)):  
        carta = self.__mano[i]         
        mostrar += f"{i + 1}. {carta}\n"
    return f"Usted tiene en su mano:\n{mostrar}"

  def seleccionarCartaTablero(self,indice):
    return self.__tablero[indice]
  def seleccionarCartaMano(self,indice):
    return self.__mano[indice]
  
  def agregarCartaTablero(self,indice): 
    carta = self.getMano()[indice]
    if isinstance(carta,CartaMonstruo):
      if len(self.__tablero.getMonstruos()) < 3:
        pos = input("1.Modo Ataque, 2. Modo Defensa:")
        while (pos != "1") and (pos !="2"):
          print("Ingrese (1 o 2)")
          pos = input("1.Modo Ataque, 2. Modo Defensa:")
        if pos == "1":
          carta.modoAtaque()
          self.__tablero.getMonstruos().append(carta)
          self.__mano.remove(carta)
        elif pos == "2":
          carta.modoDefensa()
          self.__tablero.getMonstruos().append(carta)
          self.__mano.remove(carta)
        print(f"Se ha agregado la carta monstruo al tablero \n{carta}")
      else:
        print("Espacio para carta tipo Monstruo lleno en el tablero")
    else:
      if len(self.__tablero.getEspeciales()) < 3:
        self.__tablero.getEspeciales().append(carta)
        self.__mano.remove(carta)
        print(f"Se ha agregado la carta especial al tablero \n{carta}")
      else:
        print("Espacio para cartas tipo Magica o Trampa lleno en el tablero")

#TOSTRING
  def __str__ (self):
    monstruos = []
    especiales = []

    for i in range(3):
        if i < len(self.__tablero.getMonstruos()):
            monstruos.append(str(self.__tablero.getMonstruos()[i]))
        else:
            monstruos.append("No hay cartas")

    for i in range(3):
        if i < len(self.__tablero.getEspeciales()):
            especiales.append(str(self.__tablero.getEspeciales()[i]))
        else:
            especiales.append("No hay cartas")
    return(f"Monstruo: [{monstruos[0]}] [{monstruos[1]}] [{monstruos[2]}]\nEspeciales: [{especiales[0]}] [{especiales[1]}] [{especiales[2]}] \n{self.__nombre} - Lp:{self.__puntos}")

