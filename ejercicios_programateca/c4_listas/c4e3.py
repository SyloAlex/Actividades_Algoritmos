#Ejercicio C4E3
class Exercise3():
    def __init__(self, exercise_list):
        self.exercise_list = exercise_list
    
    def blanks_to_underscore(self):
        username = []
        for student in self.exercise_list:
            student = student.lower()
            student = student.replace(" ", "_")
            username.append(student)
        print(username)

class_list = ["Emmie Grey", "Andre Hills", "Gurpreet Atherton",
"Johan Stewart", "Joseff Hurst", "Margot Conrad", "Matteo Whitaker",
"Mekhi Hussain", "Sherry Macdonald", "Mathew Cano", "Cara O'Moore",
"Kush Gonzalez", "Soren Clark", "Inaayah Broadhurst", "Ruth Lawrence",
"Nafisa Nairn", "Zachariah Velasquez"]

exercise2 = Exercise3(class_list).blanks_to_underscore()