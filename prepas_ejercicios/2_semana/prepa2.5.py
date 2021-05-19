# Ejercicio 2.5: Realiza un programa que tome por teclado una palabra y 
# verifique que solo contenga letras. Luego, recorriendo el string, cada 
# vez que haya una vocal, debe convertirse a mayúscula. Todas las consonantes 
# deben estar en minúscula.

def get_input():
    '''
    Recibe el numero
    '''
    valid = False
    while not valid:
        inp = input("Por favor, ingrese una palabra:\n>> ")
        if inp.isalpha():
            valid = True
        else:
            print("Escribe solo letras!")
    
    return inp

def lower_upper(word):
    vocals = "aeiou"
    new_word = ''
    word = word.lower()
    for index in range(len(word)):
        if word[index] in vocals:
            new_word += word[index].upper()
        else:
            new_word += word[index]
    print(new_word)

example_word = get_input()
lower_upper(example_word)