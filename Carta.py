from Orientacion import *
class Carta:
  def __init__(self, nombre, descripcion, posicion,orientacion): #Constructor
    self.__nombre = nombre #__ es para acceso privado
    self.__descripcion = descripcion
    self.__posicion = posicion
    self.__orientacion = orientacion

  #getters y setters
  def getNombre (self):
    return self.__nombre
  def getDescripcion (self):
    return self.__descripcion
  def getOrientacion (self):
    return self.__orientacion
  def setOrientacion (self, orientacion):
    self.__orientacion = orientacion
  def getPosicion (self):
    return self.__posicion
  def setPosicion (self, posicion):
    self.__posicion = posicion
  def __str__(self):
    if self.__orientacion == Orientacion.ARRIBA:
      return f"{self.__nombre}\n{self.__descripcion}"
    else:
      return "Carta boca abajo"
  def __eq__(self, carta):
    if isinstance(value,Carta):
      if(self.__nombre==carta.__nombre):
        return True
      else:
        return False