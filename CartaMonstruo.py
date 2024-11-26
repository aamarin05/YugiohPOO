from Carta import *
from Posicion import *
from Orientacion import *
from TipoAtributo import *
from TipoMonstruo import *

class CartaMonstruo(Carta):
  def __init__(self, nombre, descripcion, posicion,orientacion,tipo, atributo, defensa, ataque): #constructor
    super().__init__(nombre, descripcion, posicion,orientacion)
    self.__tipo = tipo
    self.__atributo = atributo
    self.__defensa = defensa
    self.__ataque = ataque

  def getTipo (self):
      return self.__tipo
  def getAtributo (self):
      return self.__atributo
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
      elif (self.__ataque < carta_oponente.getAtaque()):
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

  def __str__(self):
    return f"{self.__nombre}: {self.__descripcion} con ATQ:{self.__ataque} y DEF:{self.__defensa}"