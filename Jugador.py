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
  def getTablero(self):
    return  self.__tablero  

  def tomarCarta(self):
    carta=self.__deck.pop()
    self.__mano.append(carta)
    print(f"Tomaste la carta {carta.getNombre()}")
  
  def manoImprimir(self):
    mostrar= ""
    for i in range(len(self.__mano)):  
        carta = self.__mano[i]         
        mostrar += f"{i + 1}. {carta}\n"
    return f"Usted tiene en su mano:\n{mostrar}"

  def seleccionarCartaMano(self,indice):
    return self.__mano[indice]
  
  def agregarCartaTablero(self,indice):
      carta = self.getMano()[indice-1]
      if isinstance(carta,CartaMonstruo):
        if len(self.__tablero.getMonstruos()) < 3:
          pos = input("1.Modo Ataque, 2. Modo Defensa:")
          while (pos != "1") and (pos !="2"):
            print("Ingrese (1 o 2)")
            pos = input("1.Modo Ataque, 2. Modo Defensa:")
          if pos == "1":
            carta.modoAtaque()
            self.__tablero.getMonstruos().append(carta)
          elif pos == "2":
            carta.modoDefensa()
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
  def __str__ (self):
    print (f"{self.__nombre}: {self.__puntos} Lp\n{self.__tablero._str_()}")
    if self.__nombre=="Maquina":
      return(f"{self.__nombre} - Lp:{self.__puntos}\nEspeciales: [{self.getTablero().getCartas()[1][0]}] [{self.getTablero().getCartas()[1][1]}] [{self.getTablero().getCartas()[1][2]}]\nMonstruo: [{self.getTablero().getCartas()[0][0]}] [{self.getTablero().getCartas()[0][1]}] [{self.getTablero().getCartas()[0][2]}]")  
    else:
      return(f"Monstruo: [{self.getTablero().getCartas()[0][0]}] [{self.getTablero().getCartas()[0][1]}] [{self.getTablero().getCartas()[0][2]}]\nEspeciales: [{self.getTablero().getCartas()[1][0]}] [{self.getTablero().getCartas()[1][1]}] [{self.getTablero().getCartas()[1][2]}]\n{self.__nombre} - Lp:{self.__puntos}")
