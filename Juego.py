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

#FUNCIONES DE BATALLA
  def declararBatalla(self,cartaOponente,cartaAtacante,oponente,atacante): #BATALLA GENERAL
    if (cartaOponente.eModoAtaque() and cartaAtacante.eModoAtaque()): #AMBAS CARTAS EN MODO ATAQUE
        if (cartaOponente.getAtaque() < cartaAtacante.getAtaque()):
            diferencia = cartaOponente.getAtaque() - cartaAtacante.getAtaque()
            puntos = oponente.getPuntos() - abs (diferencia)
            oponente.setPuntos(puntos)
        elif (cartaAtacante.getAtaque() == cartaOponente.getAtaque()): #ATAQUE IGUAL
          oponente.getTablero().removerCarta(cartaOponente)
          atacante.getTablero().removerCarta(cartaAtacante)
        else:
          print(f"\nCarta {cartaAtacante} no pudo atacar {cartaOponente}")
    elif (cartaAtacante.eModoAtaque() and cartaOponente.eModoDefensa()): #AMBAS CARTAS MODOS DISTINTOS
        if (cartaAtacante.getAtaque > cartaOponente.getDefensa()):
            oponente.getTablero().removerCarta(cartaOponente)
        elif  (cartaAtacante.getAtaque < cartaOponente.getDefensa()):
            diferencia = cartaAtacante.getAtaque() - cartaOponente.getDefensa()
            puntos = atacante.getPuntos() - abs (diferencia)
            atacante.setPuntos(puntos) 
            cartaOponente.modoAtaque().setPosicion(Posicion.HORIZONTAL)
        else:
          print(f"\nCarta {cartaAtacante} no pudo atacar {cartaOponente}")
    print(f"\nTablero de {atacante.getNombre()}: {atacante.getTablero().__str__()}")
    print(f"\nTablero de {oponente.getNombre()}: {oponente.getTablero().__str__()}")

  def batallaDirecta(cartaAtacante,oponente):
    puntos = cartaAtacante.getAtaque() - oponente.getPuntos()
    oponente.setPuntos(abs(puntos))

