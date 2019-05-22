class level(object):
    bg = pygame.image.load(os.path.abspath(os.path.join(os.path.dirname(__file__),'images/bg.png')))

    def __init__(self,currentpos,levellength):
        self.currentpos = currentpos
        self.fulllength = fulllength
        self.vel = velocity
       
    def draw(self, win):
        win.blit(self.bg, (self.currentpos,0))
        #pygame.draw.rect(win, (255,0,0), self.hitbox2,2)
