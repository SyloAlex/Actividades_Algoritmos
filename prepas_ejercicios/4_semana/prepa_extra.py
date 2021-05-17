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
        print("Estas son sus opciones:\n1. Agregar un usuario\n2. Eliminar un usuario\n3. Actualizar datos\n4. Ver la Base de datos\n5. Salir")
        while valid is False:
            try:
                option = int(input("Que desea hacer?: "))
                if option < 1 or option > 5:
                    print("La opcion ingresada no es valida")
                else:
                    valid = True
            except ValueError:
                print("Debe ingresar un numero de las opciones indicadas")
        return option
    
    def add_student(self):
        '''
            Agrega un estudiante a base de datos. Requiere que el usuario ingrese cedula,
            nombre, carnet, edad y materias cursando.
        '''
        student = input("Ingrese el nombre del estudiante: ")
        valid = False
        while valid is False:
            try:
                age = int(input("Ingrese la edad del estudiante: "))
                id = int(input("Ingrese la cedula del estudiante: "))
                student_id = int(input("Ingrese el carnet del estudiante: "))
                valid = True
            except ValueError:
                print("Por favor ingrese los datos en numeros")
        subject_valid = False
        subjects = []
        while subject_valid is False:
            current_subject = input("Ingrese la materia que esta cursando: ")
            subjects.append(current_subject)
            more_subjects = input("Desea anexar mas materias? (Si o No): ")
            if more_subjects == "no":
                subject_valid = True
            elif more_subjects == "si":
                continue
            else:
                print("La opcion ingresada no es valida")
                break
        if student_id in self.database:
            print("Ya existe un estudiante con este carnet")
        else:
            self.database[student_id] = {"Nombre": student, "Cedula": id, "Edad": age, "Materias": subjects}
    
    def delete_student(self):
        '''
            Eliminar un estudiante de la base de datos
        '''
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
        '''
            Actualizar los datos de un estudiante en la base de datos (nombre, carnet, cedula,
            edad o materias)
        '''
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
                    update_option = int(input("Desea actualizar el nombre (1), cedula (2), edad (3), carnet (4) o materias (5): "))
                    if update_option > 0 and update_option < 6:
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
            elif update_option == 3:
                valid = False
                while valid is False:
                    self.database[student]["Edad"] = int(input("Ingrese la nueva edad del estudiante: "))
                    valid = True
            elif update_option == 4:
                valid = False
                while valid is False:
                    new_student_id = int(input("Ingrese el nuevo carnet del estudiante: "))
                    valid = True
                self.database[new_student_id] = self.database.pop(student)
            else:
                valid = False
                while valid is False:
                    try:
                        option = int(input("Desea agregar una materia (1), eliminar una materia (2) o reescribir las materias cursantes? (3): "))
                        if option > 0 and option < 4:
                            valid = True
                        else:
                            print("La opcion ingresada no es valida")
                    except ValueError:
                        print("Debe ingresar una opcion entre 1, 2 y 3")
                if option == 1:
                    valid = False
                    while valid is False:
                        new_subject = input("Ingrese el nombre de la materia a agregar: ")
                        self.database[student]["Materias"].append(new_subject)
                        option = input("Desea agregar otra materia? (Si o No): ").lower()
                        if option == "si":
                            continue
                        elif option == "no":
                            valid = True
                        else:
                            print("La opcion ingresada no es valida")
                            break
                elif option == 2:
                    delte_subject = input("Ingrese el nombre de la materia a eliminar: ")
                    if delte_subject in self.database[student]["Materias"]:
                        index = self.database[student]["Materias"].index(delte_subject)
                        self.database[student]["Materias"].pop(index)
                        print("La materia se elimino con exito")
                else:
                    new_subjects = []
                    while valid is False:
                        current_subject = input("Ingrese las nuevas materia que esta cursando: ")
                        new_subjects.append(current_subject)
                        more_subjects = input("Desea anexar mas materias? (Si o No): ")
                        if more_subjects == "no":
                            valid = True
                        elif more_subjects == "si":
                            continue
                        else:
                            print("La opcion ingresada no es valida")
                            break
                    self.database[student]["Materias"] = new_subjects
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
            for id in sorted(self.database):
                print("Nombre: {} >>Edad: {} >>Carnet: {} >>Cedula: {}".format(self.database[id]["Nombre"], 
                                                                                 self.database[id]["Edad"], 
                                                                                 id, self.database[id]["Cedula"]))
                print(">>Materias:")
                print(*self.database[id]["Materias"], sep=" / ")
                print("---------------------")

    def execute(self):
        '''
            Ejecuta las funciones add_student(), delete_student(), update_database() y
            print_database() segun las necesidades del usuario.
        '''
        print("Bienvenido a la base de datos de Sirius")
        valid_option = False
        while valid_option is False:
            option = self.get_options()
            if option == 1:
                self.add_student()
            elif option == 2:
                self.delete_student()
            elif option == 3:
                self.update_database()
            elif option == 4:
                self.print_database()
            else:
                exit()
            option_continue = input("Desea hacer algo mas? (Si o No): ").lower()
            if option_continue == "no":
                print("Entendido, que tenga un feliz dia!")
                valid_option = True
            elif option_continue == "si":
                continue
            else:
                print("La opcion ingresada no es valida, se retornara al menu!")

Sirius().execute()