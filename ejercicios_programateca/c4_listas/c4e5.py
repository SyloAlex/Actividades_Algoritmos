# Ejercicio C4E5: Escribe un programa para verificar si los números provistos en la 
# lista chequear_primos son números primos

numbers = [5, 2, 1, 4, 98, 7, 654, 754]

def check_prime(num_list):
    for num in num_list:
        divisible = []
        for num_range in range(2, (num // 2) +1):
            if num % num_range == 0:
                divisible.append(num_range)
        if divisible == []:
            print(f"{num} es un numero primo")
        else:
            print(f"{num} no es un numero primo, ya que es divisible entre {divisible}")

check_prime(numbers)                