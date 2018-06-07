class Allergies(object):
    allergies = ["eggs", "peanuts", "shellfish",
                          "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        if item in Allergies.allergies:
            n = Allergies.allergies.index(item)
            n = 2 ** n
            return n & self.score != 0
        else:
            return False

    @property
    def lst(self):
        return list(filter(self.is_allergic_to, Allergies.allergies))
    
