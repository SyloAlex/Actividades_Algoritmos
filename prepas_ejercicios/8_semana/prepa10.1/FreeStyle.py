from Competitor import Competitor

class FreeStyle(Competitor):
    def __init__(self, name, group, category, phone, competitor_number, talent):
        Competitor.__init__(self, name, group, category, phone, competitor_number)
        self.talent = talent