#FASE BATALLA DE LA MAQUINA
  def mBatalla(self):
    monstruosJugador = self.__jugador.getTablero().getMonstruos()
    monstruosMaquina = self.__maquina.getTablero().getMonstruos()
    monstruosAtaqueJ = []
    for monstruo in monstruosJugador: #REVISA LA LISTA DEL JUGADOR
      if monstruo.getOrientacion() == Orientacion.ARRIBA:
        monstruosAtaqueJ.append(monstruo) #REGISTRA LAS CARTAS QUE EL JUGADOR TIENE EN ATAQUE
    usadas = []
    for cartaM in monstruosMaquina: #VA A ITERAR LAS CARTAS MONSTRUO QUE TIENE LA MAQUINA
        if cartaM not in usadas: #SI NO SE HA USADO LA CARTA MONSTRUO
          if cartaM.eModoAtaque(): #SI ESA CARTA ESTÁ EN MODO ATAQUE LA VA A USAR
            if monstruosJugador == []:
              Juego.batallaDirecta(cartaM,self.__jugador)
              usadas.append(cartaM)   #SI SE DECLARO LA BATALLA DIRECTA SE GUARDA EN USADAS
            else:
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
    print(jugador.getTablero().__str__())
    print(jugador.manoImprimir())
    indice = input("Ingrese el indice de la carta: ")
    if (indice.isdigit()) and (int(indice) <= len(jugador.getMano())) and (int(indice)>0): #Ejecuta si hay carta en el tablero
      indice = int(indice)-1
      jugador.agregarCartaTablero(indice)
    else:
      print("En ese lugar no hay esa carta")
  def opcion2 (self,jugador): #carta es la carta magica o trampa, carta monstruo la que se quiere mejorar
    print(jugador.getTablero().__str__())

    indiceMa = input("Ingrese el indice de la carta Mágica o Trampa a usar: ")
    if (not indiceMa.isdigit()) or int(indiceMa) > len(jugador.getTablero().getEspeciales()) or int(indiceMa)<=0:
      print("No hay carta especial en ese indice")
    else:
      indiceMa = int(indiceMa)-1
      indiceMo = input("Ingrese el indice de la carta Monstruo a mejorar: ")
      if (not indiceMo.isdigit() )  or int(indiceMo) > len(jugador.getTablero().getMonstruos()) or int(indiceMo)<=0:
        print("No hay carta monstruo en ese indice")
      else:
        indiceMo = int(indiceMo)-1
      cartaMa = jugador.getTablero().getEspeciales()[indiceMa]
      cartaMo = jugador.getTablero().getMonstruos()[indiceMo]
      if (isinstance(cartaMa, CartaMagica)):
          cartaMa.usar(cartaMo)
          self.__jugador.getTablero().removerCarta(cartaMa)
      if (isinstance(cartaMa, CartaTrampa)):
          cartaMa.usar(cartaMo)
          self.__jugador.getTablero().removerCarta(cartaMo)
  def opcion3 (self,jugador,oponente,cartasUsadas):
    print(jugador)
    print(oponente)
    indiceJugador = input("Ingrese indice de su carta montruo que declara batalla: ")
    if (not indiceJugador.isdigit()) or int(indiceJugador) > len(jugador.getTablero().getMonstruos()) or int(indiceJugador)<=0:
      print("En ese lugar no hay carta")
    else:
      indiceJugador = int(indiceJugador)-1
      cartaJugador = jugador.getTablero().getMonstruos()[indiceJugador]
      if cartaJugador not in cartasUsadas:
        for cartaEspecial in self.__maquina.getTablero().getEspeciales():
          if isinstance(cartaEspecial,CartaTrampa):
            usada = cartaEspecial.usar(cartaJugador)
        if not usada:
          if(oponente.getTablero().getMonstruos() == []):
            self.batallaDirecta(cartaJugador,self.__maquina)
            print(f"{cartaJugador} tuvo una batalla directa contra {self.__maquina}")
          else:
            indiceOponente = input("Ingrese indice de la carta monstruo a atacar: ")
            if int(indiceOponente) > len(oponente.getTablero().getMonstruos()) or indiceOponente<=0:
              print("En ese lugar no hay carta")
            else:
              indiceOponente = int(indiceOponente)-1
              cartaOponente = oponente.getTablero().getMonstruos()[indiceOponente]
              self.declararBatalla(cartaOponente,cartaJugador,oponente,jugador)
              return cartaJugador
      else:
        print("Esta carta ya tuvo su batalla")


  def jugar(self):
    print(f"\n Empieza {self.__jugador.getNombre()}")
    while (self.__jugador.getPuntos() > 0 and self.__maquina.getPuntos() > 0):
      print (f"\nTurno {self.__turnos}")

      print("\nFASE TOMAR CARTA\n")
      self.__jugador.tomarCarta()
      self.__maquina.tomarCarta()

      print("\nFASE PRINCIPAL\n")
      #JUGADOR
      if self.__turnos == 1:
        print(f"{self.__jugador.manoImprimir()}")
        print("Crea tu tablero\n")
      pregunta = ""
      while pregunta != "2" :
        pregunta = input("Ingrese el número de tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION 2.- CONTINUAR A LA SIGUIENTE FASE \n: ")
        if pregunta == "1":
          self.opcion1(self.__jugador)
        else:
          print("Ingrese una opción válida")

      #MAQUINA
      self.__maquina.mFasePrincipal()

      print("FASE BATALLA\n")
      #Jugador
      print(self.__maquina)
      print(self.__jugador)
      if self.__turnos == 1:
        #JUGADOR
        pregunta = " "
        while pregunta != "":
          pregunta = input("\nIngresa el número de tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION 2.- ACTIVAR CARTA MAGICA O TRAMPA \nEnter.- para seguir: \n")
          pregunta = pregunta.lower()
          if pregunta == "1":
            self.opcion1(self.__jugador)
          elif pregunta == "2":
            self.opcion2(self.__jugador)
          else: 
            print("\nIngrese opción válida")
        #MAQUINA
        self.__maquina.usarEspeciales()
        self.mBatalla()
      else:
        #JUGADOR
        cartasUsadas = []
        pregunta = " "
        while pregunta != "":
          pregunta = input("\nIngresa el número de tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION 2.- ACTIVAR CARTA MAGICA O TRAMPA \nOPCION 3.- DECLARAR BATALLA \nEnter.- para seguir: \n")
          pregunta = pregunta.lower()
          if pregunta == "1":
            self.opcion1(self.__jugador)
          elif pregunta == "2":
            self.opcion2(self.__jugador)
          elif pregunta == "3":
            cartaUsada = self.opcion3(self.__jugador,self.__maquina,cartasUsadas)
            cartasUsadas.append(cartaUsada)
          else: 
            print("\nIngrese opción válida")
        #MAQUINA
        self.__maquina.usarEspeciales()
        self.mBatalla()
      cartasUsadas = [] 
      self.__turnos +=1
      print("\nRESULTADOS\n")
      print(self.__maquina)
      print(self.__jugador)
      if self.__jugador.getPuntos() <= 0:
        print("\nMAQUINA GANA!!")
      if self.__maquina.getPuntos() <= 0:
        print(f"\n{self.__jugador.getNombre()} GANA!!")

