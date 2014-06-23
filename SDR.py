__author__ = 'joncomo'

class SDR():

    values = None

    def __init__(self, size):
         self.values = [[0.0 for i in range(0, size)] for i in range(0, size)]