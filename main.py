from enum import (Enum)
from cartasCreadas import cartas
import random as rd

class TipoAtributo (Enum):
  OSCURIDAD = 1
  LUZ = 2
  TIERRA = 3
  AGUA = 4
  FUEGO = 5
  VIENTO = 6

class TipoMonstruo (Enum):
  L = 1 #Lanazador de Conjuros
  D = 2 #Dragon
  Z = 3 #Zombi
  G = 4 #Guerrero
  B = 5 #Bestia
  O = 6 #Demonio

class Orientacion (Enum):
  ARRIBA = 1
  ABAJO = 2

class Posicion (Enum):
  VERTICAL = 1
  HORIZONTAL = 2

class Carta:
  def __init__(self, nombre, descripcion, posicion,orientacion): #Constructor
    self.__nombre = nombre #__ es para acceso privado
    self.__descripcion = descripcion
    self.__posicion = posicion
    self.__orientacion = orientacion

  #getters y setters
  def getNombre (self):
    return self.__nombre
  def setNombre (self, nombre):
    self.__nombre = nombre
  def getDescripcion (self):
    return self.__descripcion
  def setDescripcion (self, descripcion):
    self.__descripcion = descripcion
  def getOrientacion (self):
    return self.__orientacion
  def setOrientacion (self, orientacion):
    self.__orientacion = orientacion
  def getPosicion (self):
    return self.__posicion
  def setPosicion (self, posicion):
    self.__posicion = posicion
 
class CartaMonstruo(Carta):
  def __init__(self, nombre, descripcion, posicion,orientacion,tipo, atributo, defensa, ataque): #constructor
    super().__init__(nombre, descripcion, posicion,orientacion)
    self.__tipo = tipo
    self.__atributo = atributo
    self.__defensa = defensa
    self.__ataque = ataque

  def getTipo (self):
      return self.__tipo
  def setTipo (self, tipo):
      self.__tipo = tipo
  def getAtributo (self):
      return self.__atributo
  def setAtributo (self,atributo):
      self.__atributo = atributo
  def getAtaque (self):
      return self.__ataque
  def setAtaque (self, ataque):
      self.__ataque = ataque
  def getDefensa (self):
      return self.__defensa
  def setDefensa (self, defensa):
      self.__defensa = defensa
    
  def cambiarPosicion(self,posicion):
      if self.__orientacion == Orientacion.ARRIBA:
        self.__posicion = posicion
  def modoAtaque(self):
      self.__orientacion = Orientacion.ARRIBA
  def modoDefensa(self):
      self.__orientacion = Orientacion.ABAJO
  def muere(self): #NOT SURE
    return True
  def __str__(self):
    return f"{self.__nombre}: {self.__descripcion} con ATQ:{self.__ataque} y DEF:{self.__defensa}"

class CartaMagica (Carta):
  def __init__(self, nombre, descripcion, posicion, orientacion,ataque, defensa,tipo,carta_monstruo):
    super().__init__(nombre, descripcion, posicion, orientacion)
    self.__tipo = tipo
    self.__carta_monstruo = carta_monstruo
    self.__defensa = defensa
    self.__ataque = ataque
  
  def getTipo (self):
    return self.__tipo
  def getAtaque (self):
    return self.__ataque
  def setAtaque (self, ataque):
    self._ataque = ataque
  def getDefena (self):
    return self.__defensa
  def setDefensa (self, defensa):
    self.__defensa = defensa
    
  def usar (self,carta_monstruo):
    if self.__tipo == carta_monstruo.getTipo():
      if self.__defensa == 0:
        nuevo_ataque = carta_monstruo.getAtaque() + self._ataque
        carta_monstruo.setAtaque(nuevo_ataque)
      if self.__ataque == 0:
        nueva_defensa = carta_monstruo.getDefensa() + self.__defensa
        carta_monstruo.setDefensa(nueva_defensa)
  
  def destruir (self,carta_monstruo):#NOT SURE
    if carta_monstruo.muere():
      return True

  def __str__(self):
    if self.__defensa == 0:
      return f"{self.__nombre} , incrementa en {self.__ataque} el ataque de monstruos de tipo {self.__tipo}"
    if self.__ataque == 0:
      return f"{self.__nombre} , incrementa en {self.__defensa} la defensa de monstruos de tipo {self.__tipo}"

