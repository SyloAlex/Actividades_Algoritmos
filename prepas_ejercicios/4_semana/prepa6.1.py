# Se ha realizado un estudio demográfico en una urbanización y se te ha solicitado 
# que, a partir de los datos obtenidos (almacenados en un diccionario de diccionarios), 
# calcules las siguientes estadísticas:
# Cantidad total de residentes de la urbanización.
# Promedio de edad por género.
# Nombre y edad de la persona más joven.
# Nombre y edad de la persona más vieja.
# Cantidad de personas según su ocupación

ocupantes = {"Julia Rodríguez": {"Edad": 21, "Género": "M", "Ocupación": "Estudiante"}, 
              "Santiago López": {"Edad": 33, "Género": "H", "Ocupación": "Abogado"}, 
              "Luis González": {"Edad": 8, "Género": "H", "Ocupación": "Estudiante"}, 
              "Luisana González": {"Edad": 5, "Género": "M", "Ocupación": "Estudiante"}, 
              "Martina Reverón de González": {"Edad": 37, "Género": "M", "Ocupación": "Ingeniero"}, 
              "Sergio González": {"Edad": 37, "Género": "H", "Ocupación": "Ingeniero"}, 
              "Abel Araujo": {"Edad": 81, "Género": "H", "Ocupación": "Médico"}, 
              "Roberto Mendoza": {"Edad": 56, "Género": "H", "Ocupación": "Profesor"}, 
              "Bárbara Zapatero de Piñera": {"Edad": 32, "Género": "M", "Ocupación": "Psicólogo"}, 
              "Leonardo Piñera": {"Edad": 31, "Género": "H", "Ocupación": "Administrador"}, 
              "Gustavo Álvarez": {"Edad": 14, "Género": "H", "Ocupación": "Estudiante"}, 
              "Guillermo Álvarez": {"Edad": 38, "Género": "H", "Ocupación": "Médico"}, 
              "Laura Paz de Álvarez": {"Edad": 38, "Género": "M", "Ocupación": "Desempleado"}, 
              "Ignacio Salcedo": {"Edad": 19, "Género": "H", "Ocupación": "Estudiante"}, 
              "Saúl Salcedo": {"Edad": 22, "Género": "H", "Ocupación": "Estudiante"}, 
              "Romina Salcedo": {"Edad": 25, "Género": "M", "Ocupación": "Administrador"}, 
              "Elena Pinto de Salcedo": {"Edad": 52, "Género": "M", "Ocupación": "Abogado"}, 
              "Mauricio Salcedo": {"Edad": 52, "Género": "H", "Ocupación": "Ingeniero"}, 
              "Tatiana Echeverría": {"Edad": 68, "Género": "M", "Ocupación": "Médico"}, 
              'Marcelo Gonçalves': {"Edad": 27, "Género": "H", "Ocupación": "Administrador"}, 
              "Jessica Franco de Gonçalves": {"Edad": 26, "Género": "M", "Ocupación": "Profesor"}, 
              "Valerio Fiore": {"Edad": 97, "Género": "H", "Ocupación": "Desempleado"}, 
              "Giuliana Rossi de Fiore": {"Edad": 95, "Género": "M", "Ocupación": "Desempleado"}, 
              "José Castro": {"Edad": 35, "Género": "H", "Ocupación": "Abogado"}, 
              "Samantha Correa de Castro": {"Edad": 35, "Género": "M", "Ocupación": "Abogado"}, 
              "Ángel Castro": {"Edad": 7, "Género": "H", "Ocupación": "Estudiante"}, 
              "Antonieta Marín": {"Edad": 58, "Género": "M", "Ocupación": "Profesor"}, 
              "Lorenzo Blanco": {"Edad": 77, "Género": "H", "Ocupación": "Abogado"}, 
              "Vanessa Blanco de Bustamante": {"Edad": 37, "Género": "M", "Ocupación": "Médico"}, 
              "Raúl Bustamante": {"Edad": 39, "Género": "H", "Ocupación": "Médico"}, 
              "Carolina Alcalá": {"Edad": 24, "Género": "M", "Ocupación": "Ingeniero"}, 
              "Juan Alcalá": {"Edad": 60, "Género": "H", "Ocupación": "Psicólogo"}, 
              "Ingrid Gil de Alcalá": {"Edad": 60, "Género": "M", "Ocupación": "Profesor"}, 
              "Francesca Costa de Gil": {"Edad": 88, "Género": "M", "Ocupación": "Médico"}, 
              "Giancarlo Gil": {'Edad': 89, "Género": "H", "Ocupación": "Psicólogo"}, 
              "César Lovera": {"Edad": 64, "Género": "H", "Ocupación": "Administrador"}, 
              "Natalia Lovera": {"Edad": 64, "Género": "M", "Ocupación": "Desempleado"}}

def resident_statistics(residentes):
    male_age, female_age = 0, 0
    genre = {}
    old = []
    statistics = {}
    for residents, info in residentes.items():
        for key, value in info.items():
            if key == "Edad":
                old.append(info[key])
            if info[key] == "H":
                genre["Male"] = genre.get("Male", 0) + 1
                male_age += info["Edad"]
            elif info[key] == "M":
                genre["Female"] = genre.get("Female", 0) + 1
                female_age += info["Edad"]
            if key == "Ocupación":
                statistics[value] = statistics.get(value, 0) + 1
    print("Hay un total de {} residentes".format(genre["Male"] + genre["Female"]))
    print("Promedio de edad hombres: {}".format(male_age // genre["Male"]))
    print("Promedio de edad mujeres: {}".format(female_age // genre["Female"]))
    for residents, info in residentes.items():
        if info["Edad"] == sorted(old)[0]:
            print(f"La persona mas joven es {residents} con {sorted(old)[0]} años.")
        if info["Edad"] == sorted(old)[-1]:
            print(f"La persona mas joven es {residents} con {sorted(old)[-1]} años.")
    print("Profesiones:\n---------")
    for key, value in statistics.items():
        print(f"{key}: {value}")

resident_statistics(ocupantes)