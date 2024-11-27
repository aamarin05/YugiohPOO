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
        c= CartaMonstruo(linea[1],linea[2],Posicion[linea[3]],Orientacion[linea[4]], TipoMonstruo[linea[5]],TipoAtributo[linea[6]],int(linea[7]),int(linea[8]))
        l_mons.append(c)
      if(linea[0]=="CartaMagica"):
        c= CartaMagica(linea[1], linea[2], Posicion[linea[3]], Orientacion[linea[4]],  int(linea[5]), int(linea[6]), TipoMonstruo[linea[5]])
        l_mag.append(c)
      if(linea[0]=="CartaTrampa"):
        c= CartaTrampa(linea[1], linea[2], Posicion[linea[3]], Orientacion[linea[4]], TipoAtributo[linea[6]])
        l_tram.append(c)
      archivo.close()
      deck=rd.sample(l_mons,20)+rd.sample(l_mag,5)+rd.sample(l_tram,5)
      return deck