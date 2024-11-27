from Carta import *
from Posicion import *
from Orientacion import *
from TipoAtributo import *
from TipoMonstruo import *

class CartaTrampa (Carta):
  def __init__(self, nombre, descripcion, posicion, orientacion,atributo):
    super().__init__(nombre, descripcion, posicion, orientacion)
    self.__atributo = atributo

  def getAtributo (self):
      return self.__atributo
  
  def usar(self,cartaAtacante):
    if self.__atributo == cartaAtacante.getAtributo():
      print(f"Carta Trampa:{self.__nombre} , detuvo el ataque de un monstruo con atributo {self.__atributo}")

  def __str__(self):
    return f"Carta Trampa: {self.getNombre()} , detiene el ataque de un monstruo con atributo {self.__atributo}"
