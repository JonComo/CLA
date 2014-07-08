from Neuron import Neuron

class Network:
    """Basic properties of the neural network: its size, current time and neurons"""
    size = 16
    time = 0
    neurons = []

    def __init__(self, size):
        if size > 10000:
            size = 10000

        self.size = size
        self.layoutNeurons()

    """Layout neurons based on probability, in traditional 6 layer cortical fashion"""
    def layoutNeurons(self):
        self.neurons = []
        for i in range(self.size):
            neuron = Neuron(network=self, id=i)
            self.neurons.append(neuron)

    """Run through each neuron and allow it to process its current state"""
    def processState(self):
        for i in range(self.size):
            self.neurons[i].processState()
        self.time += 1

    """Randomize each neuron's energy value for testing purposes"""
    def randomize(self):
        self.layoutNeurons()