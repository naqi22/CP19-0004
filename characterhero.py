class player(object):
    walkRight = [pygame.image.load(root+'images/CR1.png'), pygame.image.load(root+'images/CR2.png'), pygame.image.load(root+'images/CR3.png'), pygame.image.load(root+'images/CR4.png'), pygame.image.load(root+'images/CR5.png'), pygame.image.load(root+'images/CR6.png')]
    walkLeft = [pygame.image.load(root+'images/CL1.png'), pygame.image.load(root+'images/CL2.png'), pygame.image.load(root+'images/CL3.png'), pygame.image.load(root+'images/CL4.png'), pygame.image.load(root+'images/CL5.png'), pygame.image.load(root+'images/CL6.png')]

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = velocity
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if level.currentpos < (self.x+1616) * -1 and not self.isJump:
            self.y = 450
        elif level.currentpos > (self.x+1616) * -1 and not self.isJump:
            self.y = 350

        if self.walkCount + 1 >= 18:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            else:
                win.blit(self.walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 100
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()