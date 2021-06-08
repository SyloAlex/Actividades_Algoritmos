from Competitor import Competitor

class Dancer(Competitor):
    def __init__(self, name, group, category, phone, competitor_number, style):
        Competitor.__init__(self, name, group, category, phone, competitor_number)
        self.style = style