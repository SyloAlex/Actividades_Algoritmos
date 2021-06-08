from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, health, status, position):
        self.name = name
        self.health = health
        self.status = status
        self.position = position
    
    @abstractmethod
    def print_position(self):
        pass

class Hitter(Player):
    def __init__(self, name, health, status, position, avg, homerun):
        super.__init__(self, name, health, status, position)
        self.avg = avg
        self.homerun = homerun
    
    def print_position(self):
        print(f"{self.name} esta bateando")

class Pitcher(Player):
    def __init__(self, name, health,  status, position, throws, throw_innings):
        super.__init__(self, name, health, status, position)
        self.throws = throws
        self.throw_innings = throw_innings
    
    def print_position(self):
        print(f"{self.name} esta lanzando")