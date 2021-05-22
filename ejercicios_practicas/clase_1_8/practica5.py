# Ejercicios de practica para la clase de Listas y Loops

# Ejercicio 1: Escribe un for loop que imprima una lista de numeros 
# multiples de 5 y menores o iguales a 30

def looping_range():
    for number in range(1, 31):
        if number % 5 == 0:
            print(number)

# looping_range()

# Ejercicio 2: Escribir un while loop que tome los numeros de una lista,
# sumar los numeros inpares hasta que haya sumado un maximo de 5.

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 18, 17, 312, 542, 87, 23, 
            86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

def odd_list_summ(numbers):
    count = 0
    index = 0
    odd_sum = 0
    while count < 5 and index < len(numbers):
        if numbers[index] % 2 != 0:
            odd_sum += numbers[index]
            count += 1
        index += 1
    print(f"La cantidad de numeros impares fue: {count}\nLa suma total fue de: {odd_sum}")

# odd_list_summ(num_list)

# Ejercicio 3: Escribe un programa que genere una lista de los ultimos 100 años,
# y genere 2 listas, uno para los años bisiestos y otra para años capicua

def years(number_list):
    leap_year = []
    palindrome = []
    for year in number_list:
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            leap_year.append(year)
        elif year % 4 == 0 and year % 100 != 0:
            leap_year.append(year)
        if str(year) == str(year)[::-1]:
            palindrome.append(year)
    print(f"En los ultimos 100 años hubo {len(leap_year)} año(s) bisiesto(s): {leap_year}")
    print(f"En los ultimos 100 años hubo {len(palindrome)} año(s) palindromo(s): {palindrome}")

years_list = []
for i in range(0, 100):
    years_list.append(2021-i)

years(years_list)