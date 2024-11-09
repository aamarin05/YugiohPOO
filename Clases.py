from enum import (Enum)

class TipoAtributo (Enum):
  OSCURIDAD = 1
  LUZ = 2
  TIERRA = 3
  AGUA = 4
  FUEGO = 5
  VIENTO = 6

class TipoCarta (Enum):
  MONTRUO = 1
  MAGICA = 2
  TRAMPA = 3

class TipoMonstruo (Enum):
  LANZADOR_CONJUROS = 1
  DRAGON = 2
  ZOMBI = 3
  GUERRERO = 4
  BESTIA = 5
  DEMONIO = 6

class Orientacion (Enum):
  BOCA_ARRIBA = 1
  BOCA_ABAJO = 2

class Carta:
  def __init__(self, nombre, descripcion,tipo_carta,tipo_atributo,ataque,defensa,orientacion): #constructor
    self.__nombre = nombre #__ es para acceso privado
    self.__descripcion = descripcion
    self.__tipo_carta = tipo_carta
    self.__ataque = ataque
    self.__defensa = defensa
    self.__tipo_atributo = tipo_atributo
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

class Deck:
  def __init__(self,cartas):
    self.__cartas = cartas

class Tablero:
  def __init__(self, jugadores, espacio_m, espacio_magicoTrampa):
    self.__espacio_m = espacio_m
    self.__espacio_tom = espacio_magicoTrampa
    self.__jugadores = jugadores

class Jugador:
  def __init__(self,deck,puntos):
    self.__deck = deck
    self.__puntos = deck