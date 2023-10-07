from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel('models/environment')
        self.block = loader.loadModel('model/Cube.egg')
        self.block_texture = loader.loadTexture('model/cube.png')
        
        self.block.setTexture(self.block_texture)
        self.block.setpos(0, 0, 0)
        self.block.setscale(10)
        self.block.setColor(1, 1, 1, 1)

        self.model.setPos(0, 20, 0)
        self.model.setScale(10)
        

        self.model.reparentTo(render)
        self.block.reparentTo(self.model)
        base.camLens.setFov(90)

base = Game()

base.run()

