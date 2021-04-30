#Ejercicio 2.2. Calculo de Areas
#Solicitar al usuario el tipo de figura (circunferencia, elipse, cuadrado, rectangulo,
#triangulos y rombos) y calcular el area.

class GeometricFigure:
    '''
        Clase de Figuras Geometricas. Obtiene la data del usuario en
        inputs en las funciones
    '''
    def __init__(self):
        self.figure = 0
        self.height = 0
        self.width = 0
        self.radius = 0
        self.area = 0
        self.pi = 3.1415

    def get_figure(self):
        '''
            Recibe, como input, la opcion segun la figura que el usuario quiera
            calcular el area
        '''
        valid = False
        while not valid:
            print("1 (circunferencia)\n2 (elipse)\n3 (cuadrado)\n4 (rectangulo)\n5 (triangulo)\n6 (rombo)")
            inp = input("Ingresa la opcion segun el tipo de figura a la que desees calcular el area: ")
            try:
                inp = int(inp)
                if inp >= 1 and inp <= 6:
                    self.figure = inp
                    valid = True
                else:
                    print("Esa no es una opcion valida")
            except ValueError:
                print("Esa opcion no es un numero")

    def get_values(self):
        '''
            Recibe, como input, la altura, ancho y radio, segun el caso, de la 
            figura seleccionada
        '''
        self.get_figure()
        if self.figure == 1:
            valid = False
            while not valid:
                try:
                    inp_radius = input("Ingresa el radio de la figura: ")
                    self.radius = float(inp_radius)
                    valid = True
                except ValueError:
                    print("No ingresaste el valor como un numero")
        if self.figure >= 2 and self.figure <= 6:
            valid = False
            while not valid:
                try:
                    inp_height = input("Ingresa la altura de la figura: ")
                    self.height = float(inp_height)
                    inp_width = input("Ingresa el ancho de la figura: ")
                    self.width = float(inp_width)
                    valid = True
                except ValueError:
                    print("No ingresaste el valor como un numero")
    
    def get_area(self):
        '''
            Calcula el area con la data suministrada por el
            usuario.
        '''
        self.get_values()
        if self.figure == 1:
            self.area = (self.pi)*(self.radius**2)
            print("El area de la circunferencia es:", self.area)
        elif self.figure == 2:
            self.area = self.pi*self.height*self.width
            print("El area de la elipse es:", self.area)
        elif self.figure == 3 or self.figure == 4:
            self.area = self.height*self.width
            print("El area del cuadrilatero es:", self.area)
        elif self.figure == 5:
            self.area = (self.height*self.width)/2
            print("El area del triangulo es:", self.area)
        else:
            self.area = (self.height*self.width)/2
            print("El area del rombo es:", self.area)

figure = GeometricFigure().get_area()