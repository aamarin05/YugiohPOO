from cartasCreadas import listaCartasCreadas
from CartaMonstruo import *
from CartaTrampa import *
from CartaMagica import *
import random as rd



class Deck:
  def crearDeck(self):#crea lista de cartas
    l_mons=[]
    l_mag=[]
    l_tram=[]
    for c in listaCartasCreadas:
      if isinstance(c,CartaMonstruo):
        l_mons.append(c)
      if isinstance(c,CartaMagica):
        l_mag.append(c)
      if isinstance(c,CartaTrampa):
        l_tram.append(c)
      deck= rd.sample(l_mons,20)+rd.sample(l_mag,5)+rd.sample(l_tram,5)
    return deck