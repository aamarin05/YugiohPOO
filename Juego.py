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
  
  def faseDeclararBatalla(self):
    if (self.__jugadores[self.__turnoJugador] == "MAQUINA"):
      if self.__turnoJuego < 2: 
        print("No se puede declarar batalla en el primer turno")
      else:
        l_cartas_mostruo = []
        for carta in self.__tableros[self.__turnoJugador]:
          if isinstance(carta, CartaMonstruo):
            l_cartas_mostruo.append(carta)
        carta_atacante = rd.choice(l_cartas_mostruo)
        l_cartas_atacar = []
        for carta in self.__tableros[self.__turnoJugador-1]:
          if isinstance(carta, CartaMonstruo):
            l_cartas_atacar.append(carta)
        if (carta_atacante is not None and len(l_cartas_atacar) == 0):
          carta_atacada = rd.choice(l_cartas_atacar)
          if(carta_atacada.getPosicion() == Posicion.VERTICAL):
            diferencia_puntos = carta_atacada.atacarCarta()
            puntos_jugador = self.__jugadores[1].getAtaque() - diferencia_puntos
            self.__jugadores[1].set(puntos_jugador)
          
      self.__turnoJugador -= 1
    else: 
      if self.__turnoJuego < 2: 
        print("No se puede declarar batalla en el primer turno")
      else:
        carta_atacante = input("Ingrese el nombre de la carta a de su tablero: ")
        carta_atacada = input("Ingrese el nombre de la carta a la que atacar: ")
        carta_atacante = self.seleccionarCarta(carta_atacante)
        carta_atacada = self.seleccionarCarta(carta_atacada)
        if(carta_atacante is not None and carta_atacada is not None):
          if(carta_atacada.getPosicion() == Posicion.VERTICAL):
            diferencia_puntos = carta_atacada.atacarCarta()

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