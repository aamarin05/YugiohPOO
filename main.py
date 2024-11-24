from enum import (Enum)
from cartasCreadas import cartas

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

  def activar (self, carta_monstruo): #CARTA MONSTRUO CONTRARIO
    if self.__atributo == carta_monstruo.getAtributo():
      carta_monstruo.getAtaque() = 0
  def __str__(self):
    print(f"{self.__nombre} , incrementa en {self.defensa} la defensa de monstruos de tipo {self.__tipo}")
  def decartar(self): #NOT SURE
    return True
      

class Deck:
  def __init__(self,cartas):
    self.__cartas = cartas
  def getCartas (self):
    return self.__cartas
  def setCartas (self, cartas):
    self.__cartas = cartas

class Tablero:
  def __init__(self, jugadores, cartas__monstruo, cartas_tram_o_mag):
    self.__cartas__monstruo = cartas__monstruo
    self.__cartas_tram_o_mag = cartas_tram_o_mag
    self.__jugadores = jugadores
  def getJugadores(self):
    return self.__jugadores
  def setJugadores(self, jugadores):
    self.__jugadores = jugadores
  def getCartasMonstruo(self):
    return self.__cartas__monstruo
  def set_espacio_m(self, cartas__monstruo):
    self.__cartas__monstruo = cartas__monstruo
  def getCartasTramOMag(self):
    return self.__cartas_tram_o_mag
  def setCartasTramOMag(self, cartas_tram_o_mag):
    self.__cartas_tram_o_mag = cartas_tram_o_mag


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




