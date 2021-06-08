from Competitor import Competitor

class Singer(Competitor):
    def __init__(self, name, group, category, phone, competitor_number, song, author):
        Competitor.__init__(self, name, group, category, phone, competitor_number)
        self.song = song
        self.author = author