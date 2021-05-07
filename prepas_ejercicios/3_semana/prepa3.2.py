# Ejercicio 3.2: Se tienen tres textos almacenados en tres variables como strings. 
# Para cada texto debes contar cuántas veces se repite la sílaba indicada y qué índice 
# ocupa cada repetición.

x = "Outside of that, Hu argues that the royalties can be more reliable than the entropy of Wall Street. No matter what happens to the stock market, people are always going to be listening to music."
y = "CBD, which comes from either a marijuana or hemp plant, is non-psychoactive, so it won’t get you high like THC (tetrayhydrocannabinol). It may, however, offer anti-inflammatory, antioxidant, anti-psychotic, anti-convulsant, and antidepressant properties. Because it can hemp is legal in all 50 states, hemp-derived CBD products are becoming more readily available online and in stores all over the country."
z = "According to a report published by Fast Company, apparel sales have plummeted by 50 percent. It’s a margin that will be difficult to recover from, especially for small businesses that don’t have the backing of major conglomerates. These independent companies rely on seasonal buys from retailers to stay afloat. But with the bevy of store closures and restrictions on online sales, these behemoth retailers are facing hard times of their own."

buscador = ["at", "om", "in"]

def check_duplicates(text, searcher):
    valid = False
    duplicates = []
    inicio = 0
    while valid is False and inicio < len(text) - 1:
        try:
            duplicate_index = text.index(searcher, inicio)
            duplicates.append([duplicate_index, duplicate_index + 1])
        except ValueError:
            valid = True
        inicio = duplicate_index + 2
    count = text.count(searcher)
    print(f"Silaba: {searcher}")
    print(f"Hubo un total de {count} incidencia(s) en el texto")
    print(f"Las incidencias ocurrieron en los indices {duplicates}")

check_duplicates(x, buscador[0])
check_duplicates(y, buscador[1])
check_duplicates(z, buscador[2])