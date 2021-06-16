import requests

def select_option(max):
    while True:
        try:
            option = int(input("Ingrese la opcion de la pelicula:\n>> "))
            if option >= 1 and option <= max:
                break
            else:
                print("La opcion ingresada no es valida")
        except:
            print("Por favor solo ingrese numeros")
    
    return option

def search_movie(movie, parameter):
    url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/{parameter}/{movie}"
    headers = {
        'x-rapidapi-key': "e516d4f949msh483f4c7980cbe55p14066cjsnd09194288c70",
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers)
    
    return response.json()

def select_movie(results):
    for i, result in enumerate(results["titles"]):
        print(f"{i+1}.- {result['title']}")
    option = select_option(len(results["titles"]))

    return results["titles"][option-1]["id"]



def main():
    movie = input("Ingrese la pelicula a buscar:\n>> ")
    movie_list = search_movie(movie, "search")
    id = select_movie(movie_list)
    movie = search_movie(id, "film")
    print(movie)


main()