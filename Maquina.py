from Jugador import *
class Maquina (Jugador):
  def __init__(self):
    super().__init__()
    self.__nombre = "Maquina"
    self.__deck = Deck.crearDeck(self)
    self.__puntos = 4000
    self.__tablero = Tablero()
    self.__mano= [self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop()]

  def ordenarMano(self):
    for carta in self.getMano():
      cartasMonstruo = []
      cartasTrampa = []
      cartasMagicas = []
      if isinstance(carta,CartaMonstruo):
        cartasMonstruo.append(carta)
      if isinstance(carta,CartaMagica):
        cartasMagicas.append(carta)
      if isinstance(carta,CartaTrampa):
        cartasTrampa.append(carta)
    return cartasMonstruo, cartasMagicas, cartasTrampa
  def obtenerMejoresCartas(listaCartas):
    cartasOrdenadas = sorted(listaCartas, key=lambda carta: carta.getAtaque() + carta.getDefensa(), reverse=True)
    return cartasOrdenadas[:3]
  def agregarMonstruoTablero(self,monstruo,modo):
    if len(self.__tablero.getMonstruos()) < 3:
      if modo == "ataque":
        monstruo.modoAtaque()
      if modo == "defensa":
        monstruo.modoDefensa()
      self.__tablero.getMonstruos().append(monstruo)

  #FASE PRINCIPAL DE LA MÁQUINA
  def mFasePrincipal(self):
    monstruos, magicas, trampas = self.ordenarMano()
    cartasMejores = self.obtenerMejoresCartas(monstruos)
    for monstruo in cartasMejores:
      if monstruo.getAtaque() < monstruo.getDefensa():
        self.agregarMonstruoTablero(monstruo,"defensa")
      else:
        self.agregarMonstruoTablero(monstruo,"ataque")
    for cartaM in magicas:
      self.agregarEspecialesTablero(cartaM)

  def agregarEspecialesTablero(self,especial):
    if len(self.__tablero.getEspeciales()) < 3:
      self.__tablero.getEspeciales().append(especial)
      
#COMO USA LA MAQUINA LAS CARTAS ESPECIALES
  def usarEspeciales(self):
    especiales = self.__tablero.getEspeciales()
    monstruos = self.__tablero.getMonstruos()
    cartasUsadas =[]
    for carta in especiales:
      for monstruo in monstruos:
        if carta not in cartasUsadas:
          if isinstance(carta,CartaMagica):
            if monstruo.getTipo() == carta.getTipo():
              carta.usar(monstruo)
              cartasUsadas.append(carta)
          if isinstance(carta, CartaTrampa):
            if monstruo.getAtributo() == carta.getAtributo():
              carta.usar(monstruo)
              cartasUsadas.append(carta)

  

      
