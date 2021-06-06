# Realice un algoritmo que simule un juego de dados entre 2 jugadores, la idea de este
# juego obtener más puntos que el oponente, los mismos tendrán 7 turnos cada uno.
# 1 = +10pts
# 2 = +20pts
# 3 = vuelve a lanzar
# 4 = puntuacion x 2
# 5 = +40 pts
# 6 = Puntuacion /2

from Player import Player

class DiceGame:
    def __init__(self):
        self.turn = 1

    def get_names(self):
        '''
            Los jugadores ingresan sus nombres en la consola y se almacenan en self.player1 
            y self.player2
        '''
        valid = False
        while not valid:
            player1_name = input("Por favor, ingrese el nomber del primer jugador: ")
            if player1_name.isalpha():
                player1 = Player(player1_name)
                valid = True
            else:
                print("Por favor solo ingrese su primer nombre sin caracteres especiales")
        while valid:
            player2_name = input("Por favor, ingrese el nomber del segundo jugador: ")
            if player2_name.isalpha():
                player2 = Player(player2_name)
                valid = False
            else:
                print("Por favor solo ingrese su primer nombre sin caracteres especiales")
        
        return player1, player2

    def throw_dice(self, player1, player2):
        '''
            Los jugadores lanzan un dado e ingresan el resultado
            en la consola
        '''
        valid = False
        while not valid:
            try:
                dice1 = int(input("{} por favor ingresa el numero al lanzar un dado\n>>".format(player1.name)))
                if dice1 >= 1 and dice1 <= 6:
                    valid = True
                else:
                    print("Un dado solo puede dar resultados entre 1 y 6!")
            except ValueError:
                print("Escribe el resultado del dado en numeros")
        while valid:
            try:
                dice2 = int(input("{} por favor ingresa el numero al lanzar un dado\n>>".format(player2.name)))
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

    def update_scores(self, player1, player2, dice1, dice2):
        '''
            Actualiza los resultados de cada jugador dependiendo
            del resultado ingresado al lanzar los dados
        '''
        dice = [dice1, dice2]
        for index in range(len(dice)):
            if index == 0:
                player = player1
            else:
                player = player2
            if dice[index] == 1:
                player.score += 10
            elif dice[index] == 2:
                player.score += 20
            elif dice[index] == 3:
                valid = False
                while not valid:
                    print(f"{player.name}!")
                    second_dice = self.second_throw()
                    if second_dice != 3:
                        if second_dice == 1:
                            player.score += 10
                        elif second_dice == 2:
                            player.score += 20
                        elif second_dice == 4:
                            player.score *= 2
                        elif second_dice == 5:
                            player.score += 40
                        elif second_dice == 6:
                            player.score /= 2
                        valid = True
            elif dice[index] == 4:
                player.score *= 2
            elif dice[index] == 5:
                player.score += 40
            else:
                player.score /= 2
            if index == 0:
                player1.score = player.score
            else:
                player2.score = player.score

    def execute(self):
        '''
            Ejecuta el juego Dice!
        '''
        print("Bienvenidos al juego de Dados: Dice!")
        player1, player2 = self.get_names()
        print(f"Los jugadores son: {player1.name} y {player2.name}")
        while self.turn < 8:
            print(f"Turno #{self.turn}:")
            throw1, throw2 = self.throw_dice(player1, player2)
            self.update_scores(player1, player2, throw1, throw2)
            print(f"{player1.name}: {player1.score}. {player2.name}: {player2.score}")
            self.turn += 1
        print("Partida Finalizada!")
        if player1.score > player2.score:
            winner = player1
        elif player1.score < player2.score:
            winner = player2
        else:
            winner = 0
        if winner == 0:
            print(f"Hubo un empate entre los jugadores {player1.name} y {player2.name}!")
        else:
            print(f"El ganador es: {winner.name}!!!")

DiceGame().execute()