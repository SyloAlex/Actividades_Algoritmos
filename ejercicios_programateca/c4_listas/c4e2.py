#Ejercicio C4E2
class NumberLoop():
    def __init__(self):
        self.num_loop = 0
    
    def get_input(self):
        check = False
        while check is False:
            number = input("Escribe el ultimo numero de la lista aqui: ")
            try:
                num_loop = int(number)
                if num_loop < 0:
                    print("No se aceptan numeros negatuvos")
                    continue
                if num_loop >= 0 and num_loop < 5:
                    print("Numeros menores a 5 no son divisibles entre 5")
                    continue
                self.num_loop = num_loop
                check = True
            except ValueError:
                print("Eso no es un numero.")

    def get_multiples_5(self):
        self.get_input()
        for num in range(5, self.num_loop + 1, 5):
            print(num)

loop_numbers = NumberLoop().get_multiples_5()