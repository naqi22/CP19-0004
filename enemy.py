class enemy(object):
    walkRight = [pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/R1E.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/R2E.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/R3E.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/R4E.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/R5E.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/R6E.png')))]
    walkLeft = [pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/L1E.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/L2E.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/L3E.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/L4E.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/L5E.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/L6E.png')))]
    attackRight = [pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/AER1.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/AER2.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/AER3.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/AER4.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/AER5.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/AER6.png')))]
    attackLeft = [pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/AEL1.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/AEL2.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/AEL3.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/AEL4.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/AEL5.png'))), pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/AEL6.png')))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = velocity
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.attack=False

    def draw(self,win):
        if self.x  > 1616 + level.currentpos:
            self.y = 400
        else:
            self.y = 300

        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0 and self.x < man.x:
                if self.attack:
                    win.blit(self.attackRight[self.walkCount//3], (self.x,self.y))
                else:
                    win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                
                self.walkCount += 1
                
            else:
                if self.attack:
                    win.blit(self.attackLeft[self.walkCount//3], (self.x,self.y))
                else:
                    win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))

                self.walkCount += 1
                
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 50, self.y + 10, 31, 90)
            #pygame.draw.rect(win, (255,0,0),  (self.x + 50, self.y + 10, 31, 90))
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel < 0:
            if (self.x + self.width) > man.x:
                self.vel = (velocity * -1) / 2
            else:
                self.vel = velocity / 2
        else:
            if (self.x - self.width) > man.x:
                self.vel = (velocity * -1) / 2
            else:
                self.vel = velocity / 2

        self.x += self.vel

        if self.x < man.x + man.width:
            self.attack=True
            attackSound.play()
        
    def hit(self):in
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            self.x=screenwidth
            self.health=10
            self.visible=True
            self.attack=False