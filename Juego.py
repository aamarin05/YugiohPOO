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
            cartaOponente.destruida()
            oponente.getTablero().removerCarta(cartaOponente)#le aniadi esta parte de remover la carta
        elif (cartaAtacante.getAtaque() == cartaOponente.getAtaque()): #ATAQUE IGUAL
          oponente.getTablero().removerCarta(cartaOponente)
          atacante.getTablero().removerCarta(cartaAtacante)
          cartaOponente.destruida()
          cartaAtacante.destruida()
          print("Sus cartas fueron iguales")
        else:
          print(f"\nCarta {cartaAtacante} no pudo atacar {cartaOponente}")
    elif (cartaAtacante.eModoAtaque() and cartaOponente.eModoDefensa()): #AMBAS CARTAS MODOS DISTINTOS
        if (cartaAtacante.getAtaque > cartaOponente.getDefensa()):
            oponente.getTablero().removerCarta(cartaOponente)
            cartaOponente.destruida()
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
      if monstruo.eModoAtaque():
        monstruosAtaqueJ.append(monstruo) #REGISTRA LAS CARTAS QUE EL JUGADOR TIENE EN ATAQUE
    usadas = []
    trampas = []
    for cartaM in monstruosMaquina: #VA A ITERAR LAS CARTAS MONSTRUO QUE TIENE LA MAQUINA
        if cartaM not in usadas: #SI NO SE HA USADO LA CARTA MONSTRUO
          if cartaM.eModoAtaque(): #SI ESA CARTA ESTÁ EN MODO ATAQUE LA VA A USAR
            for cartaEspecial in self.__jugador.getTablero().getEspeciales(): #VA A BUSCAR SI TIENE TRAMAPA
              if isinstance(cartaEspecial,CartaTrampa): #QUE TENGA CARTAS TRAMPA SI TIENE SE USA
                usada = cartaEspecial.usar(cartaM) #SE GUARDA LA VARIABLE
                if usada: #SI SE UO UNA TRAMPA
                  trampas.append(cartaEspecial) #SE GUARDA EN TRAMPAS
                  self.__jugador.getTablero().removerCarta(cartaEspecial)
            if trampas == []: #SI ESTA VACIA ES PORQUE NO SE USO TRAMPAS, ASÍ QUE SÍ VA A RECIBIR EL ATAQUE
              if monstruosJugador == []:
                Juego.batallaDirecta(cartaM,self.__jugador)
                usadas.append(cartaM)   #SI SE DECLARO LA BATALLA DIRECTA SE GUARDA EN USADAS Y SE PASA A LA SIGUIENTE CARTA
              else: #SI NO SE DECLARÓ BATALLA DIRECTA:
                for cartaJ in monstruosAtaqueJ: #POR CADA CARTA QUE EL JUGADOR TENGA EN MODO ATAQUE, LA CARTA MONSTRUO ACTUARÁ EN ORDEN
                  if cartaM.getAtaque() > cartaJ.getAtaque(): #1. SI SU ATAQUE ES MAYOR QUE EL DEL JUGADOR ATACARÁ
                    self.declararBatalla(cartaJ,cartaM,self.__jugador,self.__maquina)
                    usadas.append(cartaM)  
                  elif cartaM.getAtaque() > cartaJ.getDefensa(): #2. SI ATAQUE ES MAYOR A LA DEFENSA 
                    self.declararBatalla(cartaJ,cartaM,self.__jugador,self.__maquina)
                    usadas.append(cartaM)  
                  elif cartaM.getDefensa() < cartaJ.getAtaque():#3. SI SU DEFENSA ES MENOR QUE EL ATAQUE 
                    self.declararBatalla(cartaJ,cartaM,self.__jugador,self.__maquina)
                    usadas.append(cartaM)  
                  elif cartaM.getAtaque() == cartaJ.getAtaque(): #4. SI SUS ATAQUES SON IGUALSE
                    self.declararBatalla(cartaJ,cartaM,self.__jugador,self.__maquina)
                    usadas.append(cartaM)  


