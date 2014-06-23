__author__ = 'joncomo'

from PIL import Image, ImageTk
import Network
import SDR

class ImageEncoder():

    index = 0
    images = []
    size = 0

    def loadImages(self, name, count):
        for i in range(0, count):
            img = Image.open('%s%d.png' % (name, i))
            self.images.append(img)
        image = self.images[0]
        self.size = image.size[0]

    def perceiveNext(self) -> SDR:
        sdr = self.perceiveImage(self.images[self.index])

        self.index += 1
        if (self.index > len(self.images)-1):
            self.index = 0

        return sdr

    def perceiveImage(self, image) -> SDR:
        pixels = image.load()
        sdr = SDR.SDR(self.size)

        for x in range(self.size):
            for y in range(self.size):
                pixel = pixels[x, y]
                sdr.values[x][y] = (pixel[0] + pixel[1] + pixel[2])/(3.0 * 255.0)
        return sdr