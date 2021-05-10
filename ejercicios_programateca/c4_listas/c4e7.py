# C4E7: Una famosa cadena de noticias te contrato para que diseñaras un programa el cual muestre los titulares en Twitter, 
# sin embargo esta plataforma limita los tweets a 140 caracteres.
# Escribe un Loop con Break en donde recorras la lista titulares dada, y en cada iteración inserta 
# los titulares en una variable tweet

headlines = ["Oso se come a hombre en el Avila",
             "Anuncian nuevas leyes para la nación",
             "Si lees esto, estudia los resumenes de clase para el Quiz ;)",
             "Gato rescata a bombero atrapado en un árbol",
             "La UNIMET tiene nueva cancha de fútbol",
             "Los estudiantes de algoritmos y programción son los mejores!"]

def news_media(headline_list):
    tweet = ""
    for headline in headline_list:
        if tweet == "":
            tweet = tweet + headline
        elif len(tweet) < 140:
            tweet = tweet + ', ' + headline
        else:
            break
    print(tweet[0:140])

news_media(headlines)