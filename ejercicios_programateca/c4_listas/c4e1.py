#Ejercicio C4E1
class ListInput():
    def __init__(self):
        self.new_list = []
    def get_input(self):
        phrase = input("Escriba una lista de palabras separando las palabras con espacios: ")
        new_phrase = phrase.split()
        word_list = []
        for word in new_phrase:
            word_list.append(word)
        self.new_list = word_list

    def print_list(self):
        self.get_input()
        for words in self.new_list:
            print(words)

lista = ListInput().print_list()