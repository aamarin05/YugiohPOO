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
    archivo= open("cartasCreadas",'r')
    for linea in archivo.strip().split(','):
      if(linea[0]=="CartaMonstruo"):
        c= CartaMonstruo(nombre=linea[1],descripcion=linea[2],posicion=linea[3].strip(""),orientacion=linea[4].strip(""),tipomonstruo= linea[5].strip(""),atributo= linea[6].strip(""),defensa= int(linea[7]),ataque= int(linea[8]))
        l_mons.append(c)
      if(linea[0]=="CartaMagica"):
        c= CartaMagica(nombre=linea[1], descripcion=linea[2], posicion=linea[3].strip(""), orientacion=linea[4].strip(""), ataque= int(linea[5]), defensa= int(linea[6]),tipomonstruo= linea[7].strip(""))
        l_mag.append(c)
      if(linea[0]=="CartaTrampa"):
        c= CartaTrampa(nombre=linea[1], descripcion=linea[2], posicion=linea[3].strip(""),  orientacion=linea[4].strip(""),atributo= linea[5].strip(""))
        l_tram.append(c)
      archivo.close()
      deck=rd.sample(l_mons,20)+rd.sample(l_mag,5)+rd.sample(l_tram,5)
      return deck