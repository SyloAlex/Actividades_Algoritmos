# C6E1A: Use List comprehension para crear una nueva lista primeros_nombres que contenga 
# solo los primeros nombres en minúsculas de la lista estudiantes.

students = ["Emmie Grey",
"Andre Hills",
"Gurpreet Atherton",
"Johan Stewart",
"Joseff Hurst",
"Margot Conrad",
"Matteo Whitaker",
"Mekhi Hussain",
"Sherry Macdonald",
"Mathew Cano",
"Cara O'Moore",
"Kush Gonzalez",
"Soren Clark",
"Inaayah Broadhurst",
"Ruth Lawrence",
"Nafisa Nairn",
"Zachariah Velasquez"]

def first_names(names):
    first_name = [name.split(" ")[0].lower() for name in names]
    print(*first_name)

def multiple_of_3():
    multiples = [num for num in range(1, (3*20)+1) if num % 3 == 0 ]
    print(multiples)

first_names(students)

# C6E1B: Use un List comprehension para crear una lista multiplos_3 
# que contenga los primeros 20 múltiplos de 3

multiple_of_3()