# Ejercicio Base de Datos

class Sirius:
    '''
        Base de datos de estudiantes de la UNIMET
    '''
    def __init__(self):
        self.database = {}
    
    def get_options(self):
        '''
            El usuario ingresa la opcion de lo que desea hacer en la base de datos
        '''
        valid = False
        print("Estas son sus opciones:\n1. Agregar un usuario\n2. Eliminar un usuario\n3. Actualizar datos\n4. Ver la Base de datos")
        while valid is False:
            try:
                option = int(input("Que desea hacer?: "))
                if option < 1 or option > 4:
                    print("La opcion ingresada no es valida")
                else:
                    valid = True
            except ValueError:
                print("Debe ingresar un numero de las opciones indicadas")
        return option
    
    def add_user(self):
        '''
            Agrega un usuario a base de datos. Requiere que el usuario ingrese cedula,
            nombre y carnet.
        '''
        student = input("Ingrese el nombre del estudiante: ")
        valid = False
        while valid is False:
            try:
                id = int(input("Ingrese la cedula del estudiante: "))
                student_id = int(input("Ingrese el carnet del estudiante: "))
                valid = True
            except ValueError:
                print("Por favor ingrese los datos en numeros")
        self.database[student_id] = {"Nombre": student, "Cedula": id}
    
    def delete_student(self):
        valid = False
        while valid is False:
            try:
                student = int(input("Ingrese el carnet del estudiante que desea eliminar: "))
                valid = True
            except ValueError:
                print("Debe ingresar el numero de carnet del estudiante")
        if student in self.database:
            self.database.pop(student)
            print("Se ha eliminado exitosamente")
        else:
            print("El estudiante NO esta en la base de datos")

    def update_database(self):
        valid = False
        while valid is False:
            try:
                student = int(input("Ingrese el carnet del estudiante que desea actualizar: "))
                valid = True
            except ValueError:
                print("Debe ingresar el numero de carnet del estudiante")
        if student in self.database:
            valid = False
            while valid is False:
                try:
                    update_option = int(input("Desea actualizar el nombre (1), la cedula (2) o el carnet (3): "))
                    if update_option > 0 and update_option < 4:
                        valid = True
                    else:
                        print("La opcion seleccionada no es valida")
                except ValueError:
                    print("Debe ingresar el numero de carnet del estudiante")
            if update_option == 1:
                self.database[student]["Nombre"] = input("Ingrese el nuevo nombre del estudiante: ")
            elif update_option == 2:
                valid = False
                while valid is False:
                    self.database[student]["Cedula"] = int(input("Ingrese la nueva cedula del estudiante: "))
                    valid = True
            else:
                valid = False
                while valid is False:
                    new_student_id = int(input("Ingrese el nuevo carnet del estudiante: "))
                    valid = True
                self.database[new_student_id] = self.database.pop(student)
        else:
            print("El estudiante NO esta en la base de datos")

    def print_database(self):
        '''
            Imprime los estudiantes y sus datos de la base de datos
        '''
        if self.database == {}:
            print("No hay estudiantes en la base de datos!!!!")
        else:
            print("\nLista de estudiantes:\n---------------------")
            for id, student_info in self.database.items():
                print("Nombre: {} Carnet: {} Cedula: {}".format(student_info["Nombre"], id, student_info["Cedula"]))

    def execute(self):
        print("Bienvenido a la base de datos de Sirius")
        valid_option = False
        while valid_option is False:
            option = self.get_options()
            if option == 1:
                self.add_user()
            elif option == 2:
                self.delete_student()
            elif option == 3:
                self.update_database()
            elif option == 4:
                self.print_database()
            option_continue = input("Desea hacer algo mas? (Si o No): ").lower()
            if option_continue == "no":
                print("Entendido, que tenga un feliz dia!")
                valid_option = True

Sirius().execute()