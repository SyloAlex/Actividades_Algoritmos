doctors = ['Angela Johnson', 'David Kane', 'Marcus Stewart', 'Jessica Cruz']

class Vetenrinary:
    def __init__(self):
        self.doctors = ['Angela Johnson', 'David Kane', 'Marcus Stewart', 'Jessica Cruz']
        self.database = {}
    
    def get_doctor(self):
        '''
            Permite al usuario seleccionar el doctor que desea que lo atienda
        '''
        print("Esta es la lista de doctores disponibles:")
        for index, doctor in enumerate(self.doctors):
            print("{}.- {}".format(index + 1, doctor))
        valid = False
        while not valid:
            try:
                option = int(input("Ingrese la opcion del doctor que desea que lo atienda\n>> "))
                if option >= 1 and option <= 4:
                    valid = True
                else:
                    print("La opcion ingresada no es valida")
            except ValueError:
                print("Ingrese una opcion numerica")

        return self.doctors[option - 1]

    def get_mascot_info(self):
        '''
            El usuario ingresa todos los datos referentes a la mascota
            y su dueño. Mascotaa: Nombre, edad, raza, tipo. Dueño: Nombre, 
            edad, cedula, telefono.
        '''
        valid = False
        while not valid:
            mascot_name = input("Ingrese el nombre de su mascota\n>> ")
            if mascot_name.isalpha():
                valid = True
            else:
                print("Escriba el nombre de su mascota sin caracteres especiales")
        valid = False
        while not valid:
            try:
                mascot_age = int(input("Ingrese la edad de su mascota\n>> "))
                valid = True
            except ValueError:
                print("Ingrese la edad en numeros")
        valid = False
        while not valid:
            mascot_type = input("Ingrese el tipo de mascota\n>> ")
            if mascot_type.isalpha():
                valid = True
            else:
                print("Escriba el tipo de mascota sin caracteres especiales o numeros")
        valid = False
        while not valid:
            mascot_race = input("Ingrese la raza de su mascota\n>> ")
            if mascot_race.isalpha():
                valid = True
            else:
                print("Escriba la raza de su mascota sin caracteres especiales o numeros")
        valid = False
        while not valid:
            mascot_owner = input("Ingrese el nombre del dueño\n>> ")
            if mascot_owner.isalpha():
                valid = True
            else:
                print("Escriba el nombre del dueño sin caracteres especiales o numeros")
        valid = False
        while not valid:
            try:
                owner_age = int(input("Ingrese la edad del dueño\n>> "))
                valid = True
            except ValueError:
                print("Ingrese la edad en numeros")
        valid = False
        while not valid:
            try:
                dni_owner = int(input("Ingrese la cedula del dueño\n>> "))
                valid = True
            except ValueError:
                print("Ingrese la cedula en numeros")
        valid = False
        while not valid:
            try:
                owner_phone = int(input("Ingrese el telefono del dueño sin caracteres especiales\n>> "))
                valid = True
            except ValueError:
                print("Ingrese el telefono del dueño en numeros sin caracteres especiales")
        self.database[len(self.database) + 1] = {"Nombre mascota": mascot_name, "Edad Mascota": mascot_age,
                                                "Tipo de Mascota": mascot_type, "Raza de la Mascota": mascot_race,
                                                "Nombre del Dueño": mascot_owner, "Edad del Dueño": owner_age,
                                                "Cedula del Dueño": dni_owner, "Telefono del Dueño": owner_phone}

    def get_services(self):
        '''
            El usuario ingresa la opcion segun el servicio que desea
            adquirir
        '''
        print("Los servicios disponibles son:\n1. Consulta (20$)\n2. Operacion (80$)\n3. Peluqueria (30$)")
        mascot_service = []
        valid = False
        while not valid:
            try:
                service = int(input("Ingrese el servicio que desea adquirir\n>> "))
                if service >= 1 and service <= 3:
                    if service == 1:
                        mascot_service.append(("Consulta", 20))
                    elif service == 2:
                        mascot_service.append(("Operacion", 80))
                    else:
                        mascot_service.append(("Peluqueria", 30))
                    option = input("Desea anexar otro servicio?\n>> ").lower()
                    option_valid = True
                    while option_valid:
                        if option == "si":
                            option_valid = False
                            continue
                        elif option == "no":
                            option_valid = False
                            valid = True
                        else:
                            print("La opcion ingresada no es valida")
                else:
                    print("La opcion ingresada no es valida")
            except ValueError:
                print("Ingrese la opcion numerica")

        return mascot_service
    
    def print_receipt(self, doctor, services):
        '''
            Imprime la factura con los datos de mascota/dueño, doctor tratante,
            y servicio cobrado
        '''
        print("-"*30 + "\nFactura:\n")
        for key, value in self.database.items():
            if key == len(self.database):
                for info, mascot_data in value.items():
                    print(f">>{info}: {mascot_data}")
            print("-"*30)
        print(f"Sera atendido por el/la Dr(a). {doctor}")
        for service in services:
            print(f"Adquirio el servicio de {service[0]} por {service[1]}$")
        print("-"*30)
    
    def print_database(self):
        '''
            Imprime la base de datos completa. Todos los clientes que fueron atendidos
            en el dia
        '''
        print("-"*30 + "\nBase de Datos:\n")
        for key, value in self.database.items():
            print(f"ID: {key}")
            for info, mascot_data in value.items():
                print(f">>{info}: {mascot_data}")
            print("-"*30)

    def execute(self):
        '''
            Ejecuta las funciones para almacenar en base de datos los datos de la mascota/dueño,
            el doctor tratante y el servicio. A su vez, imprime la factura y permite visualizar la base
            de datos
        '''
        print("Bienvenido a la Veterinaria: Trino y Salem!")
        continue_process = False
        while not continue_process:
            doctor = self.get_doctor()
            self.get_mascot_info()
            service = self.get_services()
            self.print_receipt(doctor, service)
            option = input("Desea registrar a alguien mas?\n>> ")
            option_valid = False
            while not option_valid:
                if option == "si":
                    option_valid = True
                    continue
                elif option == "no":
                    option_valid = True
                    option_db = input("Desea ver la base de datos?\n>> ")
                    option_valid_db = False
                    while not option_valid_db:
                        if option_db == "si":
                            option_valid_db = True
                            self.print_database()
                            continue
                        elif option_db == "no":
                            option_valid_db = True
                        else:
                            print("La opcion ingresada no es valida!")
                    continue_process = True
                    print("Entendido, se cerrara el programa")
                else:
                    print("La opcion ingresada no es valida!")
            
Vetenrinary().execute()