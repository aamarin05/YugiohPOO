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
  def eModoAtaque(self):
      if self.__posicion== Posicion.VERTICAL:
          return True
      else:
          return False
  def eModoDefensa(self):
      if self.__posicion== Posicion.HORIZONTAL:
          return True
      else:
          return False
  def muere(self): #NOT SURE
    return True
  def __str__(self):
    if self.__posicion== Posicion.VERTICAL:
        modo= "ATAQUE"
    else:
        modo= "DEFENSA"
    return f"Carta Monstruo\nModo:{modo}\n{super().__str__()}\nATQ:{self.__ataque}\nDEF:{self.__defensa}"