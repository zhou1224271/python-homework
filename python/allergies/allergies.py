class Allergies(object):
    def __init__(self, score):
        self.allergies = ["eggs", "peanuts", "shellfish",
                          "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
        self.score = score

    def is_allergic_to(self, item):
        if item in self.allergies:
            n = self.allergies.index(item)
            n = 2 ** n
            return n & self.score != 0
        else:
            return False

    @property
    def lst(self):
        allergies = []
        for item in self.allergies:
            if self.is_allergic_to(item):
                allergies.append(item)

        return allergies
