__author__ = 'joncomo'

import random
import Network

class Neuron:
    energy = 0
    network = None

    def __init__(self, network):
        self.network = network
        self.weights = [[0 for i in range(network.size)] for j in range(network.size)]

    def processState(self):
        self.energy *= 0.6
        # Modify weights based on previously active

    def randomize(self):
        self.energy = random.uniform(0.0, 1.0)

    def addEnergy(self, energy):
        self.energy += energy
        if (self.energy > 1): self.energy = 1