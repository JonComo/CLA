__author__ = 'joncomo'

import random
import Network

class Neuron:
    energy = 0
    network = None
    position = None

    def __init__(self, network, position=[0, 0, 0]):
        self.network = network
        self.weights = [[0 for i in range(network.size)] for j in range(network.size)]
        self.position = position;
        self.randomPosition()

    def processState(self):
        self.energy *= 0.6
        # Modify weights based on previously active

    def randomize(self):
        self.energy = random.uniform(0.0, 1.0)

    def randomPosition(self):
        self.position = [random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)]

    def addEnergy(self, energy):
        self.energy += energy
        if (self.energy > 1): self.energy = 1

    def description(self):
        return {"p": self.position, "e": self.energy}