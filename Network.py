from Neuron import Neuron
import json
import random

class Network:
    """Basic properties of the neural network: its size, current time and neurons"""
    size = 16
    time = 0

    def __init__(self, size):
        if size > 10000:
            size = 10000

        self.neurons = {}
        self.size = size
        self.layoutNeurons()

    """Layout neurons based on probability, in traditional 6 layer cortical fashion"""
    def layoutNeurons(self):
        self.neurons = {}
        layerCount = 6.0
        amountPerLayer = self.size/layerCount
        currentAmount = 0
        currentLayer = 0
        for i in range(self.size):
            neuron = Neuron(network=self, id=i)
            self.neurons[i] = neuron
            if i >= currentAmount:
                currentLayer += 1.0/layerCount
                currentAmount += amountPerLayer
            neuron.position[1] = currentLayer

    """Run through each neuron and allow it to process its current state"""
    def processState(self):
        for i in range(self.size):
            self.neurons[i].processState()
        self.time += 1

    """Randomize each neuron's energy value for testing purposes"""
    def randomize(self):
        self.layoutNeurons()

    """Return structural data of the network to be rendered"""
    def data(self):
        response = {"type": "structure"}
        response["data"] = {}

        for i in range(self.size):
            neuron = self.neurons[i]
            response["data"][i] = neuron.description()

        return json.dumps(response)