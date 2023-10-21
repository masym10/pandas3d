from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = MapManager()
        self.land.loadMap('my_map.txt')
        self.hero = Hero((5,(40-8),1), self.land)
        self.hero.accept_events()

        base.camLens.setFov(90)

base = Game()

base.run()