import random
import sys
import Network

class Neuron:
    energy = 0
    network = None
    position = None
    id = 0

    def __init__(self, network, position=[0, 0, 0], id=0):
        self.id = id
        self.network = network
        self.weights = {}
        self.position = position
        self.randomPosition()
        self.randomize()

    def processState(self):
        self.energy *= 0.6  # K leak amount

        for neuron in self.network.neurons:
            if neuron == self:
                continue
            if neuron.energy > 0.3:
                pass
        # Modify weights based on previously active

    def randomize(self):
        self.energy = random.uniform(0.0, 1.0)

    def randomPosition(self):
        self.position = [self.randomNumber(), self.randomNumber(), self.randomNumber()]

    def addEnergy(self, energy):
        self.energy += energy
        if self.energy > 1:
            self.energy = 1

    def description(self):
        return {"p": [round(self.position[0], 2), round(self.position[1], 2), round(self.position[2], 2)], "e": round(self.energy, 2)}

    def randomNumber(self):
        return round(random.uniform(0.0, 1.0), 2)

    """Find neurons close to this one, in layer or by distance"""
    def neuronsWithinDistance(self, distance=0):
        testDist = sys.float_info.max



