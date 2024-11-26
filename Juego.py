from CartaMonstruo import *
from CartaMagica import *
from CartaTrampa import *
from Posicion import *
from Jugador import *
from Maquina import *

#Clase Juego 
class Juego():
  def __init__(self, maquina, jugador): 
    self.__maquina = maquina
    self.__jugador = jugador
  def declararBatalla(self,cartaMonstruo,oponente,atacante):
    if (self.eModoAtaque() and cartaMonstruo.eModoAtaque()):
        if (self.getAtaque() > cartaMonstruo.getAtaque()):
            diferencia = self.getAtaque() - cartaMonstruo.getAtaque()
            puntos = oponente.getPuntos() - abs (diferencia)
            oponente.setPuntos(puntos)
        if (self.getAtaque() == cartaMonstruo.getAtaque()):
          oponente.getTablero().removerCarta(cartaMonstruo)
          atacante.getTablero().removerCarta(self)
    if (self.eModoDefensa() and cartaMonstruo.eModoDefensa()):
        if (self.getAtaque > cartaMonstruo.getDefensa()):
            oponente.getTablero().removerCarta(cartaMonstruo)
        if  (self.getAtaque < cartaMonstruo.getDefensa()):
            diferencia = self.getAtaque() - cartaMonstruo.getDefensa()
            puntos = atacante.getPuntos() - abs (diferencia)
            atacante.setPuntos(puntos) 
            cartaMonstruo.modoAtaque().setPosicion(Posicion.HORIZONTAL)



  def Jugar(self):
    print("Fase principal")
    print(f"Mano del jugador: {self.__jugador.getMano()}")
    print("Crea tu tablero")
    while (self.__jugador.getMano()>0):
      carta = input("Escriba el numero de la carta para agregarla al tablero: ")
      modoCarta = input("1.Modo ataque, 2. Modo defensa. (1 o 2)")
      if modoCarta == "1":
        self.__jugador.getMano()[int(carta)].modoAtaque()
      if modoCarta == "2":
        self.__jugador.getMano()[int(carta)].modoDefensa()
      self.__jugador.agregarCarta(carta)

    for carta in self.__maquina.getMano():
      self.__maquina.tablero.agregarCarta(carta)
      
      """
      pregunta = input("Elige tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION 2.- ACTIVAR CARTA MAGICA O TRAMPA \nOPCION 3.- DECLARAR BATALLA")

      def opcion1 ():
        self.agregarCartaTablero(carta)
      """
    turnos = 1
    pregunta
    while (self.__jugador.getPuntos() > 0 and self.__maquina.getPuntos() > 0):
      if turnos == 1:
        print ("Turno 1") 
        carta = self.__jugador.tomarCarta()
        print(carta)
        pregunta = input("Quieres colocar la carta en tablero (si/no)?")
        if pregunta.lower() == "si":
          self.__jugador.agregarCartaTablero(carta)
        pregunta = ("¿Quieres activar una carta mágica o trampa? (si/no)")
        if pregunta.lower == "si":
          print(self.__jugador.getTablero())
          indice = input("Ingresa el indice de la carta: ")
          carta = self.__jugador.seleccionarCarta(int(indice+1))
          indice = input("Ingrese el indice de la carta monstruo a mejorar: ")
          if (isinstance(carta, CartaMagica)):
            carta.usar()
        carta = self.__maquina.robar_carta()
        self.__maquina.agregarCartaTablero(carta)
      print (f"Turno {turnos}")
      carta = self.__jugador.tomarCarta()
      print(carta)
      pregunta = input("Quieres colocar la carta en tablero?")
      if pregunta.lower() == "si":
        self.__jugador.agregarCartaTablero(carta)
      pregunta = input("¿Quieres activar una carta mágica o trampa?")
      if pregunta.lower == "si":
        print(self.__jugador.tablero)
        indice = input("Ingresa el indice de la carta: ")
        carta = self.__jugador.seleccionarCarta(int(indice+1))
        indice = input("Ingrese el indice de la carta monstruo a mejorar: ")
        if (isinstance(carta, CartaMagica)):
          carta.usar()
      pregunta = input("¿Quieres declarar batalla ?")
      if pregunta.lower() == "si":
        print(self.__jugador.getTablero())
        indiceJugador = input("Ingrese indice de su carta montruo: ")
        print(self.__maquina.getTablero())
        indiceOponente = input("Ingrese indice de la carta monstruo a atacar: ")
        self.__jugador.getTablero[int(indice+1)].declararBatalla(self.__maquina.getTablero[int(indice+1)])
      carta = self.__maquina.robar_carta()
      self.__maquina.agregarCartaTablero(carta)
      self.__maquina.getTablero[0].declararBatalla(self.__maquina.getTablero[0])
      turnos +=1