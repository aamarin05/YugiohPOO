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

  def declararBatalla(self,cartaOponente,cartaAtacante,oponente,atacante):
    if isinstance(cartaAtacante,CartaMonstruo) and isinstance(cartaOponente,CartaMonstruo):
      cartasTrampa=[]
      for c in oponente.getMagicaTrampa():
        if isinstance(c,CartaTrampa):
          cartasTrampa.append(c)
      if len(cartasTrampa)>0:
        atributos= []
        for ct in cartasTrampa:
          atributos.append(ct.getAtributo())
        cartasTrampa[atributos.index(cartaOponente.getAtributo())].activar(cartaAtacante)  
      if (cartaOponente.eModoAtaque() and cartaAtacante.eModoAtaque()):
          if (cartaOponente.getAtaque() < cartaAtacante.getAtaque()):
              diferencia = cartaOponente.getAtaque() - cartaAtacante.getAtaque()
              puntos = oponente.getPuntos() - abs (diferencia)
              oponente.setPuntos(puntos)
          if (cartaAtacante.getAtaque() == cartaOponente.getAtaque()):
            oponente.getTablero().removerCarta(cartaOponente)
            atacante.getTablero().removerCarta(cartaAtacante)
      if (cartaAtacante.eModoAtaque() and cartaOponente.eModoDefensa()):
          if (cartaAtacante.getAtaque > cartaOponente.getDefensa()):
              oponente.getTablero().removerCarta(cartaOponente)
          if  (cartaAtacante.getAtaque < cartaOponente.getDefensa()):
              diferencia = cartaAtacante.getAtaque() - cartaOponente.getDefensa()
              puntos = atacante.getPuntos() - abs (diferencia)
              atacante.setPuntos(puntos) 
              cartaOponente.modoAtaque().setPosicion(Posicion.HORIZONTAL)
    print(f"Tablero de {atacante.getNombre()}: {atacante.getTablero()}")
    print(f"Tablero de {oponente.getNombre()}: {oponente.getTablero()}")

  def batallaDirecta(cartaAtacante,oponente):
    puntos = cartaAtacante.getAtaque() - oponente.getPuntos
    oponente.setPuntos(abs(puntos))

#OPCIONES DEL JUGADOR
  def opcion1 (self,jugador): #Carta es la que se quiere agregar al tablero
    print(jugador.getTablero())#print(jugador.manoImprimir())
    indice = input("Ingrese el indice de la carta: ")
    jugador.agregarCartaTablero(int(indice)+1)
    contarmagicas= 0
    for c in jugador.getTablero().getMagicaTrampa():
      if isinstance(c,CartaMagica):
        contarmagicas+=1
    print(f"¡Tienes {contarmagicas} cartas magicas que puedes usar!")
            
  def opcion2 (self,jugador): #carta es la carta magica o trampa, carta monstruo la que se quiere mejorar
    print(jugador.getTablero())
    indiceMa = input("Ingrese el indice de la carta Mágica a usar: ")
    cartaMa = jugador.getTablero().seleccionarCarta(int(indiceMa)+1)
    indiceMo = input("Ingrese el indice de la carta Monstruo a mejorar")
    cartaMo = jugador.getTablero().seleccionarCarta(int(indiceMo)+1)
    if (isinstance(cartaMa, CartaMagica)):
      cartaMa.usar(cartaMo)
    if (isinstance(cartaMa, CartaTrampa)):
      cartaMa.usar(cartaMo)
  def opcion3 (self,jugador,oponente,cartasUsadas):
    print(jugador)
    print(oponente)
    indiceJugador = input("Ingrese indice de su carta montruo que declara batalla: ")
    cartaJugador = jugador.getTablero().getMonstruos()[int(indiceJugador)+1]
    if cartaJugador not in cartasUsadas:
      if oponente.getTablero().getMonstruos() == []:
        self.batallaDirecta(cartaJugador,self.__maquina)
        print(f"{cartaJugador} tuvo una batalla directa contra {self.__maquina}")
      else:
        indiceOponente = input("Ingrese indice de la carta monstruo a atacar: ")
        cartaOponente = oponente.getTablero().getMonstruos()[int(indiceOponente)+1]
        self.declararBatalla(cartaOponente,cartaJugador,oponente,jugador)
      return cartaJugador
    else:
      print("Esta carta ya tuvo su batalla")


  def Jugar(self):
    while (self.__jugador.getPuntos() > 0 and self.__maquina.getPuntos() > 0):
      print (f"Turno {self.__turnos}")

      print("Fase tomar carta")
      self.__jugador.tomarCarta()
      self.__maquina.tomarCarta()

      print("Fase principal")
      #JUGADOR
      if self.__turnos == 1:
        print(f"Mano del jugador: {self.__jugador.getMano()}")
        print("Crea tu tablero")
      while True:
        pregunta = input("Ingrese el número de tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION 2.- CONTINUAR A LA SIGUIENTE FASE")
        if pregunta == "1":
          print(f"Mano del jugador: {self.__jugador.getMano()}")
          indice = input("Escriba el número de la carta de su mano para agregarla al tablero: ")
          self.__jugador.agregarCartaTablero(int(indice)+1)
        elif pregunta == "2":
          break
        else:
          print("Ingrese una opción válida")
      #MAQUINA
      self.__maquina.fasePrincipal()

      print("Fase Batalla")
      #Jugador
      print(self.__jugador)
      print(self.__maquina)
      if self.__turnos == 1:
        while True:
          pregunta = input("Ingresa el número de tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION 2.- ACTIVAR CARTA MAGICA O TRAMPA \nEnter para seguir")
          pregunta = pregunta.lower()
          if pregunta == "1":
            self.opcion1(self.__jugador)
          elif pregunta == "2":
            self.opcion2(self.__jugador)
          elif pregunta == "":
            self.__maquina.faseBatalla()
            break
          else: 
            print("Ingrese opción válida")
      else:
        cartasUsadas = []
        while True:
          pregunta = input("Ingresa el número de tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION 2.- ACTIVAR CARTA MAGICA O TRAMPA \nOPCION 3.- DECLARAR BATALLA \nEnter para seguir")
          pregunta = pregunta.lower()
          if pregunta == "1":
            self.opcion1(self.__jugador)
          elif pregunta == "2":
            self.opcion2(self.__jugador)
          elif pregunta == "3":
            cartaUsada = self.opcion3(self.__jugador,self.__maquina,cartasUsadas)
            cartasUsadas.append(cartaUsada)
          elif pregunta == "":
            self.__maquina.faseBatalla()
            cartasUsadas = []
          else: 
            print("Ingrese opción válida")
      
      self.__turnos +=1