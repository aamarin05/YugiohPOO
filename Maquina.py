from Jugador import *
class Maquina:
  def __init__(self):
    self.__nombre = "Maquina"
    self.__deck = Deck.crearDeck()
    self.__puntos = 4000
    self.__tablero = Tablero()
    self.__mano= [self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop()]
  def getMano (self):
    return self.__mano
  def getPuntos (self):
    return self.__puntos
  def getTablero(self):
    return  self.__tablero  
  

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
  
  def obtenerMejoresCartas(self,listaCartas):
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

  def tomarCarta(self):
    carta=self.__deck.pop()
    self.__mano.append(carta)
    print(f"Tomaste la carta {carta.getNombre()}")

  def manoImprimir(self):
    mostrar= ""
    for i in range(len(self.__mano)):  
        carta = self.__mano[i]         
        mostrar += f"{i + 1}. {carta.__str__()}\n"
    return f"Usted tiene en su mano:\n{mostrar}"

  def seleccionarCartaMano(self,indice):
    return self.__mano[indice]
  
  def agregarCartaTablero(self,indice):
      carta = self.getMano()[indice-1]
      if isinstance(carta,CartaMonstruo):
        if len(self.__tablero.getMonstruos()) < 3:
          pos = input("1.Modo Ataque, 2. Modo Defensa:")
          while (pos != "1") and (pos !="2"):
            print("Ingrese (1 o 2)")
            pos = input("1.Modo Ataque, 2. Modo Defensa:")
          if pos == "1":
            carta.modoAtaque()
            self.__tablero.getMonstruos().append(carta)
            self.__mano.remove(carta)
          elif pos == "2":
            carta.modoDefensa()
            self.__tablero.getMonstruos().append(carta)
            self.__mano.remove(carta)
          print(f"Se ha agregado la carta monstruo {carta} al tablero")
        else:
          print("Espacio para carta tipo Monstruo lleno en el tablero")
      else:
        if len(self.__tablero.getEspeciales()) < 3:
          self.__tablero.getEspeciales().append(carta)
          self.__mano.remove(carta)
          print(f"Se ha agregado la carta especial {carta} al tablero")
        else:
          print("Espacio para cartas tipo Magica o Trampa lleno en el tablero")

  def seleccionarCartaTablero(self,indice):
    return self.__tablero[indice]
  def __str__ (self):
    print (f"{self.__nombre}: {self.__puntos} Lp\n{self.__tablero._str_()}")
    if self.__nombre=="Maquina":
      monstruos = []
      especiales = []

      for i in range(3):
          if i < len(self.__tablero.getMonstruos()):
              monstruos.append(str(self.__tablero.getMonstruos()[i]))
          else:
              monstruos.append("No hay cartas")

      for i in range(3):
          if i < len(self.__tablero.getEspeciales()):
              especiales.append(str(self.__tablero.getEspeciales()[i]))
          else:
              especiales.append("No hay cartas")
      return(f"{self.__nombre} - Lp:{self.__puntos}\nEspeciales: [{especiales[0]}] [{especiales[1]}] [{especiales[2]}]\nMonstruo: [{monstruos[0]}] [{monstruos[1]}] [{monstruos[2]}]")  
    else:
      return(f"Monstruo: [{monstruos[0]}] [{monstruos[1]}] [{monstruos[2]}]\nEspeciales: [{especiales[0]}] [{especiales[1]}] [{especiales[2]}]")

