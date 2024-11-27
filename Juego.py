from CartaMonstruo import *
from CartaMagica import *
from CartaTrampa import *
from Posicion import *
from Orientacion import *
from Jugador import *
from Maquina import *

#Clase Juego 
class Juego():
  def __init__(self, maquina, jugador): 
    self.__maquina = maquina
    self.__jugador = jugador
    self.__turnos = 1

  def declararBatalla(self,cartaOponente,cartaAtacante,oponente,atacante):
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
        elif (cartaAtacante.getAtaque() == cartaOponente.getAtaque()):
          oponente.getTablero().removerCarta(cartaOponente)
          atacante.getTablero().removerCarta(cartaAtacante)
    elif (cartaAtacante.eModoAtaque() and cartaOponente.eModoDefensa()):
        if (cartaAtacante.getAtaque > cartaOponente.getDefensa()):
            oponente.getTablero().removerCarta(cartaOponente)
        elif  (cartaAtacante.getAtaque < cartaOponente.getDefensa()):
            diferencia = cartaAtacante.getAtaque() - cartaOponente.getDefensa()
            puntos = atacante.getPuntos() - abs (diferencia)
            atacante.setPuntos(puntos) 
            cartaOponente.modoAtaque().setPosicion(Posicion.HORIZONTAL)
    print(f"Tablero de {atacante.getNombre()}: {atacante.getTablero()}")
    print(f"Tablero de {oponente.getNombre()}: {oponente.getTablero()}")

  def batallaDirecta(cartaAtacante,oponente):
    puntos = cartaAtacante.getAtaque() - oponente.getPuntos
    oponente.setPuntos(abs(puntos))

  #FASE BATALLA DE LA MAQUINA
  def mBatalla(self):
    monstruosJugador = self.__jugador.getTablero().getMonstruos()
    monstruosMaquina = self.__maquina.getTablero().getMonstruos()
    monstruosAtaqueJ = []
    for monstruo in monstruosJugador:
      if monstruo.getOrientacion() == Orientacion.ARRIBA:
        monstruosAtaqueJ.append(monstruo)
    usadas = []
    for cartaM in monstruosMaquina:
        if cartaM not in usadas:
          if cartaM.emodoAtaque():
            if monstruosJugador == []:
              self.batallaDirecta(cartaM,self.__jugador)
              usadas.append(cartaM)   
            for cartaJ in monstruosAtaqueJ:
              if cartaM.getAtaque() > cartaJ.getAtaque():
                self.declararBatalla(cartaJ,cartaM,self.__jugador,self.__maquina)
                usadas.append(cartaM)  
              elif cartaM.getAtaque() > cartaJ.getDefensa():
                self.declararBatalla(cartaJ,cartaM,self.__jugador,self.__maquina)
                usadas.append(cartaM)  
              elif cartaM.getDefensa() < cartaJ.getAtaque():
                self.declararBatalla(cartaJ,cartaM,self.__jugador,self.__maquina)
                usadas.append(cartaM)  
              elif cartaM.getAtaque() == cartaJ.getAtaque():
                self.declararBatalla(cartaJ,cartaM,self.__jugador,self.__maquina)
                usadas.append(cartaM)  


