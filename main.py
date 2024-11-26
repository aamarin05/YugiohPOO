from Jugador import *
from Maquina import *
from Juego import *

if __name__ == "__main__":
  print("Bienvenido al juego de Yugioh")
  nombre = input ("Por favor, ingrese su nombre: ")
  jugador = Jugador(nombre)
  maquina = Maquina()
  juego = Juego(jugador, maquina)
  juego.jugar()
