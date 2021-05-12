# Ejercicio C7E2: Contar la cantidad de palabras distintas que hay en la lista quote usand
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