#OPCIONES DEL JUGADOR
  #COLOCAR CARTA EN EL TABLERO
  def opcion1 (self,jugador): #Carta es la que se quiere agregar al tablero
    print(jugador.getTablero().__str__()) #imprimer el tablero
    print(jugador.manoImprimir()) #imprime la mano
    indice = input("Ingrese el indice de la carta: ")
    if (indice.isdigit()) and (int(indice) <= len(jugador.getMano())) and (int(indice)>0): #Ejecuta si hay carta en el tablero
      indice = int(indice)-1
      jugador.agregarCartaTablero(indice)
      print(jugador.getTablero().__str__())

    else:
      print("En ese lugar no hay esa carta")

  #USAR CARTA ESPECIAL
  def opcion2 (self,jugador): #carta es la carta magica o trampa, carta monstruo la que se quiere mejorar
    print(jugador.getTablero().__str__())
    indiceMa = input("Ingrese el indice de la carta Mágica a usar: ")
    if (not indiceMa.isdigit()) or int(indiceMa) > len(jugador.getTablero().getEspeciales()) or int(indiceMa)<=0:
      print("No hay carta especial en ese indice")
    else: #INDICE CORRECTO
      indiceMa = int(indiceMa)-1
      indiceMo = input("Ingrese el indice de la carta Monstruo a mejorar: ")
      if (not indiceMo.isdigit() )  or int(indiceMo) > len(jugador.getTablero().getMonstruos()) or int(indiceMo)<=0:
        print("No hay carta monstruo en ese indice")
      else: #INDICE CORRECTO
        indiceMo = int(indiceMo)-1
        cartaMa = jugador.getTablero().getEspeciales()[indiceMa]
        cartaMo = jugador.getTablero().getMonstruos()[indiceMo]
        if (isinstance(cartaMa, CartaMagica)):
            cartaMa.usar(cartaMo)
            self.__jugador.getTablero().removerCarta(cartaMa)
        else:
          print("Esta carta no es mágica")

  #DECLARAR BATALLA
  def opcion3 (self,jugador,oponente,cartasUsadas):
    print(jugador)
    print("___________________________________________________________________________________________________________________")
    print(oponente)
    indiceJugador = input("Ingrese indice de su carta montruo que declara batalla: ") #INDICE DE LA CARTA DEL JUGADOR
    if (not indiceJugador.isdigit()) or int(indiceJugador) > len(jugador.getTablero().getMonstruos()) or int(indiceJugador)<=0:
      print("En ese lugar no hay carta")
    else:
      indiceJugador = int(indiceJugador)-1
      cartaJugador = jugador.getTablero().getMonstruos()[indiceJugador] #CARTA DEL JUGADOR
      trampas = []
      if cartaJugador not in cartasUsadas: #SI ESA CARTA NO SE HA USADO
        for cartaEspecial in oponente.getTablero().getEspeciales(): #SE BUSCA EN LAS ESPECIALES DE LA MAQUINA
          if isinstance(cartaEspecial,CartaTrampa): #QUE TENGA CARTAS TRAMPA SI TIENE SE USA
            usada = cartaEspecial.usar(cartaJugador) #SE GUARDA LA VARIABLE
            if usada: #SI SE UO UNA TRAMPA
              trampas.append(cartaEspecial) #SE GUARDA EN TRAMPAS
              oponente.getTablero().removerCarta(cartaEspecial)
        if trampas == []: #SI ESTA VACIA ES PORQUE NO SE USO TRAMPAS, ASÍ QUE SÍ VA A RECIBIR EL ATAQUE
          if(oponente.getTablero().getMonstruos() == []):
            self.batallaDirecta(cartaJugador,oponente)
            print(f"{cartaJugador} tuvo una batalla directa contra {oponente}")
          else:
            indiceOponente = input("Ingrese indice de la carta monstruo a atacar: ")
            if ((not indiceOponente.isdigit()) or int(indiceOponente) > len(oponente.getTablero().getMonstruos()) or int(indiceOponente)<=0):
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
        print(f"{self.__jugador.manoImprimir()}\n")
        print("Crea tu tablero\n")
      pregunta = "  "
      while pregunta != "" :
        pregunta = input("Ingrese el número de tú acción \nOOCIÓN 1.- COLOCAR CARTA EN TABLERO \nOPCION Enter.- CONTINUAR A LA SIGUIENTE FASE \n ")
        if pregunta == "1":
          self.opcion1(self.__jugador)
        else:
          print("\nIngrese una opción válida\n")

      #MAQUINA
      self.__maquina.mFasePrincipal()

      print("\nFASE BATALLA\n")
      #Jugador
      print(self.__maquina.__str__())
      print("___________________________________________________________________________________________________________________")
      print(self.__jugador.__str__())
      if self.__turnos == 1:
        #JUGADOR
        pregunta = "  "
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
      print(self.__maquina.__str__())
      print(self.__jugador.__str__())
      if self.__jugador.getPuntos() <= 0:
        print("\nMAQUINA GANA!!")
      if self.__maquina.getPuntos() <= 0:
        print(f"\n{self.__jugador.getNombre()} GANA!!")

