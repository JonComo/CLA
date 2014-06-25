import Neuron
from PIL import Image

class Network:
    """Basic properties of the neural network, its size (sizexsize), current time (time) and neurons"""
    size = 16
    time = 0
    neurons = None
    layers = 5

    """Current image representation of the neural network"""
    visual = None

    def __init__(self, size, layers=5):
        if size > 50:
            size = 50
        if layers > 5:
            layers = 5

        self.layers = layers
        self.size = size
        self.neurons = [[[Neuron.Neuron(network=self) for i in range(size)] for j in range(size)] for i in range(layers)]

    def receiveInput(self, sdr):
        for x in range(self.size):
            for y in range(self.size):
                self.neurons[0][x][y].addEnergy(sdr.values[x][y])

    """Run through each neuron and allow it to process its current state"""
    def processState(self):
        for l in range(self.layers):
            for x in range(self.size):
                for y in range(self.size):
                    self.neurons[l][x][y].processState()
        self.time += 1

    """Randomize each neuron's energy value for testing purposes"""
    def randomize(self):
        for l in range(self.layers):
            for x in range(self.size):
                for y in range(self.size):
                    self.neurons[l][x][y].randomize()


    def saveVisual(self, filename):
        self.visual = Image.new('RGB', (self.size, self.size), "black")  # create a new black image
        pixels = self.visual.load()

        for x in range(self.size):
            for y in range(self.size):
                neuron = self.neurons[0][x][y]
                glow = (int)(255 * neuron.energy)
                pixels[x, y] = (glow, glow, glow)
        #Save image to local directory for display from Bottle server or index.tpl
        self.visual.save(filename)