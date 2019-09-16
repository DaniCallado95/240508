class Jugador:
    def __init__(self, nombre, tipo, numero_propuesto, numero_preguntado):
        self.nombre = nombre
        self.tipo = tipo
        self.numero_propuesto = numero_propuesto
        self.numero_preguntado = numero_preguntado

    def Pensar(self):
        self.numero_propuesto = int(input("Elige un numero entre 0 y 100: "))

    def Preguntar(self):
        self.numero_preguntado = int(input("Pregunta un numero entre 0 y 100: "))

    def Comprobar(self, num):
        if num > self.numero_propuesto:
            print("Menor...")
            return True
        elif num < self.numero_propuesto:
            print("Mayor...")
            return True
        else:
            print("Lo has adivinado!")
            return False

    def Saludar(self):
        print("Hola me llamo {}.".format(self.nombre))

class Partida:
    def __init__(self, jugador1, jugador2, num_intentos):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.num_intentos = num_intentos

    def jugar(self):
        player1.Pensar()
        while True:
            player2.Preguntar()
            self.num_intentos += 1
            if not player1.Comprobar(player2.numero_preguntado):
                break

        print("sólo has necesitado {} intentos".format(self.num_intentos))

if __name__ == "__main__":

    print("Bienvenidos al juego!")

    player1 = Jugador("Dani",1,0,0)
    player2 = Jugador("Kike",2,0,0)
    player1.Saludar()
    player2.Saludar()
    partida = Partida(player1, player2, 0)
    partida.jugar()

