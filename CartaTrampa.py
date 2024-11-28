from Carta import *
from Posicion import *
from Orientacion import *
from TipoAtributo import *
from TipoMonstruo import *

class CartaTrampa (Carta):
  def __init__(self, nombre, descripcion, posicion, orientacion,atributo):
    super().__init__(nombre, descripcion, posicion, orientacion)
    self.__atributo = atributo
    self.__orientacion = Orientacion.ABAJO

#GETTER
  def getAtributo (self):
      return self.__atributo
  
#FUNCIÓN JUGABLE
  def usar(self,cartaAtacante):#UNA CARTA TRAMPA SE USA Y TIENE COMO ARGUMENTO UNA CARTAMonstruo
    if self.__atributo == cartaAtacante.getAtributo():
      print(f"Carta Trampa:{self.getNombre()} , detuvo el ataque de un monstruo con atributo {self.__atributo}")
      return True
    else:
      return False

#TO STRING
  def __str__(self):
    return f"Carta Trampa: {self.getNombre()} , detiene el ataque de un monstruo con atributo {self.__atributo}"
