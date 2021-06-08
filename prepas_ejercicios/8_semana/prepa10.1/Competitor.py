from abc import ABC, abstractmethod

class Competitor(ABC):
    def __init__(self, name, group, category, phone, competitor_number):
        self.name = name
        self.group = group
        self.category = category
        self.phone = phone
        self.competitor_number = competitor_number

    def print_attributes(self):
        for key, value in vars(self).items():
            print(f"{key}: {value}")