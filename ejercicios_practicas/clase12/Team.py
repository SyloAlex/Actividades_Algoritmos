class Team:
    def __init__(self, name, city, roster):
        self.name= name
        self.city = city
        self.roster = roster
        self.wins = 0
        self.losses = 0
    
    def get_win(self):
        self.wins += 1
    
    def get_losses(self):
        self.losses += 1