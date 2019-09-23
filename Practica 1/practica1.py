### GESTIÓN DE SISTEMAS DE INFORMACIÓN  ###
### Práctica 1 - Adivinar un número     ###
### Autor - Daniel Callado Martínez     ###
### Fecha - 27/09/2019                  ###

import random

### Clase Partida ###
class Partida:

    ganador = None
    perdedor = None
    num_intentos = None

    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def Jugar(self):
        print("Comenzamos el juego!!!")
        print("______________________\n")

        self.num_intentos = 0
        self.numero = random.randint(1,100) 

        while True:
            self.num_intentos += 1

            player1.Pensar()
            if self.Comprobar(player1.numero_propuesto):
                self.ganador = player1
                self.perdedor = player2
                player1.partidas_ganadas += 1
                break

            player2.Pensar()
            if self.Comprobar(player2.numero_propuesto):
                self.ganador = player2
                self.perdedor = player1
                player2.partidas_ganadas += 1
                break

        print("\nGanador {} !!! sólo has necesitado {} intentos.".format(self.ganador.nombre, self.num_intentos))
        print("{} llevas {} partidas ganadas contra las {} de {}. \n".format(self.ganador.nombre,self.ganador.partidas_ganadas,self.perdedor.partidas_ganadas,self.perdedor.nombre))
        self.Jugar()

    def Comprobar(self, num):
        if num > self.numero:
            print("Menor...")
            return False
        elif num < self.numero:
            print("Mayor...")
            return False
        else:
            print("Lo has adivinado!!!")
            return True

### Clase Jugador ###
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidas_ganadas = 0

    def Pensar(self):
        self.numero_propuesto = int(input("{} elige un numero entre 1 y 100: ".format(self.nombre)))

    def Saludar(self):
        print("Hola me llamo {}.".format(self.nombre))

### Main ###
if __name__ == "__main__":

    print("Bienvenidos al juego de adivinar un numero del 1 al 100 (2 Jugadores)!!!\n")

    player1 = Jugador(input("¿Cómo te llamas jugador 1?: "))
    player1.Saludar()
    print("")

    player2 = Jugador(input("¿Cómo te llamas jugador 2?: "))
    player2.Saludar()
    print("")

    partida = Partida(player1, player2)
    partida.Jugar()

