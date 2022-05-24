class WaitingLounge:
    def __init__(self, planet, puncts, weight):
        self.planet = planet
        self.weight = weight
        self.puncts = puncts

    def __add__(self, other):
        return WaitingLounge(min(self.puncts.exten(other.puncts)), self.puncts.extend(other.puncts), self.weight + other.weight)

    def __eq__(self, other):
        if len(self.puncts) == len(other.puncts) and self.weight == other.weight and self.planet == other.planet:
            return True

    def __ne__(self, other):
        if len(self.puncts) != len(other.puncts) or self.weight != other.weight or self.planet != other.planet:
            return True

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def  __le__(self, other):
        pass

    def __ge__(self, other):
        pass

