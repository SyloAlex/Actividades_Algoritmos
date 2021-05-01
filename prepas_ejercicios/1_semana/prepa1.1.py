#Ejercicio 1: Debes realizar un programa que ejecute las operaciones que se llevan a cabo en una cuenta bancaria.
from datetime import datetime

class BankAccount:
    def __init__(self):
        self.balance = 3480
        self.date = datetime.today().date()
        self.movements = []
    
    def get_input(self):
        print("Estas son sus opciones\n1.Retirar de su cuenta\n2.Depositar en su cuenta\n3.Consultar saldo disponible\n4.Realizar una compra\n5.Revisar movimientos")
        valid = False
        while valid is False:
            try:
                option = input("Por favor, indiquenos la opcion: ")
                option = int(option)
                if option >= 1 and option <= 5:
                    valid = True
                else:
                    print("La opcion seleccionada no es valida")
            except ValueError:
                print("La opcion que seleccionaste no es un numero")
        return option
    
    def withdrawal(self):
        valid = False
        while valid is False:
            try:
                withdrawal_input = input("Cuanto desea retirar de su cuenta?: ")
                withdrawal_input = float(withdrawal_input)
                valid = True
            except ValueError:
                print("Por favor, ingrese el monto que desea retirar en numeros")
        self.balance -= withdrawal_input
        date = str(self.date.day) + "/" + str(self.date.month) + "/" + str(self.date.year)
        new_balance = str(date) + " Ha retirado " + str(withdrawal_input) + "$. Su saldo actual es de " + str(self.balance) + "S."
        self.movements.append(new_balance)
        print(new_balance)

    def deposit(self):
        valid = False
        while valid is False:
            try:
                deposit_input = input("Cuanto desea depositar en su cuenta?: ")
                deposit_input = float(deposit_input)
                valid = True
            except ValueError:
                print("Por favor, ingrese el monto que desea depositar en numeros")
        self.balance += deposit_input
        date = str(self.date.day) + "/" + str(self.date.month) + "/" + str(self.date.year)
        new_balance = str(date) + " Ha depositado " + str(deposit_input) + "$. Su saldo actual es de " + str(self.balance) + "S."
        self.movements.append(new_balance)
        print(new_balance)
    
    def make_a_purchase(self):
        purchase_reason = input("Que va a comprar: ")
        valid = False
        while valid is False:
            try:
                shop_input = input("Cual es el costo?: ")
                shop_input = float(shop_input)
                valid = True
            except ValueError:
                print("Por favor, ingrese el monto de la compra en numeros")
        self.balance -= shop_input
        date = str(self.date.day) + "/" + str(self.date.month) + "/" + str(self.date.year)
        new_balance = str(date) + " Ha realizado una compra de " + str(shop_input) + "$ por la compra de " + str(purchase_reason) + ". Su saldo actual es de " + str(self.balance) + "S."
        self.movements.append(new_balance)
        print(new_balance)

    def check_balance(self):
        print(self.date, "Su saldo actual disponible es de:", self.balance)

    def check_movements(self):
        print("Sus transacciones del dia de hoy son:")
        for movement in self.movements:
            print(movement)

    def make_transaction(self):
        print("Bienvenido al Banco BlahBlahBlah")
        valid = False
        while valid is False:
            option = self.get_input()
            if option == 1:
                self.withdrawal()
            elif option == 2:
                self.deposit()
            elif option == 3:
                self.check_balance()
            elif option == 4:
                self.make_a_purchase()
            else:
                self.check_movements()
            if self.balance < 0:
                print("Su saldo actual es negativo. No puede realizar retiros o compras")
                valid = True
                exit()
            valid_transaction = False
            while valid_transaction is False:
                try:
                    check = input("Desea realizar otra transaccion:\nSi\nNo:\n")
                    if check.isalpha() is True and check == "No":
                        print("Entendido, espero tenga un feliz dia")
                        valid_transaction = True
                        valid = True
                    if check.isalpha() is True and check == "Si":
                        print("Perfecto")
                        valid_transaction = True
                except ValueError:
                    print("La opcion seleccionada no es valida")

prueba = BankAccount()
prueba.make_transaction()