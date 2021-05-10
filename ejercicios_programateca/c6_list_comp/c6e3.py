# C6E3: Dada un String de caracteres en minúscula. La tarea es verificar si el string dado es un 
# heterograma o no. Un heterograma es una palabra, frase u oración en la que ninguna letra 
# del alfabeto aparece más de una vez.

def heterogram():
    phrase = input("Escriba una frase: ").lower()
    flag = True
    for index in range((len(phrase)//2)+1):
        if phrase[index] == " ":
            pass
        elif phrase[index] in phrase[index+1:len(phrase)]:
            print(f"La oracion {phrase} no es un heterograma")
            flag = False
            break
    if flag == True:
        print(f"La oracion {phrase} es un heterograma")

def heterogram_set():
    phrase = input("Escriba una frase: ").lower()
    phrase_set = set(phrase)
    if len(phrase) == len(phrase_set):
        print(f"La oracion {phrase} es un heterograma")
    else:
        print(f"La oracion {phrase} no es un heterograma")

heterogram_set()