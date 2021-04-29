#Ejercicio 1 de Variables, Operadores y Strings
def new_volume(reservoir, rain):
    rain -= rain*0.1
    reservoir += rain
    reservoir += reservoir*0.05
    reservoir -= reservoir*0.02
    reservoir -= 2.5e5
    print(f"El volumen del reservoirorio es {reservoir}m3")

new_volume(reservoir=4.445e8, rain=5e6)