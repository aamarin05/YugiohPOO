from enum import (Enum)

class TipoAtributo (Enum):
  OSCURIDAD = 1
  LUZ = 2
  TIERRA = 3
  AGUA = 4
  FUEGO = 5
  VIENTO = 6

class TipoCarta (Enum):
  MONSTRUO = 1
  MAGICA = 2
  TRAMPA = 3

class TipoMonstruo (Enum):
  L = 1 #Lanazador de Conjuros
  D = 2 #Dragon
  Z = 3 #Zombi
  G = 4 #Guerrero
  B = 5 #Bestia
  O = 6 #Demonio

class Orientacion (Enum):
  BOCA_ARRIBA = 1
  BOCA_ABAJO = 2

class Carta:
  def __init__(self, nombre, descripcion,tipo_carta,tipo_atributo,tipo_monstruo,ataque,defensa,orientacion): #constructor
    self.__nombre = nombre #__ es para acceso privado
    self.__descripcion = descripcion
    self.__tipo_carta = tipo_carta

    if (tipo_carta == TipoCarta.MONSTRUO):
      self.__tipo_atributo = tipo_atributo
      self.__tipo_monstruo = tipo_monstruo
      self.__ataque = ataque
      self.__defensa = defensa
      self.__orientacion = orientacion
    if (tipo_carta == TipoCarta.TRAMPA):
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
  def getTipo_carta (self):
    return self.__tipo_carta
  def setTipo_carta (self, tipo_carta):
    self.__tipo_carta = tipo_carta
  def getTipo_atributo (self):
    return self.__tipo_atributo
  def setTipo_atributo (self, tipo_atributo):
    self.__tipo_atributo = tipo_atributo
  def getAtaque (self):
    return self.__ataque
  def setAtaque (self, ataque):
    self.__ataque = ataque
  def getDefena (self):
    return self.__defensa
  def setNombre (self, defensa):
    self.__defensa = defensa
  def getOrientacion (self):
    return self.__orientacion
  def setOrientacion (self, orientacion):
    self.__orientacion = orientacion
  def getTipo_monstruo (self):
    return self.__tipo_monstruo
  def setTipo_monstruo (self, tipo_monstruo):
    self.__tipo_monstruo = tipo_monstruo


class Deck:
  def __init__(self,cartas):
    self.__cartas = cartas
  def getCartas (self):
    return self.__cartas
  def setCartas (self, cartas):
    self.__cartas = cartas

class Tablero:
  def __init__(self, jugadores, espacio_m, espacio_magicoTrampa):
    self.__espacio_m = espacio_m
    self.__espacio_tom = espacio_magicoTrampa
    self.__jugadores = jugadores
  def get_jugadores(self):
    return self._jugadores
  def set_jugadores(self, jugadores):
    self._jugadores = jugadores
  def get_espacio_m(self):
    return self._espacio_m
  def set_espacio_m(self, espacio_m):
    self._espacio_m = espacio_m
  def get_espacio_magicoTrampa(self):
    return self._espacio_magicoTrampa
  def set_espacio_magicoTrampa(self, espacio_magicoTrampa):
    self._espacio_magicoTrampa = espacio_magicoTrampa


class Jugador:
  def __init__(self,deck,puntos):
    self.__deck = deck
    self.__puntos = 4000
  def getDeck (self):
    return self.__deck
  def setDeck (self, deck):
    self.__deck = deck
  def getPuntos (self):
    return self.__puntos
  def setPuntos (self, puntos):
    self.__puntos = puntos