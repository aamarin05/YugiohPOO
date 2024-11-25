from main import CartaMonstruo, CartaMagica, CartaTrampa
from main import TipoAtributo, TipoMonstruo, Orientacion, Posicion


cartas = [
    # Cartas de Monstruo (50 cartas)
    CartaMonstruo("Dragón Blanco de Ojos Azules", "Un dragón legendario", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.D, TipoAtributo.LUZ, 2500, 3000),
    CartaMonstruo("Mago Oscuro", "Un mago experto", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.L, TipoAtributo.OSCURIDAD, 2100, 2500),
    CartaMonstruo("Guerrero de la Llama", "Un guerrero imbatible", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.G, TipoAtributo.FUEGO, 1200, 1800),
    CartaMonstruo("Dragón de Fuego", "Un dragón envuelto en llamas", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.D, TipoAtributo.FUEGO, 1500, 2000),
    CartaMonstruo("Rey Bestia", "El líder de las bestias salvajes", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.TIERRA, 1600, 1900),
    CartaMonstruo("Zombi Infectado", "Un no-muerto aterrador", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.Z, TipoAtributo.OSCURIDAD, 1200, 1600),
    CartaMonstruo("Caballero de la Luz", "Un caballero radiante", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.G, TipoAtributo.LUZ, 1400, 1700),
    CartaMonstruo("Demonio del Abismo", "Un demonio que surge de las profundidades", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.O, TipoAtributo.OSCURIDAD, 2000, 2400),
    CartaMonstruo("Águila de Viento", "Una criatura que domina los cielos", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.VIENTO, 1300, 1500),
    CartaMonstruo("Titán de Agua", "Un coloso acuático", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.G, TipoAtributo.AGUA, 1900, 2200),
    CartaMonstruo("Golem de Piedra", "Un monstruo inmenso con un gran poder defensivo", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.G, TipoAtributo.TIERRA, 1500, 3000),
    CartaMonstruo("Dragón de Acero", "Un dragón mecánico con resistencia imparable", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.D, TipoAtributo.TIERRA, 2300, 2200),
    CartaMonstruo("Bestia Salvaje", "Una criatura de gran velocidad y fuerza", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.VIENTO, 1800, 1500),
    CartaMonstruo("Caballero Oscuro", "Un caballero vengativo con poder destructivo", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.G, TipoAtributo.OSCURIDAD, 1700, 1600),
    CartaMonstruo("Luchador Fantasma", "Un espectro de guerrero con gran destreza en combate", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.Z, TipoAtributo.OSCURIDAD, 1600, 1200),
    CartaMonstruo("Zombi Destructor", "Un zombi con un cuerpo irrompible", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.Z, TipoAtributo.OSCURIDAD, 2000, 2000),
    CartaMonstruo("Dragón Infernal", "Un dragón de fuego con poderes destructivos", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.D, TipoAtributo.FUEGO, 2500, 2100),
    CartaMonstruo("Guerrero Noble", "Un guerrero de honor con gran poder de ataque", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.G, TipoAtributo.LUZ, 2200, 1800),
    CartaMonstruo("Aquelarre de Bestias", "Un grupo de bestias salvajes en feroz ataque", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.TIERRA, 1900, 1900),
    CartaMonstruo("Demonio Destructor", "Un demonio con un inmenso poder de ataque", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.O, TipoAtributo.OSCURIDAD, 2500, 2000),
    CartaMonstruo("Grifo Alado", "Un monstruo con alas poderosas que puede volar rápidamente", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.D, TipoAtributo.VIENTO, 2100, 1500),
    CartaMonstruo("Lobo Gigante", "Un feroz lobo con gran velocidad y agilidad", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.TIERRA, 1800, 1400),
    CartaMonstruo("Hechicero Oscuro", "Un hechicero con poderes oscuros y magia destructiva", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.L, TipoAtributo.OSCURIDAD, 2500, 2000),
    CartaMonstruo("César Dragón", "Un dragón noble con gran resistencia y poder", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.D, TipoAtributo.LUZ, 2400, 2100),
    CartaMonstruo("Lanceros Zombis", "Un grupo de lanceros zombis que luchan en conjunto", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.Z, TipoAtributo.OSCURIDAD, 1700, 1000),
    CartaMonstruo("Bestia Mística", "Una criatura mística con poderosos ataques físicos", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.TIERRA, 1900, 1700),
    CartaMonstruo("Dragón Alado de la Oscuridad", "Un dragón que controla las sombras para atacar a su oponente", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.D, TipoAtributo.OSCURIDAD, 2800, 2400),
    CartaMonstruo("Guerrero Celestial", "Un guerrero con poderes místicos que defiende el reino", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.G, TipoAtributo.LUZ, 2200, 2000),
    CartaMonstruo("Luchador Imparable", "Un luchador con gran agilidad y fuerza, capaz de superar cualquier obstáculo", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.G, TipoAtributo.FUEGO, 2300, 1500),
    CartaMonstruo("Demonio del Abismo", "Un demonio con un poder destructivo capaz de destruir todo lo que toca", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.O, TipoAtributo.OSCURIDAD, 2600, 2300),
    CartaMonstruo("Caballero de Hierro", "Un caballero blindado con gran defensa", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.G, TipoAtributo.TIERRA, 1500, 2500),
    CartaMonstruo("Draco Espacial", "Un dragón que viaja entre las estrellas con gran rapidez", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.D, TipoAtributo.VIENTO, 2200, 1700),
    CartaMonstruo("Zombi Destructor", "Un zombi con habilidades mejoradas y un poder de ataque letal", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.Z, TipoAtributo.OSCURIDAD, 2400, 1800),
    CartaMonstruo("Furia de Fuego", "Una criatura de fuego que inflige daño masivo", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.FUEGO, 1900, 1200),
    CartaMonstruo("Dragón Submarino", "Un dragón acuático con una defensa impenetrable", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.D, TipoAtributo.AGUA, 2100, 2200),
    CartaMonstruo("Sombra del Demonio", "Una criatura demoníaca con la capacidad de absorber la energía de sus enemigos", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.O, TipoAtributo.OSCURIDAD, 2600, 1500),
    CartaMonstruo("Fuerza Bestial", "Una bestia salvaje que tiene una fuerza increíble", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.TIERRA, 2300, 1800),
    CartaMonstruo("Mago del Fuego", "Un hechicero que controla las llamas para atacar a su oponente", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.L, TipoAtributo.FUEGO, 2000, 1600),
    CartaMonstruo("Guerrero Eléctrico", "Un guerrero que usa electricidad para atacar y paralizar a sus enemigos", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.G, TipoAtributo.VIENTO, 2100, 1700),
    CartaMonstruo("Bestia Fantasmagórica", "Una bestia fantasmagórica que ataca desde las sombras", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.OSCURIDAD, 1900, 1500),
    CartaMonstruo("Dragón de Fuego Infernal", "Un dragón envuelto en llamas que quema todo lo que toca", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.D, TipoAtributo.FUEGO, 2600, 2100),
    CartaMonstruo("Espíritu del Guerrero", "El espíritu de un guerrero que regresa para luchar con gran coraje", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.G, TipoAtributo.LUZ, 1800, 1500),
    CartaMonstruo("Lobo Fantasma", "Un lobo que acecha en las sombras y ataca sin previo aviso", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.OSCURIDAD, 1600, 1200),
    CartaMonstruo("Tiburón Dragón", "Un monstruo acuático y dracónico con gran capacidad de ataque y defensa", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.D, TipoAtributo.AGUA, 2200, 1800),
    CartaMonstruo("Demonio Celestial", "Un demonio con poderes sobrenaturales que domina el cielo", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.O, TipoAtributo.LUZ, 2400, 2000),
    CartaMonstruo("Sombra del Zombi", "Un zombi que se mueve sigilosamente, atacando en la oscuridad", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.Z, TipoAtributo.OSCURIDAD, 1700, 1100),
    CartaMonstruo("Golem de Tierra", "Un golem de piedra con una defensa impenetrable y gran resistencia", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.TIERRA, 2500, 2400),
    CartaMonstruo("Halcón Celestial", "Un halcón con alas doradas que puede volar a grandes velocidades", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.LUZ, 2000, 1700),
    CartaMonstruo("Vampiro Sombrío", "Un vampiro con poderes oscuros que drena la vida de sus enemigos", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.O, TipoAtributo.OSCURIDAD, 2100, 1600),
    CartaMonstruo("Rayo Bestial", "Una bestia con poderes eléctricos, capaz de destruir cualquier obstáculo", Posicion.VERTICAL, Orientacion.ABAJO, TipoMonstruo.B, TipoAtributo.VIENTO, 2200, 1900),

    # Cartas Mágicas (15 cartas)
    CartaMagica("Espada de Arturo", "Incrementa el ataque de guerreros", Posicion.HORIZONTAL, Orientacion.ABAJO, 200, 0, "Guerrero"),
    CartaMagica("Escudo de Chamelote", "Incrementa la defensa de guerreros", Posicion.HORIZONTAL, Orientacion.ABAJO, 0, 200, "Guerrero"),
    CartaMagica("Poder de la Luz", "Incrementa el ataque de monstruos de luz", Posicion.HORIZONTAL, Orientacion.ABAJO, 300, 0, "LUZ"),
    CartaMagica("Fuerza de la Oscuridad", "Incrementa la defensa de monstruos oscuros", Posicion.HORIZONTAL, Orientacion.ABAJO, 0, 300, "OSCURIDAD"),
    CartaMagica("Llama Ardiente", "Incrementa el ataque de monstruos de fuego", Posicion.HORIZONTAL, Orientacion.ABAJO, 400, 0, "FUEGO"),
    CartaMagica("Barrera Protectora", "Aumenta la defensa de todos los monstruos", Posicion.HORIZONTAL, Orientacion.ABAJO, 0, 150, "Todo"),
    CartaMagica("Espada Ardiente", "Aumenta el ataque de los monstruos fuego", Posicion.HORIZONTAL, Orientacion.ABAJO, 250, 0, "FUEGO"),
    CartaMagica("Luz Radiante", "Aumenta el ataque de los monstruos de luz", Posicion.HORIZONTAL, Orientacion.ABAJO, 300, 0, "LUZ"),
    CartaMagica("Escudo del Guerrero", "Aumenta la defensa de los guerreros", Posicion.HORIZONTAL, Orientacion.ABAJO, 0, 200, "Guerrero"),
    CartaMagica("Fuerza Viento", "Aumenta el ataque de los monstruos viento", Posicion.HORIZONTAL, Orientacion.ABAJO, 250, 0, "VIENTO"),
    CartaMagica("Magia Curativa", "Recupera 1000 puntos de vida", Posicion.HORIZONTAL, Orientacion.ABAJO, 0, 0, "Curativa"),
    CartaMagica("Potencia Oscura", "Incrementa el ataque de monstruos oscuros", Posicion.HORIZONTAL, Orientacion.ABAJO, 300, 0, "OSCURIDAD"),
    CartaMagica("Tornado Mágico", "Destruye una carta mágica o trampa", Posicion.HORIZONTAL, Orientacion.ABAJO, 0, 0, "Destrucción"),
    CartaMagica("Fuerza Espiritual", "Aumenta la defensa de los monstruos de luz", Posicion.HORIZONTAL, Orientacion.ABAJO, 0, 300, "LUZ"),
    CartaMagica("Fuego Eterno", "Aumenta el ataque de los monstruos fuego", Posicion.HORIZONTAL, Orientacion.ABAJO, 300, 0, "FUEGO"),
    CartaMagica("Escudo Divino", "Aumenta la defensa de los monstruos de fuego", Posicion.HORIZONTAL, Orientacion.ABAJO, 0, 250, "FUEGO"),
    CartaMagica("Luz Brillante", "Aumenta el ataque de los monstruos de luz", Posicion.HORIZONTAL, Orientacion.ABAJO, 200, 0, "LUZ"),
    CartaMagica("Viento Cortante", "Aumenta el ataque de los monstruos de viento", Posicion.HORIZONTAL, Orientacion.ABAJO, 250, 0, "VIENTO"),
    CartaMagica("Escudo del Guerrero", "Aumenta la defensa de los guerreros", Posicion.HORIZONTAL, Orientacion.ABAJO, 0, 200, "Guerrero"),
    CartaMagica("Destello Luminiscente", "Aumenta la defensa de monstruos de luz", Posicion.HORIZONTAL, Orientacion.ABAJO, 0, 300, "LUZ"),

    # Cartas Trampa (15 cartas)
    CartaTrampa("Tornado de Polvo", "Detiene el ataque de monstruos con atributo VIENTO", Posicion.HORIZONTAL, Orientacion.ABAJO, "VIENTO"),
    CartaTrampa("Barrera de Fuego", "Detiene el ataque de monstruos con atributo FUEGO", Posicion.HORIZONTAL, Orientacion.ABAJO, "FUEGO"),
    CartaTrampa("Escudo del Agua", "Detiene el ataque de monstruos con atributo AGUA", Posicion.HORIZONTAL, Orientacion.ABAJO, "AGUA"),
    CartaTrampa("Escudo de Tierra", "Detiene el ataque de monstruos con atributo TIERRA", Posicion.HORIZONTAL, Orientacion.ABAJO, "TIERRA"),
    CartaTrampa("Oscuridad Eterna", "Detiene el ataque de monstruos con atributo OSCURIDAD", Posicion.HORIZONTAL, Orientacion.ABAJO, "OSCURIDAD"),
    CartaTrampa("Luz Radiante", "Detiene el ataque de monstruos con atributo LUZ", Posicion.HORIZONTAL, Orientacion.ABAJO, "LUZ"),
    CartaTrampa("Ataque de Viento", "Detiene el ataque de monstruos con atributo VIENTO", Posicion.HORIZONTAL, Orientacion.ABAJO, "VIENTO"),
    CartaTrampa("Barrera Sagrada", "Detiene el ataque de monstruos con atributo TIERRA", Posicion.HORIZONTAL, Orientacion.ABAJO, "TIERRA"),
    CartaTrampa("Llamas Infinitas", "Detiene el ataque de monstruos con atributo FUEGO", Posicion.HORIZONTAL, Orientacion.ABAJO, "FUEGO"),
    CartaTrampa("Reflejo Oscuro", "Detiene el ataque de monstruos con atributo OSCURIDAD", Posicion.HORIZONTAL, Orientacion.ABAJO, "OSCURIDAD"),
    CartaTrampa("Barrera de Hielo", "Detiene el ataque de monstruos con atributo AGUA", Posicion.HORIZONTAL, Orientacion.ABAJO, "AGUA"),
    CartaTrampa("Manto de Fuego", "Detiene el ataque de monstruos con atributo FUEGO", Posicion.HORIZONTAL, Orientacion.ABAJO, "FUEGO"),
    CartaTrampa("Sombra Oscura", "Detiene el ataque de monstruos con atributo OSCURIDAD", Posicion.HORIZONTAL, Orientacion.ABAJO, "OSCURIDAD"),
    CartaTrampa("Viento Cortante", "Detiene el ataque de monstruos con atributo VIENTO", Posicion.HORIZONTAL, Orientacion.ABAJO, "VIENTO"),
    CartaTrampa("Reflejo de Luz", "Detiene el ataque de monstruos con atributo LUZ", Posicion.HORIZONTAL, Orientacion.ABAJO, "LUZ")
]