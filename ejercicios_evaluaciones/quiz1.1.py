import random

class Number_Game:
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
            player1 = input("Por favor, ingrese el nombre del primer jugador: ")
            if player1.isalpha():
                self.player1 = player1
                valid = True
            else:
                print("Por favor solo ingrese su primer nombre sin caracteres especiales")
        while valid:
            player2 = input("Por favor, ingrese el nombre del segundo jugador: ")
            if player2.isalpha():
                self.player2 = player2
                valid = False
            else:
                print("Por favor solo ingrese su primer nombre sin caracteres especiales")
        while not valid:
            try:
                player_type = int(input("Cuale jugador sera Camarada? (1 o 2):\n>> "))
                if player_type >= 1 and player_type <= 2:
                    if player_type == 1:
                        player1_type = "Camarada"
                    else:
                        player1_type = "Ondulado"
                    valid = True
                else:
                    print("La opcion ingresada no es valida")
            except ValueError:
                print("Ingrese un numero entre el 1 y 2")
        
        return player1_type


    def partner_wavey_numbers(self, player1):
        '''
            Ejecuta el codigo para generar numeros al azar hasta que alguno de
            los jugadores cumpla con los requisitos de camarada u ondulado.
        '''
        repeat = False
        while not repeat:
            num1 = str(random.randint(100, 1000))
            checker = True
            for index in range(len(num1)):
                if num1[index] != num1[0]:
                    checker = False
                    break
            num2 = str(random.randint(100, 1000))
            checker_2 = True
            for index in range(len(num2)):
                if num2[0] != num2[1]:
                    if index % 2 != 0:
                        if num2[index] != num2[1]:
                            checker_2 = False
                            break
                    else:
                        if num2[index] != num2[0]:
                            checker_2 = False
                            break
                else:
                    checker_2 = False
            if player1 == "Camarada":
                if checker == True and checker_2 == True:
                    self.player1score += int(num1)
                    self.player2score += int(num2)
                    repeat = True
                    print("{}: {} y {}: {}".format(self.player1, num1, self.player2, num2))
            if player1 == "Ondulado":
                if checker == True and checker_2 == True:
                    self.player2score += int(num1)
                    self.player1score += int(num2)
                    repeat = True
                    print("{}: {} y {}: {}".format(self.player1, num2, self.player2, num1))
        print(f"Puntuacion:\n{self.player1}: {self.player1score}\n{self.player2}: {self.player2score}")
            
    def execute(self):
        '''
            Ejecuta el juego Random Number!
        '''
        print("Bienvenidos al juego de Numeros: Random!!!")
        player1 = self.get_names()
        print(f"Los jugadores son: {self.player1} y {self.player2}")
        while self.turn < 4:
            print(f"Turno #{self.turn}:")
            self.partner_wavey_numbers(player1)
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

Number_Game().execute()