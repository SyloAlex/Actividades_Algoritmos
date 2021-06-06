from Student import Student

def register_student():
    name = input("Ingrese el nombre del estudiante:\n>> ")
    course = input("Ingrese el grado que cursa el estudiante:\n>> ")
    while True:
        try:
            grade = float(input("Ingrese el promedio del estudiante:\n>> "))
            break
        except:
            print("Por favor solo ingrese el promedio en numeros")
    address = input("Ingrese la direccion del estudiante\n>> ")
    parent = input("Ingrese el nombre del representante:\n>> ")
    while True:
        try:
            phone = int(input("Ingrese el telefono del representante:\n>> "))
            break
        except:
            print("Por favor solo ingrese el telefono en numeros")
    scholarship = "No"
    if grade > 18:
        scholarship = "Si"
    student = Student(name, course, grade, address, parent, phone, scholarship)

    return student

def menu(max):
    while True:
        try:
            menu_option = int(input("Ingrese la opcion del menu:\n>> "))
            if menu_option >= 1 and menu_option <= max:
                break
            else:
                print("La opcion ingresada no es valida")
        except:
            print("Por favor solo ingrese numeros")
    
    return menu_option

def continue_menu():
    valid = False
    while not valid:
        option_continue = input("Desea hacer algo mas? (Si o No):\n>> ").lower()
        if option_continue == "no":
            print("Entendido, que tenga un feliz dia!")
            return_valid = True
            valid = True
        elif option_continue == "si":
            return_valid = False
            valid = True
            continue
        else:
            print("La opcion ingresada no es valida, se retornara al menu!")
    
    return return_valid

def show_database(students):
    if students == []:
        print("La base de datos esta vacia!")
    else:
        students.sort(key=lambda x: x.grade, reverse=True)
        print("Base de Datos CSLC:")
        for student in students:
            print("""
    Nombre: {}
    Curso: {}
    Promedio: {}
    Direccion: {}
    Representante: {}
    Telefono: {}
    Beca: {}
    -------------------""".format(student.name, student.course, student.grade, student.address,
                                student.parent, student.phone, student.scholarship))

def show_top_5(students):
    if students == []:
        print("La base de datos esta vacia!")
    else:
        students.sort(key=lambda x: x.grade, reverse=True)
        print("Base de Datos CSLC:")
        i = 0
        while i < 5:
            print("""
    Nombre: {}
    Curso: {}
    Promedio: {}
    Direccion: {}
    Representante: {}
    Telefono: {}
    Beca: {}
    -------------------""".format(students[i].name, students[i].course, students[i].grade, students[i].address,
                                students[i].parent, students[i].phone, students[i].scholarship))
            i += 1

def general_mean(students):
    if students == []:
        print("La base de datos esta vacia!")
    else:
        mean = 0
        for student in students:
            mean += student.grade
        mean = mean / len(students)
        print(f"El promedio general de la institucion es {mean}")

def grade_ten_fifteen(students):
    if students == []:
        print("La base de datos esta vacia!")
    else:
        more_than_16 = 0
        between_10_and_16 = 0
        less_than_10 = 0
        for student in students:
            if student.grade >= 16:
                more_than_16 += 1
            elif student.grade <= 10:
                less_than_10 += 1
            else:
                between_10_and_16 +=1
        print("""
        Estudantes con promedio menor a 10: {}
        Estudantes con promedio entre 10 y 16: {}
        Estudantes con promedio mayor a 16: {}
        """.format(less_than_10, between_10_and_16, more_than_16))
