# Escriba un programa que itere los enteros del 0 al 50:
# >>> Para múltiplos de tres imprima "Fizz" en lugar del número
# >>> Para los múltiplos de cinco imprima "Buzz".
# >>> Para números que son múltiplos de tres y cinco, imprime "FizzBuzz".
# >>> Para el resto de los números imprima el número.

def number_iterator():
    output = []
    for num in range(0, 51):
        if num % 3 == 0 and num % 5 == 0:
            output.append("FizzBuzz")
        elif num % 3 == 0:
            output.append("Fizz")
        elif num % 5 == 0:
            output.append("Buzz")
        else:
            output.append(num)
    return output

result = number_iterator()
print(result)