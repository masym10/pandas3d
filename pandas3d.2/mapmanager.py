import pickle

class MapManager:
    def __init__(self):
        self.model = 'model/block/block.egg'
        self.texture = 'model/block/block.png'
        self.color = (0.2, 0.2, 0.35, 0.5)# 4 прозорість

        self.addNew() #create new location

    def addNew(self):
        """створюєм основну для нової карти
        """
        self.land = render.attachNewNode('Land')
        
    def addBlock(self, position):
        """створює блок
        """

        block = loader.loadModel(self.model)
        block_texture = loader.loadTexture(self.texture)


        block.setTexture(block_texture)
        block.setPos(position)
        block.setColor(self.color)

        block.setTag('at', str(position))

        block.reparentTo(self.land)

    def delBlock(self, position):
       blocks = self.findBlocks(position)
       for block in blocks:
           block.removeNode()

    def delBlockFrom(self, pos):
        x, y, z = self.findHightestEmpty(pos)
        pos = x, y, z-1
        for block in self.findBlocks(pos):
            block.removeNode()
    
    def buildBlock(self, pos):
        x, y, z = pos
        new_pos = self.findHightestEmpty(pos)
        if new_pos[2] <=z + 1:
            self.addBlock(new_pos)

    def loadMap(self, filename):
        """зчитування карти
        """
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(" ")
                for number in line:
                    for z in range(int(number) + 1):
                        self.addBlock((x,y,z))
                    x +=1
                y +=1
    
    def saveMap(self):
        blocks = self.land.getChildren()
        with open('map.dat', 'wb') as file:
            pickle.dump(len(blocks), file)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, file)

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def clear(self):
        self.land.removeNode()
        self.addNew()

    def load_map(self):
        self.clear()
        with open('map.dat', 'rb') as file:
            lenght = pickle.load(file)
            
            for i in range(lenght):
                pos = pickle.load(file)
                self.addBlock(pos)

    def findBlocks(self, pos):
        return self.land.findAllMatches("=at="+str(pos))

    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True

    def findHightestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z +=1

        return (x, y, z)