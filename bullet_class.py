class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing 

    def draw(self,win):
        win.blit(bullet_bg, (self.x,self.y))