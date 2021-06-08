from Competitor import Competitor

class Musician(Competitor):
    def __init__(self, name, group, category, phone, competitor_number, instrument):
        Competitor.__init__(self, name, group, category, phone, competitor_number)
        self.instrument = instrument