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
    self.__turnos = 1
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

  def opcion1 (jugador): #Carta es la que se quiere agregar al tablero
    indice = input("Ingrese el indice de la carta: ")
    jugador.agregarCartaTablero(int(indice)+1)
  def opcion2 (jugador): #carta es la carta magica o trampa, carta monstruo la que se quiere mejorar
    indiceMa = input("Ingrese el indice de la carta Mágica a usar: ")
    cartaMa = jugador.getTablero().seleccionarCarta(int(indiceMa)+1)
    indiceMo = input("Ingrese el indice de la carta Monstruo a mejorar")
    cartaMo = jugador.getTablero().seleccionarCarta(int(indiceMo)+1)
    if (isinstance(cartaMa, CartaMagica)):
      cartaMa.usar(cartaMo)
    if (isinstance(cartaMa, CartaTrampa)):
      cartaMa.usar(cartaMo) #CAMBIAR LA FUNCIÓN
  def opcion3 (jugador,oponente):
    print(jugador)
    print(oponente)
    indiceJugador = input("Ingrese indice de su carta montruo que declara batalla: ")
    indiceOponente = input("Ingrese indice de la carta monstruo a atacar: ")
    jugador.getTablero[int(indiceJugador)+1].declararBatalla(oponente.getTablero[int(indiceOponente)+1])


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


    while (self.__jugador.getPuntos() > 0 and self.__maquina.getPuntos() > 0):
      print (f"Turno {turnos}")
      carta = self.__jugador.tomarCarta()
      print(carta)
      if turnos == 1:
        pregunta = input("Elige tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION 2.- ACTIVAR CARTA MAGICA O TRAMPA")
        pregunta = pregunta.lower()
        if pregunta == "1":
          self.opcion1(self.__jugador)
        elif pregunta == "2":
          self.opcion2(self.__jugador)
        elif pregunta == "":
          carta = self.__maquina.robar_carta()
          self.__maquina.agregarCartaTablero(carta) #CAMBIAR LA FUNCION DE MAQUINA
        else: 
          print("Ingrese una opción 1,2 o enter para seguir")

      pregunta = input("Elige tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION 2.- ACTIVAR CARTA MAGICA O TRAMPA \nOPCION 3.- DECLARAR BATALLA")
      pregunta = pregunta.lower()
      if pregunta == "1":
        self.opcion1(self.__jugador)
      elif pregunta == "2":
        self.opcion2(self.__jugador)
      elif pregunta == "3":
        self.opcion3(self.__jugador,self.__maquina)
      elif pregunta == "":
        carta = self.__maquina.robar_carta()
        self.__maquina.agregarCartaTablero(carta) #CAMBIAR LA FUNCION DE MAQUINA
      else: 
        print("Ingrese una opción 1,2,3 o enter para el siguiente turno")
    
#AGREGAR LOS PRINTS DE LO QUE ACABA DE PASAR
      carta = self.__maquina.robar_carta()
      self.__maquina.agregarCartaTablero(carta)
      self.__maquina.getTablero[0].declararBatalla(self.__maquina.getTablero[0])
      turnos +=1