from Jugador import *
from Tablero import *
class Maquina:
  def __init__(self):
    self.__nombre = "Maquina"
    self.__deck = Deck.crearDeck()
    self.__puntos = 4000
    self.__tablero = Tablero()
    self.__mano= [self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop(),self.__deck.pop()]

#SETTERS Y GETTERS
  def getNombre(self):
    return self.__nombre
  def getPuntos (self):
    return self.__puntos
  def setPuntos (self, puntos):
    self.__puntos = puntos
  def getMano (self):
    return self.__mano 
  def getTablero(self):
    return  self.__tablero 

#FUNCIONES DE LA MAQUINA PARA AGREGAR Y ORDENAR
  def ordenarMano(self): #ORDENA LA MANO SEPARANDO LAS CARTAS EN SUS TIPOS
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
  
  def obtenerMejoresCartas(self,listaCartas): #LAS 3 MEJORES CARTAS SON LAS QUE LA SUMA DE SU ATAQUE Y DEFENSA ES LA MAYOR ENTRE TODAS
    cartasOrdenadas = sorted(listaCartas, key=lambda carta: carta.getAtaque() + carta.getDefensa(), reverse=True)
    return cartasOrdenadas[:3]
  
  def agregarMonstruoTablero(self,monstruo,modo):
    if len(self.__tablero.getMonstruos()) < 3: #SI LOS ESPACIOS DE MONSTRUO NO ESTÁN LLENOS
      if modo == "ataque":
        monstruo.modoAtaque()
      if modo == "defensa":
        monstruo.modoDefensa()
      self.getTablero().getMonstruos().append(monstruo)
      self.getMano().remove(monstruo)

  def agregarEspecialesTablero(self,especial):
    if len(self.getTablero().getEspeciales()) < 3:
      self.getTablero().getEspeciales().append(especial)

#FASE PRINCIPAL DE LA MÁQUINA EN CADA TURNO SE LLAMA
  def mFasePrincipal(self):
    monstruos, magicas, trampas = self.ordenarMano() #ORDENA LA MANO SEPARANDO LAS CARTAS EN SUS TIPOS
    cartasMejores = self.obtenerMejoresCartas(monstruos) #CARTAS MEJORES DE MONSTRUOS
    for monstruo in cartasMejores: #QUE HACE CON LOS 3 MEJORES MONSTRUOS
      if monstruo.getAtaque() < monstruo.getDefensa(): #SI SU DEFENSA ES MAYOR LA COLOCARÁ BOCA ABAJO
        self.agregarMonstruoTablero(monstruo,"defensa")
      else: #SI SU ATAQUE ES MAYOR O IGUAL A SU DEENSA, MODO ATAQUE
        self.agregarMonstruoTablero(monstruo,"ataque")
    for cartaT in trampas: #INTENTA PONER LAS CARTAS TRAMPA PRIMERO HASTA QUE YA NO HAYA EN LA MANO O NO SE PUEDAN COLOR
      self.agregarEspecialesTablero(cartaT)
    for cartaM in magicas: #INTENTA COLOCAR CARTAS MAGICAS AL TABLERO SI NO HAY CARTAS TRAMPA PRIMERO, HASTA QUE YA NO SE PUEDAN COLOCAR
      self.agregarEspecialesTablero(cartaM)
      
#COMO USA LA MAQUINA LAS CARTAS ESPECIALES
  def usarEspeciales(self):
    especiales = self.__tablero.getEspeciales()
    monstruos = self.__tablero.getMonstruos()
    cartasUsadas =[] #PARA NO INTENTAR USAR LA MISMA CARTA CON OTRO MONSTRUO
    for carta in especiales:
      if carta not in cartasUsadas:#SI SE USA LA CARTA YA NO SE VUELVE A USAR
        for monstruo in monstruos: #SI NO SE USA VA A TRATAR DE USARLA CON EL SIGUIENTE MONSTRUO
          if isinstance(carta,CartaMagica):
              carta.usar(monstruo)
              cartasUsadas.append(carta)

#FUNCION DE JUGADOR
  def tomarCarta(self):
    carta=self.__deck.pop()
    self.__mano.append(carta)
    print(f"Maquina la carta {carta.getNombre()}")

  def manoImprimir(self):
    mostrar= ""
    for i in range(len(self.__mano)):  
        carta = self.__mano[i]         
        mostrar += f"{i + 1}. {carta.__str__()}\n"
    return f"Usted tiene en su mano:\n{mostrar}"

  def seleccionarCartaMano(self,indice):
    return self.__mano[indice]
  
  def agregarCartaTablero(self,indice):
    carta = self.getMano()[indice]
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

#TO STRING 
  def __str__ (self):
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

