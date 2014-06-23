import random
from PIL import Image, ImageTk
import ImageEncoder
import SDR

class Network:
    size = 16
    time = 0

    application = None
    neurons = None

    #images as source
    imageEncoder = None

    visual = None

    def __init__(self, size):
        self.size = size
        self.neurons = [[Neuron(network=self) for i in range(size)] for j in range(size)]

        self.imageEncoder = ImageEncoder.ImageEncoder()
        self.imageEncoder.loadImages(name='input/test', count=3)


    def processState(self):
        # Image encoding
        sdr = self.imageEncoder.perceiveNext()

        for x in range(self.size):
            for y in range(self.size):
                self.neurons[x][y].addEnergy(sdr.values[x][y])
                self.neurons[x][y].processState()

        self.time += 1
        self.visualize()

    def randomize(self):
        for x in range(self.size):
            for y in range(self.size):
                self.neurons[x][y].randomize()

    def visualize(self):
        img = Image.new('RGB', (self.size, self.size), "black")  # create a new black image
        pixels = img.load()

        for x in range(self.size):
            for y in range(self.size):
                neuron = self.neurons[x][y]
                glow = (int)(255 * neuron.energy)
                pixels[x, y] = (glow, glow, glow)

        self.visual = img
        self.application.viewImage(self.visual, left=True)
        self.application.viewImage(self.visual, left=False)

        self.application.mainloop()



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