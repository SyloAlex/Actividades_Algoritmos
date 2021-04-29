#Ejercicio C4E4
class Exercise4():
    def __init__(self, num_list):
        self.num_list = num_list
    
    def odd_sum(self):
        counter = 0
        odd_sum = 0
        odd_list = []
        for number in self.num_list:
            if counter == 5:
                break
            if number % 2 != 0:
                counter += 1
                odd_sum += number
                odd_list.append(number)
        print(f"La cantidad de números impares es: {counter}")
        print(f"Los números impares son: {odd_list}")
        print(f"La suma total de los números impares es: {odd_sum}")

nums = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69 , 113, 166]
exercise4 = Exercise4(nums).odd_sum()