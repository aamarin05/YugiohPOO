from Jugador import *
from Maquina import *
from Juego import *
c= CartaMonstruo("Dragón Blanco de Ojos Azules","Un dragón legendario",Posicion.VERTICAL,Orientacion.ARRIBA,TipoMonstruo.D,TipoAtributo.LUZ,2500,3000)
print(c)
if __name__ == "__main__":
  print("Bienvenido al juego de Yugioh")
  nombre = input ("Por favor, ingrese su nombre: ")
  jugador = Jugador(nombre)
  maquina = Maquina()
  juego = Juego(maquina, jugador)
  juego.jugar()