class CartaTrampa (Carta):
  def __init__(self, nombre, descripcion, posicion, orientacion,atributo,tipo):
    super().__init__(nombre, descripcion, posicion, orientacion)
    self.__atributo = atributo
    self.__carta_monstruo = carta_monstruo

  def getAtributo (self):
      return self.__atributo
  def setAtributo (self,atributo):
      self.__atributo = atributo
  def __str__(self):
    return f"{self.__nombre} , detiene el ataque de un monstruo tipo {self.__carta_monstruo.getAtributo()}"

from cartasCreadas import listaCartasCreadas
class Deck:
  def crearDeck(self):#crea lista de cartas
    l_mons=[]
    l_mag=[]
    l_tram=[]
    for c in listaCartasCreadas:
      if isinstance(c,CartaMonstruo):
        l_mons.append(c)
      if isinstance(c,CartaMagica):
        l_mag.append(c)
      if isinstance(c,CartaTrampa):
        l_tram.append(c)
      deck= rd.sample(l_mons,20)+rd.sample(l_mag,5)+rd.sample(l_tram,5)
    return deck

class Tablero:
  def _init_(self):
    self.__cartas= []


class Jugador:
  def __init__(self,nombre):
    self.__nombre = nombre
    self.__deck = Deck.crearDeck(self)
    self.__puntos = 4000
    self.__tablero = Tablero()
    self.__mano= [self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop()]
  def getNombre(self):
    return self.__nombre
  def setNombre (self, nombre):
    self.__nombre = nombre
  def getDeck (self):
    return self.__deck
  def setDeck (self, deck):
    self.__deck = deck
  def getPuntos (self):
    return self.__puntos
  def setPuntos (self, puntos):
    self.__puntos = puntos
  def getMano (self):
    return self.__mano

  def tomarCarta(self):
    return self.__deck.pop()
  def contar_cartas_tipo(self, tipo):
    for carta in self.__mano:
      return sum(isinstance(carta, tipo))
  def agregarCartaTablero(self,carta):
    if (len(self.__tablero)<=6):
      if isinstance(carta,CartaMonstruo):
        if self.contar_cartas_tipo(CartaMonstruo) < 3:
          self.__tablero.__cartas.append(carta)
          self.__mano.remove(carta)
        elif isinstance(carta, (CartaMagica, CartaTrampa)):
          if self.contar_cartas_tipo(CartaMagica) + self.contar_cartas_tipo(CartaTrampa) < 3:
            self.__tablero.__cartas.append(carta)
            self.__mano.remove(carta)
  def seleccionarCartaTablero(self,indice):
    return self.__tablero()[indice]



#Clase Juego 
class Juego():
  def __init__(self, maquina, jugador): #donde las lista tableros y jugadores tienen 2 elementos
    self.__maquina = maquina
    self.__jugador = jugador
    self.__turno = 0
  def faseDeclararBatalla(self, carta_oponente):
    if self.__turno < 2: 
      print("No se puede declarar batalla en el primer turno")
    else: #El turno es igual a 2 o mayor
      if(carta_oponente.posicion == Posicion.VERTICAL): #si es verdad, entonces quiere decir que esta en ataque
        return False    # se comparan los puntos de ataque de la carta de ataque al la carta atacada
    
      # else: #Si es falso, quiere decir que esta en defensa
  
  




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
  


class Maquina (Jugador):
  def __init__(self):
    super().__init__()
    self.__deck = Deck.crearDeck(self)
    self.__puntos = 4000
    self.__tablero = Tablero()
    self.__mano= [self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop()]

if __name__ == "__main__":
  print("Bienvenido al juego de Yugioh")
  nombre = input ("Por favor, ingrese su nombre: ")
  jugador = Jugador(nombre)
  maquina = Maquina()
  juego = Juego(jugador, maquina)
  juego.jugar()