from CartaMonstruo import *
from CartaTrampa import *
from CartaMagica import *
from TipoAtributo import *
from TipoMonstruo import *
import random as rd

class Deck:
  def crearDeck(self):
    l_mons=[]
    l_mag=[]
    l_tram=[]
    archivo= open("cartasCreadas.txt",'r')
    for linea in archivo:
      linea = linea.strip().split(',')
      if(linea[0]=="CartaMonstruo"):
        c= CartaMonstruo(nombre=linea[1],descripcion=linea[2],posicion=Posicion[linea[3]],orientacion=Orientacion[linea[4]],tipomonstruo= TipoMonstruo[linea[5]],atributo= TipoAtributo[linea[6]],defensa= int(linea[7]),ataque= int(linea[8]))
        l_mons.append(c)
      if(linea[0]=="CartaMagica"):
        c= CartaMagica(nombre=linea[1], descripcion=linea[2], posicion=Posicion[linea[3]], orientacion=Orientacion[linea[4]], ataque= int(linea[5]), defensa= int(linea[6]),tipomonstruo= TipoMonstruo[linea[5]])
        l_mag.append(c)
      if(linea[0]=="CartaTrampa"):
        c= CartaTrampa(nombre=linea[1], descripcion=linea[2], posicion=Posicion[linea[3]], orientacion=Orientacion[linea[4]],atributo= TipoAtributo[linea[6]])
        l_tram.append(c)
      archivo.close()
      deck=rd.sample(l_mons,20)+rd.sample(l_mag,5)+rd.sample(l_tram,5)
      return deck