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

  def seleccionarCartaTablero(self,indice):
    return self.__tablero[indice]
  def seleccionarCartaMano(self,indice):
    return self.__mano[indice]
  
  def agregarCartaTablero(self,indice):
    print (indice)
    if indice <= len(self.getMano() and indice>0):
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
          print(f"Se ha agregado la carta monstruo {carta} al tablero")
        else:
          print("Espacio para carta tipo Monstruo lleno en el tablero")
      else:
        if len(self.__tablero.getEspeciales()) < 3:
          self.__tablero.getEspeciales().append(carta)
          self.__mano.remove(carta)
          print(f"Se ha agregado la carta especial {carta} al tablero")
        else:
          print("Espacio para cartas tipo Magica o Trampa lleno en el tablero")
    else:
      print("Esa carta no se encuentra en mano")

  def __str__ (self):
    print (f"{self.__nombre}: {self.__puntos} Lp\n{self.__tablero._str_()}")
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
    if self.__nombre=="Maquina":
      return(f"{self.__nombre} - Lp:{self.__puntos}\nEspeciales: [{especiales[0]}] [{especiales[1]}] [{especiales[2]}]\nMonstruo: [{monstruos[0]}] [{monstruos[1]}] [{monstruos[2]}]")  
    else:
      return(f"Monstruo: [{monstruos[0]}] [{monstruos[1]}] [{monstruos[2]}]\nEspeciales: [{especiales[0]}] [{especiales[1]}] [{especiales[2]}]")

