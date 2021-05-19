# Ejercicio 3.5: Realice un algoritmo que, dado un número ingresado 
# por el usuario, determine si este es:
# Primo.
# Compuesto.
# Oblongo.
# Palíndromo.
# Perfecto.
# Abundante
# Deficiente.
# Cuadrado.
# Libre de cuadrados.

class Calculator:
    '''
        Calculadora que permite saber si un numero es primo, compuesto,
        oblongo, palindromo, perfecto, abundante, deficiente, cuadrado,
        o libre de cuadrados
    '''
    def __init__(self):
        self.number = 0
    
    def get_number(self):
        '''
            El usuario ingresa el numero al que le desea calcular la opcion
        '''
        valid = False
        while valid is False:
            try:
                self.number = int(input("Ingrese el numero:\n>> "))
                valid = True
            except ValueError:
                print("Por favor ingrese un numero, no letras o caracteres especiales")
    
    def get_option(self):
        '''
            El usuario ingresa el numero de las opciones posibles
        '''
        valid = True
        while valid is True:
            try:
                print("Puedo saber si el numero es:\n1. Primo\n2. Compuesto\n3. Oblongo\n4. Palindromo\n5. Perfecto\n6. Abundante\n7. Deficiente\n8. Cuadrado\n9. Libre de cuadrados\n10. Salir")
                option = int(input("Ingresa una opcion:\n>>> "))
                if option >= 1 and option <= 10:
                    valid = False
                else:
                    print("La opcion seleccionada no es valida")
            except ValueError:
                print("Ingrse una opcion en numeros")
        
        return option

    def check_prime(self):
        '''
            Revisa si el numero ingresado es un numero primo
        '''
        flag = True
        if self.number != 0:
            for number in range(2, (self.number // 2) + 1):
                if self.number % number == 0:
                    flag = False
                    break
            if flag == True:
                print("El numero {} es un numero primo".format(self.number))
            else:
                print("El numero {} no es un numero primo".format(self.number))
        else:
            print("El cero no es un numero primo!!")
    
    def check_compound_number(self):
        '''
            Revisa si el numero ingresado es un numero compuesto
        '''
        flag = True
        if self.number != 0:
            for number in range(2, (self.number // 2) + 1):
                if self.number % number == 0:
                    flag = False
                    break
            if flag == True:
                print("El numero {} no es un numero compuesto".format(self.number))
            else:
                print("El numero {} es un numero compuesto".format(self.number))
        else:
            print("El cero no es un numero compuesto!!")

    def check_pronic(self):
        '''
            Revisa si el numero ingresado es un numero oblongo
        '''
        flag = False
        for number in range(0, (self.number // 2) + 1):
            if (number*(number+1)) == self.number:
                flag = True
                break
        if flag:
            print("El numero {} es oblongo. Sus multiplicantes son {} y {}".format(self.number, number, number + 1))
        else:
            print("El numero {} no es oblongo".format(self.number))

    def check_palindrome(self):
        '''
            Revisa si el numero ingresado es un palindromo
        '''
        palindrome = str(self.number)
        if palindrome == palindrome[::-1]:
            print("El numero {} es palindromo!".format(self.number))
        else:
            print("El numero {} no es palindromo".format(self.number))

    def check_perfect_number(self):
        '''
            Revisa si el numero ingresado es perfecto
        '''
        perfect_number = 0
        for number in range(1, (self.number // 2) + 1):
            if self.number % number == 0:
                perfect_number += number
        if perfect_number == self.number:
            print("El numero {} es perfecto!".format(self.number))
        else:
            print("El numero {} no es perfecto".format(self.number))
    
    def check_abundant_number(self):
        '''
            Revisa si el numero ingresado es perfecto
        '''
        abundant_number = 0
        for number in range(1, (self.number // 2) + 1):
            if self.number % number == 0:
                abundant_number += number
        if abundant_number > self.number:
            print("El numero {} es abundante!".format(self.number))
        else:
            print("El numero {} no es abundante".format(self.number))

    def check_deficient_number(self):
        '''
            Revisa si el numero ingresado es perfecto
        '''
        deficient_number = 0
        for number in range(1, (self.number // 2) + 1):
            if self.number % number == 0:
                deficient_number += number
        if deficient_number < self.number:
            print("El numero {} es deficiente!".format(self.number))
        else:
            print("El numero {} no es deficiente".format(self.number))

    def check_square(self):
        flag = True
        for number in range(1, (self.number // 2) + 1):
            if number ** 2 == self.number:
                flag = False
        if flag:
            print("El numero {} no es cuadrado".format(self.number))
        else:
            print("El numero {} es cuadrado!".format(self.number))

    def check_squares_free(self):
        free_square = 1
        for number in range(1, (self.number // 2) + 1):
            if self.number % number == 0:
                flag = True
                for prime_checker in range(2, (number // 2) + 1):
                    if number % prime_checker == 0:
                        flag = False
                        break
                if flag == True:
                    free_square *= number
        print(free_square)
        if free_square == self.number:
            print("El numero {} esta libre de cuadrados!".format(self.number))
        else:
            print("El numero {} no esta libre de cuadrados".format(self.number))

    def execute(self):
        '''
            Ejecuta el programa de calculo de numeros extraños
        '''
        print("Bienvenido a tu calculadora de numeros extraños personal!")
        continue_process = True
        while continue_process is True:
            option = self.get_option()
            if option == 10:
                print("Entendido, cerrando el programa")
                exit()
            self.get_number()
            if option == 1:
                self.check_prime()
            elif option == 2:
                self.check_compound_number()
            elif option == 3:
                self.check_pronic()
            elif option == 4:
                self.check_palindrome()
            elif option == 5:
                self.check_perfect_number()
            elif option == 6:
                self.check_abundant_number()
            elif option == 7:
                self.check_deficient_number()
            elif option == 8:
                self.check_square()
            else:
                self.check_squares_free()
            continue_option = input("-"*40 + "\nDesea continuar? (si o no)\n>> ").lower()
            print("-"*40)
            if continue_option == "si":
                continue
            elif continue_option == "no":
                print("Entendido, cerrando el programa")
                continue_process = False
            else:
                print("La opcion ingresada no es valida, se retornara al menu de pantalla")

Calculator().execute()