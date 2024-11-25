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
  
  # Metodo atacar carta oponente
  def atacarCarta(self, carta_oponente): #retorna la diferencia de puntos de las dos cartas
    diferencia_puntos = 0
    if (carta_oponente.getPosicion() == Posicion.VERTICAL): # queire decir que esta en ataque
      if (self.__ataque > carta_oponente.getAtaque()):
        diferencia_puntos = self.__ataque - carta_oponente.getAtaque()
        return diferencia_puntos
      elif (self.__ataque < carta_oponente.getAtaque):
        diferencia_puntos = carta_oponente.getAtaque() - self.__ataque
        return diferencia_puntos
      else: 
        diferencia_puntos = 0
    else: # carta atacada esta en defensa
      if (self.__ataque > carta_oponente.getDefensa()):
        diferencia_puntos = self.__ataque - carta_oponente.getDefensa()
        return diferencia_puntos
      elif (self.__ataque < carta_oponente.getDefensa):
        diferencia_puntos = carta_oponente.getDefensa() - self.__ataque
        return diferencia_puntos
      else: 
        diferencia_puntos = 0


class CartaMagica (Carta):
  def __init__(self, nombre, descripcion, posicion, orientacion,ataque, defensa,tipo,carta_monstruo):
    super().__init__(nombre, descripcion, posicion, orientacion)
    self.__tipo = tipo
    self.__carta_montruo = carta_monstruo
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
      return f"{self.__nombre} , incrementa en {self._ataque} el ataque de monstruos de tipo {self.__tipo}"
    if self.__ataque == 0:
      return f"{self.__nombre} , incrementa en {self.defensa} la defensa de monstruos de tipo {self.__tipo}"

class CartaTrampa (Carta):
  def __init__(self, nombre, descripcion, posicion, orientacion,atributo,carta_monstruo):
    super().__init__(nombre, descripcion, posicion, orientacion)
    self.__atributo = atributo

  def getAtributo (self):
      return self.__atributo
  def setAtributo (self,atributo):
      self.__atributo = atributo
from cartasCreadas import cartas
class Deck:
  def crearDeck(self,archivo):
    l_mons=[]
    l_mag=[]
    l_tram=[]
    archivo= open(archivo,'r')
    for linea in archivo.strip().split(','):
      nombre,descripcion,tipodecarta,posicion,orientacion,ataque,defensa,tipomonstruo,tipoatributo= linea
      if(tipodecarta==TipoCarta.MONSTRUO):
        c= CartaMonstruo(nombre,descripcion,posicion,orientacion,tipomonstruo,tipoatributo,defensa,ataque)
        l_mons.append(c)
      if(tipodecarta==TipoCarta.MAGICA):
        c= CartaMagica(nombre, descripcion, posicion, orientacion, ataque, defensa)
        l_mag.append(c)
      if(tipodecarta==TipoCarta.TRAMPA):
        c= CartaTrampa(nombre, descripcion, posicion, orientacion,tipoatributo)
        l_tram.append(c)
      archivo.close()
      deck=rd.sample(l_mons,20)+rd.sample(l_mag,5)+rd.sample(l_tram,5)
      return deck

class Tablero:
  def _init_(self):
    self.cartas= []
  def contar_cartas_tipo(self, tipo):
    for carta in self.cartas:
      return sum(isinstance(carta, tipo))
  def agregarCarta(self,carta):
    if (len(cartas)<=6):
      if isinstance(carta,CartaMonstruo):
        if self.contar_cartas_tipo(Monstruo) < 3:
          self.cartas.append(carta)
        elif isinstance(carta, (Magica, Trampa)):
          if self.contar_cartas_tipo(Magica) + self.contar_cartas_tipo(Trampa) < 3:
            self.cartas.append(carta)
  def seleccionarCarta(self,nombre):
    for c in self.cartas:
      if (c.getNombre()==nombre):
        return c


class Jugador:
  def __init__(self,nombre,deck):
    self.__nombre = nombre
    self.__deck = deck
    self.__puntos = 4000
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



#Clase Juego 
class Juego():
  def __init__(self, Lista_tableros, l_jugadores, turnoJugador): 
    self.__tableros = Lista_tableros 
    self.__jugadores = l_jugadores
    self.__turnoJuego = 0
    self.__turnoJugador = turnoJugador # 0 para la persona y 1 para la maquina
  # def faseDeclararBatalla(self, carta_oponente):
    
  #   if self.__turno < 2: 
  #     print("No se puede declarar batalla en el primer turno")
  #   else: #El turno es igual a 2 o mayor
  #     diferencia_puntos = self.atacarCarta(carta_oponente)
  #     if()
    
  #     # else: #Si es falso, quiere decir que esta en defensa
  
  def faseDeclararBatalla(self):
    if (self.__jugadores[self.__turnoJugador] == "MAQUINA"):
      if self.__turnoJuego < 2: 
        print("No se puede declarar batalla en el primer turno")
      else:
        # carta_atacante   = rd.choice(self.__tableros[self.__turnoJugador])
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