# Ejercicio 1: Contar la cantidad de frutas en el diccionario cesta de frutas usando la lista
# frutas como referencia.

cesta = {"manzanas": 4, "naranjas": 19, "hamburguesas": 3, "sandwiches": 8}
frutas = ["manzanas", "naranjas", "peras", "parchitas", "uvas", "cambures"]

def fruit_quantity(fruit_dict, fruits):
    cantidad_de_frutas, cantidad_de_no_frutas = 0, 0
    for alimento, cantidad in fruit_dict.items():
        if alimento in fruits:
            cantidad_de_frutas += cantidad
        else:
            cantidad_de_no_frutas += cantidad
    print("Hay {} frutas en su cesta y {} objetos que no son frutas".format(cantidad_de_frutas, 
                                                                            cantidad_de_no_frutas))

fruit_quantity(cesta, frutas)

# Ejercicio 2: Contar la cantidad de palabras distintas que hay en la lista quote usand
# un diccionario

quote = ["Tienes", "que", "bailar", "como", "si", "no", "hubiera", "nadie", "mirando", "Ana",
          "como", "si", "nunca", "te", "lastimaran", "Canta", "como", "si", "no", "hubiera",
          "nadie", "escuchando", "y", "vive", "como", "si", "fuera", "el", "cielo", "en",
          "la", "tierra"]

def count_words(word_list):
    counter = {}
    for word in word_list:
        counter[word] = counter.get(word, 0) + 1
        # if word in counter:
        #     counter[word] += 1
        # else:
        #     counter[word] = 1
    print(counter)

count_words(quote)