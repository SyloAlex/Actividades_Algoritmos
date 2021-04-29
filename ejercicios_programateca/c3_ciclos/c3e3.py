class PointsCollector:
    '''
    Recibe la puntuacion ingresada en la terminal y verifica la factibilidad
    de lo escrito.
    '''
    def __init__(self):
        self.points = 0

    def get_input(self):
        checker = False
        while checker is False:
            try:
                inp = input("Ingrese su puntuacion: ")
                points = int(inp)
                if points < 0:
                    print("No puedes tener una puntuacion negativa.")
                    continue
                if points == 0:
                    print("La puntuacion minima obtenible es de 1 punto")
                if points > 200:
                    print("El maximo puntaje obtenible es de 200")
                    continue
                self.points = points
                checker = True
            except ValueError:
                print("Las letras no son numeros :/ Por favor escriba su puntuacion en numeros")
                continue

    def check_points(self):
        '''
            Verifica el puntaje obtenido y lo coteja con la tabla de premios para imprimir un mensaje
            con su puntuacion y, en caso de haber ganado algo, el premio obtenido.
        '''
        self.get_input()
        if self.points >= 1 and self.points <= 50:
            print(f"No hay premios para {self.points} pts")
        if self.points >= 51 and self.points <= 150:
            price = "Bronce"
            print(f"Felicitaciones, Ganaste la medalla de {price} por haber tenido {self.points} pts!")
        if self.points >= 151 and self.points <= 180:
            price = "Plata"
            print(f"Felicitaciones, Ganaste la medalla de {price} por haber tenido {self.points} pts!")
        if self.points >= 181 and self.points <= 200:
            price = "Oro"
            print(f"Felicitaciones, Ganaste la medalla de {price} por haber tenido {self.points} pts!")

score = PointsCollector()
score.check_points()