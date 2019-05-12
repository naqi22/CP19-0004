import pygame

pygame.init()

screenwidth=957
screenheight=538
fulllength=8337
currentpos=0
velocity=10
gravity=9
win = pygame.display.set_mode((screenwidth,screenheight))

pygame.display.set_caption("ZomBers")
root='c:/Users/abid/Desktop/OwnGame/'


clock = pygame.time.Clock()



class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class level(object):
    bg = pygame.image.load(root+'images/bg.png')

    def __init__(self,currentpos,levellength):
        self.currentpos = currentpos
        self.fulllength = fulllength
        self.vel = velocity
       
    def draw(self, win):
        win.blit(self.bg, (self.currentpos,0))
        #pygame.draw.rect(win, (255,0,0), self.hitbox2,2)

class enemy(object):
    walkRight = [pygame.image.load('C:/Users/abid/Desktop/PyGame/R1E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/R2E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/R3E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/R4E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/R5E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/R6E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/R7E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/R8E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/R9E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/R10E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/R11E.png')]
    walkLeft = [pygame.image.load('C:/Users/abid/Desktop/PyGame/L1E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/L2E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/L3E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/L4E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/L5E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/L6E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/L7E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/L8E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/L9E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/L10E.png'), pygame.image.load('C:/Users/abid/Desktop/PyGame/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = velocity
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

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


def redrawGameWindow():
    level.draw(win)
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

level = level(0,fulllength)
man = player(0, 350, 107,107)
goblin = enemy(0, 410, 64, 64, screenwidth)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        
        if bullet.x < screenwidth and bullet.x > 0:
            bullet.x += bullet.vel*5
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width - 10), round(man.y + 35), 6, (0,0,0), facing))
        shootLoop = 1

    if keys[pygame.K_LEFT]:
        if  level.currentpos < 0 and man.x<=0:
            level.currentpos += velocity
            
        elif man.x>0:
            man.x -= velocity 
             
        man.left = True
        man.right = False
        man.standing = False
        if goblin.vel < 0:
            goblin.x-=velocity * 1.5
        
        
    elif keys[pygame.K_RIGHT]:
        if level.currentpos > -(fulllength-screenwidth):
            level.currentpos -= velocity
          
        elif man.x < (screenwidth-man.width):
            man.x += velocity 
            
        man.right = True
        man.left = False
        man.standing = False
        if goblin.vel > 0:
            goblin.x+=velocity * -1.5
        
    else:
        man.standing = True
        man.walkCount = 0
        #goblin.vel=goblin.vel / 2

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    
    redrawGameWindow()
pygame.quit()
