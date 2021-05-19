# Realice un algoritmo que simule un juego de dados entre 2 jugadores, la idea de este
# juego obtener más puntos que el oponente, los mismos tendrán 7 turnos cada uno.
# 1 = +10pts
# 2 = +20pts
# 3 = vuelve a lanzar
# 4 = puntuacion x 2
# 5 = +40 pts
# 6 = Puntuacion /2

class Dice_Game:
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.player1score = 0
        self.player2score = 0
        self.turn = 1

    def get_names(self):
        '''
            Los jugadores ingresan sus nombres en la consola y se almacenan en self.player1 
            y self.player2
        '''
        valid = False
        while not valid:
            player1 = input("Por favor, ingrese el nomber del primer jugador: ")
            if player1.isalpha():
                self.player1 = player1
                valid = True
            else:
                print("Por favor solo ingrese su primer nombre sin caracteres especiales")
        while valid:
            player2 = input("Por favor, ingrese el nomber del segundo jugador: ")
            if player2.isalpha():
                self.player2 = player2
                valid = False
            else:
                print("Por favor solo ingrese su primer nombre sin caracteres especiales")

    def throw_dice(self):
        '''
            Los jugadores lanzan un dado e ingresan el resultado
            en la consola
        '''
        valid = False
        while not valid:
            try:
                dice1 = int(input("{} por favor ingresa el numero al lanzar un dado\n>>".format(self.player1)))
                if dice1 >= 1 and dice1 <= 6:
                    valid = True
                else:
                    print("Un dado solo puede dar resultados entre 1 y 6!")
            except ValueError:
                print("Escribe el resultado del dado en numeros")
        while valid:
            try:
                dice2 = int(input("{} por favor ingresa el numero al lanzar un dado\n>>".format(self.player2)))
                if dice2 >= 1 and dice2 <= 6:
                    valid = False
                else:
                    print("Un dado solo puede dar resultados entre 1 y 6!")
            except ValueError:
                print("Escribe el resultado del dado en numeros")

        return dice1, dice2

    def second_throw(self):
        '''
            Si el primer resultado fue 3, vuelve a lanzar el dado
            en el mismo turno
        '''
        print("Vuelves a lanzar el dado!")
        valid = False
        while not valid:
            try:
                dice = int(input("Ingresa el resultado:\n>> "))
                if dice >= 1 and dice <= 6:
                    valid = True
                else:
                    print("Un dado solo puede dar resultados entre 1 y 6!")
            except ValueError:
                print("Escribe el resultado del dado en numeros")
        
        return dice

    def update_scores(self, dice1, dice2):
        '''
            Actualiza los resultados de cada jugador dependiendo
            del resultado ingresado al lanzar los dados
        '''
        dice = [dice1, dice2]
        for index in range(len(dice)):
            if index == 0:
                player = self.player1score
            else:
                player = self.player2score
            if dice[index] == 1:
                player += 10
            elif dice[index] == 2:
                player += 20
            elif dice[index] == 3:
                valid = False
                while not valid:
                    print(f"{self.player1}!")
                    second_dice = self.second_throw()
                    if second_dice != 3:
                        if second_dice == 1:
                            player += 10
                        elif second_dice == 2:
                            player += 20
                        elif second_dice == 4:
                            player *= 2
                        elif second_dice == 5:
                            player += 40
                        elif second_dice == 6:
                            player /= 2
                        valid = True
            elif dice[index] == 4:
                player *= 2
            elif dice[index] == 5:
                player += 40
            else:
                player /= 2
            if index == 0:
                self.player1score = player
            else:
                self.player2score = player

    def execute(self):
        '''
            Ejecuta el juego Dice!
        '''
        print("Bienvenidos al juego de Dados: Dice!")
        self.get_names()
        print(f"Los jugadores son: {self.player1} y {self.player2}")
        while self.turn < 8:
            print(f"Turno #{self.turn}:")
            throw1, throw2 = self.throw_dice()
            self.update_scores(throw1, throw2)
            self.turn += 1
        print("Partida Finalizada!")
        if self.player1score > self.player2score:
            winner = self.player1
        elif self.player1score < self.player2score:
            winner = self.player2
        else:
            winner = 0
        if winner == 0:
            print(f"Hubo un empate entre los jugadores {self.player1} y {self.player2}!")
        else:
            print(f"El ganador es: {winner}!!!")

Dice_Game().execute()