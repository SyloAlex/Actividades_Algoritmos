#Ejercicio 2.6: Este juego consiste en solicitar varias palabras en inglés por teclado y 
#luego insertarlas en un texto con espacios vacíos para crear una historia.

class MadLibs:
    def __init__(self):
        self.adjectives = []
        self.plural_nouns = []
        self.city = ""
        self.place = ""
        self.celebrity = ""
        self.number = ""
        self.verb = ""
        self.body_parts = []
        self.letter = ""
        self.singular_nouns = []
        self.femenine_name = ""
        self.clothing = ""

    def get_adjectives(self):
        '''
            Recibe el input de 6 adjetivos y verifica si son validos
        '''
        valid = False
        while not valid:
            input_adjectives = input("Ingresa 6 adjetivos separados por un espacio en blanco: ")
            adjectives_list = []
            input_adjectives = input_adjectives.split(" ")
            try:
                for adjective in input_adjectives:
                    if adjective.isalpha() == False:
                        raise ValueError
                    else:
                        adjectives_list.append(adjective)
                if len(adjectives_list) == 6:
                    valid = True
                    self.adjectives += adjectives_list
                else:
                    print("Ingresaste menos palabras de las indicadas")
            except ValueError:
                print("Ingresaste numeros o caracteres especiales y las palabras solo tienen letras")

    def get_plural_nouns(self):
        '''
            Recibe el input de 4 sustantivos en plural y verifica si son validos
        '''
        valid = False
        while not valid:
            input_plural_nouns = input("Ingresa 4 sustantivos plurales separados por un espacio en blanco: ")
            plural_nouns_list = []
            input_plural_nouns = input_plural_nouns.split(" ")
            try:
                for plural_noun in input_plural_nouns:
                    if plural_noun.isalpha() == False:
                        raise ValueError
                    else:
                        plural_nouns_list.append(plural_noun)
                if len(plural_nouns_list) == 4:
                    valid = True
                    self.plural_nouns += plural_nouns_list
                else:
                    print("Ingresaste menos palabras de las indicadas")
            except ValueError:
                print("Ingresaste numeros o caracteres especiales y las palabras solo tienen letras")

    def get_city(self):
        '''
            Recibe el input de 1 ciudad y verifica si es valido
        '''
        valid = False
        while not valid:
            input_city = input("Ingresa el nombre de una ciudad: ")
            try:
                if input_city.isalpha() == False:
                    raise ValueError
                else:
                    self.city = input_city
                    valid = True
            except ValueError:
                print("Ingresaste numeros o caracteres especiales y las palabras solo tienen letras")

    def get_place(self):
        '''
            Recibe el input de 1 lugar y verifica si es valido
        '''
        valid = False
        while not valid:
            input_place = input("Ingresa el nombre de un lugar: ")
            try:
                if input_place.isalpha() == False:
                    raise ValueError
                else:
                    self.place = input_place
                    valid = True
            except ValueError:
                print("Ingresaste numeros o caracteres especiales y las palabras solo tienen letras")

    def get_celebrity(self):
        '''
            Recibe el input de 1 celebridad y verifica si es valido
        '''
        valid = False
        while not valid:
            input_celebrity = input("Ingresa el nombre de una celebridad: ")
            try:
                if input_celebrity.isalpha() == False:
                    raise ValueError
                else:
                    self.celebrity = input_celebrity
                    valid = True
            except ValueError:
                print("Ingresaste numeros o caracteres especiales y las palabras solo tienen letras")

    def get_number(self):
        '''
            Recibe el input de 1 numero y verifica si es valido
        '''
        valid = False
        while not valid:
            input_number = input("Ingresa un numero: ")
            try:
                if input_number.isnumeric() == False:
                    raise ValueError
                else:
                    self.number = input_number
                    valid = True
            except ValueError:
                print("Ingresaste letras o caracteres especiales y no un numero")
    
    def get_verb(self):
        '''
            Recibe el input de 1 verbo y verifica si es valido
        '''
        valid = False
        while not valid:
            input_verb = input("Ingresa un verbo: ")
            try:
                if input_verb.isalpha() == False:
                    raise ValueError
                else:
                    self.verb = input_verb
                    valid = True
            except ValueError:
                print("Ingresaste numeros o caracteres especiales y las palabras solo tienen letras")
    
    def get_body_parts(self):
        '''
            Recibe el input de 2 partes del cuerpo y verifica si son validos
        '''
        valid = False
        while not valid:
            input_body_parts = input("Ingresa el nombre de 2 partes del cuerpo separados por un espacio en blanco: ")
            body_parts_list = []
            input_body_parts = input_body_parts.split(" ")
            try:
                for body_part in input_body_parts:
                    if body_part.isalpha() == False:
                        raise ValueError
                    else:
                        body_parts_list.append(body_part)
                if len(body_parts_list) == 2:
                    valid = True
                    self.body_parts += body_parts_list
                else:
                    print("Ingresaste menos palabras de las indicadas")
            except ValueError:
                print("Ingresaste numeros o caracteres especiales y las palabras solo tienen letras")

    def get_letter(self):
        '''
            Recibe el input de 1 letra y verifica si es valido
        '''
        valid = False
        while not valid:
            input_letter = input("Ingresa una letra del alfabeto: ")
            try:
                if input_letter.isalpha() == False or len(input_letter) != 1:
                    raise ValueError
                else:
                    self.letter = input_letter
                    valid = True
            except ValueError:
                print("Ingresaste numeros o caracteres especiales, o mas de una letra")

    def get_singular_nouns(self):
        '''
            Recibe el input de 2 sustantivos en singular y verifica si son validos
        '''
        valid = False
        while not valid:
            input_singular_nouns = input("Ingresa 2 sustantivos singulares separados por un espacio en blanco: ")
            singular_nouns_list = []
            input_singular_nouns = input_singular_nouns.split(" ")
            try:
                for singular_noun in input_singular_nouns:
                    if singular_noun.isalpha() == False:
                        raise ValueError
                    else:
                        singular_nouns_list.append(singular_noun)
                if len(singular_nouns_list) == 2:
                    valid = True
                    self.singular_nouns += singular_nouns_list
                else:
                    print("Ingresaste menos palabras de las indicadas")
            except ValueError:
                print("Ingresaste numeros o caracteres especiales y las palabras solo tienen letras")
        print(self.singular_nouns)

    def get_femenine_name(self):
        '''
            Recibe el input de 1 nombre femenino y verifica si es valido
        '''
        valid = False
        while not valid:
            input_femenine_name = input("Ingresa un nombre femenino: ")
            try:
                if input_femenine_name.isalpha() == False:
                    raise ValueError
                else:
                    self.femenine_name = input_femenine_name
                    valid = True
            except ValueError:
                print("Ingresaste numeros o caracteres especiales y las palabras solo tienen letras")
    
    def get_clothing(self):
        '''
            Recibe el input de 1 prenda de vestir y verifica si es valido
        '''
        valid = False
        while not valid:
            input_clothing = input("Ingresa el nombre de una prenda de vestir: ")
            try:
                if input_clothing.isalpha() == False:
                    raise ValueError
                else:
                    self.clothing = input_clothing
                    valid = True
            except ValueError:
                print("Ingresaste numeros o caracteres especiales y las palabras solo tienen letras")

    def story_output(self):
        '''
            Formatea la historia segun los inputs del usuario para crear su propio cuento
        '''
        story = f"There are many {self.adjectives[0]} ways to choose a/an {self.singular_nouns[0]} to read. First, you could ask for recommendations from your friends and {self.plural_nouns[0]}. Just don't ask Aunt {self.femenine_name} -- she only reads {self.adjectives[1]} books with {self.clothing}-ripping goddesses on the cover. If your friends and family are no help, try checking out the {self.singular_nouns[1]} Review in 'The {self.city} Times'. If the {self.plural_nouns[1]} featured there are too {self.adjectives[2]} for your taste, try something a little more low-{self.body_parts[0]}, like {self.letter}: 'The {self.celebrity} Magazine', or '{self.plural_nouns[2]} Magazine'. You could also choose a book the {self.adjectives[3]}-fashioned way. Head to your local library or {self.place} and browse the shelves until something catches your {self.body_parts[1]}. Or, you could save yourself a whole lot of {self.adjectives[4]} trouble and log on to www.bookish.com, the {self.adjectives[5]} new website to {self.verb} for books! With all the time you'll save not having to search for {self.plural_nouns[3]}, you can read {self.number} more books!"
        print(story)

    def execute_mad_libs(self):
        '''
            Ejecuta todas las funciones de input y output
        '''
        print("Bienvenido a Mad Libs! A continuacion se te daran una serie de instrucciones\nPorf favor ingresa todo en ingles")
        self.get_adjectives()
        self.get_plural_nouns()
        self.get_city()
        self.get_place()
        self.get_celebrity()
        self.get_number()
        self.get_verb()
        self.get_body_parts()
        self.get_letter()
        self.get_singular_nouns()
        self.get_femenine_name()
        self.get_clothing()
        self.story_output()

prueba = MadLibs().execute_mad_libs()