#OPCIONES DEL JUGADOR
  def opcion1 (self,jugador): #Carta es la que se quiere agregar al tablero
    print(jugador.getTablero()._str_())
    print(jugador.manoImprimir())
    indice = input("Ingrese el indice de la carta: ")
    if indice-1 <= len(jugador.getTablero):
      jugador.agregarCartaTablero(int(indice))
  def opcion2 (self,jugador): #carta es la carta magica o trampa, carta monstruo la que se quiere mejorar
    print(jugador.getTablero()._str_())
    indiceMa = input("Ingrese el indice de la carta Mágica o Trampa a usar: ")
    cartaMa = jugador.getTablero().getEspeciales()[(int(indiceMa)-1)]
    indiceMo = input("Ingrese el indice de la carta Monstruo a mejorar")
    cartaMo = jugador.getTablero().getMonstruos()[(int(indiceMo)-1)]
    if (isinstance(cartaMa, CartaMagica)):
      if (isinstance(cartaMo, CartaMonstruo)):
        cartaMa.usar(cartaMo)
      else:
        print("No hay carta monstruo en ese indice")
    if (isinstance(cartaMa, CartaTrampa)):
      if (isinstance(cartaMo, CartaMonstruo)):
        cartaMa.usar(cartaMo)
      else:
        print("No hay carta monstruo en ese indice")
    else:
      print("No hay carta especial en ese indice")
  def opcion3 (self,jugador,oponente,cartasUsadas):
    print(jugador)
    print(oponente)
    indiceJugador = input("Ingrese indice de su carta montruo que declara batalla: ")
    cartaJugador = jugador.getTablero().getMonstruos()[int(indiceJugador)-1]
    if cartaJugador not in cartasUsadas:
      if(oponente.getTablero().getMonstruos() == []):
        self.batallaDirecta(cartaJugador,self.__maquina)
        print(f"{cartaJugador} tuvo una batalla directa contra {self.__maquina}")
      else:
        indiceOponente = input("Ingrese indice de la carta monstruo a atacar: ")
        cartaOponente = oponente.getTablero().getMonstruos()[int(indiceOponente)-1]
        self.declararBatalla(cartaOponente,cartaJugador,oponente,jugador)
      return cartaJugador
    else:
      print("Esta carta ya tuvo su batalla")


  def jugar(self):
    while (self.__jugador.getPuntos() > 0 and self.__maquina.getPuntos() > 0):
      print (f"Turno {self.__turnos}")

      print("Fase tomar carta")
      self.__jugador.tomarCarta()
      self.__maquina.tomarCarta()

      print("Fase principal")
      #JUGADOR
      if self.__turnos == 1:
        print(f"Mano del jugador: {self.__jugador.manoImprimir()}")
        print("Crea tu tablero")
      pregunta = ""
      while pregunta != "2" :
        pregunta = input("Ingrese el número de tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION 2.- CONTINUAR A LA SIGUIENTE FASE \n:")
        if pregunta == "1":
          self.opcion1(self.__jugador)
        else:
          print("Ingrese una opción válida")

      #MAQUINA
      self.__maquina.mFasePrincipal()

      print("Fase Batalla")
      #Jugador
      print(self.__maquina)
      print(self.__jugador)
      if self.__turnos == 1:
        #JUGADOR
        pregunta = " "
        while pregunta != "":
          pregunta = input("Ingresa el número de tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION 2.- ACTIVAR CARTA MAGICA O TRAMPA \nEnter para seguir")
          pregunta = pregunta.lower()
          if pregunta == "1":
            self.opcion1(self.__jugador)
          elif pregunta == "2":
            self.opcion2(self.__jugador)
          else: 
            print("Ingrese opción válida")
        #MAQUINA
        self.__maquina.usarEspeciales()
        self.mBatalla()
      else:
        #JUGADOR
        cartasUsadas = []
        pregunta = " "
        while pregunta != "":
          pregunta = input("Ingresa el número de tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION 2.- ACTIVAR CARTA MAGICA O TRAMPA \nOPCION 3.- DECLARAR BATALLA \nEnter para seguir")
          pregunta = pregunta.lower()
          if pregunta == "1":
            self.opcion1(self.__jugador)
          elif pregunta == "2":
            self.opcion2(self.__jugador)
          elif pregunta == "3":
            cartaUsada = self.opcion3(self.__jugador,self.__maquina,cartasUsadas)
            cartasUsadas.append(cartaUsada)
          else: 
            print("Ingrese opción válida")
        #MAQUINA
        self.__maquina.usarEspeciales()
        self.mBatalla()
        cartasUsadas = [] 
        self.__turnos +=1
