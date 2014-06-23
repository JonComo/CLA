import tkinter
from PIL import Image, ImageTk

import Network

class Application(tkinter.Frame):

    network = Network.Network(size=16)

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

        self.network.application = self

    def createWidgets(self):
        self.stepButton = tkinter.Button(self, text='Step', command=self.stepTime)
        self.stepButton.pack(side=tkinter.LEFT)
        self.quitButton = tkinter.Button(self, text='Quit', command=root.destroy)
        self.quitButton.pack(side=tkinter.RIGHT)

        self.canvas = tkinter.Canvas(root, width=400, height=300)
        self.canvas.pack(side=tkinter.LEFT)

    def stepTime(self):
        self.network.processState()

    def viewImage(self, image, left):
        image = image.resize((200,200), Image.NEAREST)
        if left:
            self.leftImage = ImageTk.PhotoImage(image)
            self.canvas.create_image(100, 100, image=self.leftImage)
        else:
            self.rightImage = ImageTk.PhotoImage(image)
            self.canvas.create_image(300, 100, image=self.rightImage)


root = tkinter.Tk()
root.minsize(width=400, height=300)
app = Application(master=root)
app.mainloop()