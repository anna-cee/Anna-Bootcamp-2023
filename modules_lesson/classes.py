#class construction
class Food:
    def __init__(self, name, isHealthy):
        self.name = name
        self.isHealthy = isHealthy

#inheritance
class Food:
    def __init__(self, name, isHealthy):
        self.name = name
        self.isHealthy = isHealthy

class Fruit(Food):
    def __init__(self, name, hasSeeds, hasStone):
        super().__init__(name, True)
        self.hasSeeds = hasSeeds
        self.hasStone = hasStone
