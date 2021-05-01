#Ejercicio 2.2: Diseña un programa que determine si un número o palabra ingresados por teclado, son palíndromos o no.

class Word:

    def __init__(self):
        self.word = ''

    def get_input(self):
        valid = False
        while valid is False:
            try:
                word = input("Escribe una palabra o secuencia de numeros: ")
                letter_check = word.isalpha()
                number_check = word.isnumeric()
                if letter_check is True or number_check is True:
                    self.word = word
                    valid = True
            except ValueError:
                print("Por favor, ingresa una palabra en letras o un numero")
    
    def check_palindrome(self):
        self.get_input()
        palindrome = self.word[::-1]
        if self.word.lower() == palindrome.lower():
            print("El palindromo de", self.word.lower(), "es", palindrome.lower())
        else:
            print(self.word, "no es un palindromo.")

prueba = Word().check_palindrome()