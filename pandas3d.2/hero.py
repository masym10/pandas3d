class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor((0.2, 0.2, 0.2, 0))
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.accept_events()
        self.cameraOn = False
        self.mode = True

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.setH(120)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True
    
    def cameraUp(self):
        base.camera.reparentTo(render)
        base.mouseInterfaceNode.setPos(self.hero.getPos())
        base.enableMouse()
        self.cameraOn = False

    def changView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return(-1, 1)
        elif angle <= 290:
            return(-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return(0, -1)
        
    def lookAt(self, angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)
        return x+dy, y+dy, z
    
    def justMove(self, angel):
        pos = self.lookAt(angel)
        self.hero.setPos(pos)

    def tryMove(self, angel):
        pos = self.lookAt(angel)
        if self.land.isEmpty(pos):
            pos = self.land.findHightestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)
        
    def changeMode(self):
        self.mode = not self.mode

    def moveTo(self, angel):
        if self.mode == True:
            self.justMove(angel)
        else:
            self.tryMove(angel)
        
    def forward(self):
        angle = self.hero.getH() % 360
        self.moveTo(angle)

    def forwardBack(self):
        angle = (self.hero.getH() + 180) % 360
        self.moveTo(angle)

    def forwardLeft(self):
        angle = (self.hero.getH() + 90) % 360
        self.moveTo(angle)

    def forwardRight(self):
        angle = (self.hero.getH() - 90) % 360
        self.moveTo(angle)

    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        if self.hero.getZ() > 1 and self.mode:
            self.hero.setZ(self.hero.getZ() - 1)

    def turnLeft(self):
        self.hero.setH((self.hero.getH()+5) % 360)

    def turnRight(self):
        self.hero.setH((self.hero.getH()-5) % 360)

    def accept_events(self):
        base.accept('n', self.turnLeft)
        base.accept('n-repeat', self.turnLeft)
        base.accept('m', self.turnRight)
        base.accept('m-repeat', self.turnRight)
        base.accept('c', self.changView)
        base.accept('w', self.forward)
        base.accept('w-repeat', self.forward)
        base.accept('s', self.forwardBack)
        base.accept('s-repeat', self.forwardBack)
        base.accept('a', self.forwardLeft)
        base.accept('a-repeat', self.forwardLeft)
        base.accept('d', self.forwardRight)
        base.accept('d-repeat', self.forwardRight)

        base.accept('q', self.up)
        base.accept('q-repeat', self.up)

        base.accept('e', self.down)
        base.accept('e-repeat', self.down)

        base.accept('z', self.changeMode)