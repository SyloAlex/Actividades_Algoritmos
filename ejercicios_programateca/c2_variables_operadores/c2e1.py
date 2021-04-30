#Ejercicio 1 de Variables, Operadores y Strings
class WaterReservoir:
    def __init__(self, reservoir, rain):
        self.reservoir = reservoir
        self.rain = rain
    def new_volume(self):
        rain_changed = self.rain
        reservoir_changed = self.reservoir
        rain_changed -= rain_changed*0.1
        reservoir_changed += rain_changed
        reservoir_changed += reservoir_changed*0.05
        reservoir_changed -= reservoir_changed*0.02
        reservoir_changed -= 2.5e5
        print(f"El volumen del reservoirorio es {reservoir_changed}m3")

change_volume = WaterReservoir(reservoir=4.445e8, rain=5e6).new_volume()