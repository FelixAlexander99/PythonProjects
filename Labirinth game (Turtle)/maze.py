from pygame import *

#classes
#Creates sprites using rectangles
class Card(sprite.Sprite):
    def __init__(self,width,height,x,y,color):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    def draw(self):
        draw.rect(window, self.fill_color, self.rect)

#Creates sprites using images
class Pic(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture) , (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

#Modified image sprite class with movement options
class Player(Pic):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        #Checking collisions to the right
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        #Checking collisions to the left
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)

        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        #Checking collisions going down
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        
    def fire(self):
        bullet = Bullet(bullet_img, self.rect.right, self.rect.centery, 15, 20, 15)
        bullets.add(bullet)

#Modified image sprite class with automatic movement
class Enemy(Pic):
    def __init__(self, picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed
    #Enemy moves along X axis from 400-600
    def update(self):
        if self.rect.x <= 400:
            self.direction = "right"
        if self.rect.x >= 600:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    
class Bullet(sprite.Sprite):
    def __init__(self, picture,x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 750:
            self.kill()
        sprite.groupcollide(barriers, bullets, False, True)
        sprite.groupcollide(enemies, bullets, True, True)

#colors
back = (120, 120, 255)
GREEN = (0, 255, 0)

#Main window setup
window = display.set_mode((700,500))
window.fill(back) 
display.set_caption("Labirynth")

#Conditions
run = True
finish = False

#Images
wall_img = "wall.png"
monster_img = "monster.png"
bullet_img = "bullet.png"
player_img = "ghost.png"
finish_img = "finish.png"
background = "background.jpg"
win_screen = "win.jpg"

#object creation
objects = list()
objects.append(Pic(background, 700, 500, 0, 0))
objects.append(Pic(wall_img,   80, 400, 300, 100))
objects.append(Pic(wall_img,   200, 80, 370, 240))
objects.append(Pic(finish_img, 50, 50, 450, 400))

player = Player(player_img, 80, 80, 100, 250, 0, 0)
enemy = Enemy(monster_img, 60, 70, 600, 100, 5)
win = Pic(win_screen, 700, 500, 0, 0)

#Adding walls to group
barriers = sprite.Group()
barriers.add(objects[1])
barriers.add(objects[2])

#Creating bullet group
bullets = sprite.Group()

#Creating enemy group
enemies = sprite.Group()
enemies.add(enemy)

#game loop 
while run:
    #Event handling
    #Verificare daca se iese din program (cu X)
    for e in event.get():
        if e.type == QUIT:
            run = False
        #Player movement
        #Key press
        elif e.type == KEYDOWN:
            #Up Arrow
            if e.key == K_UP:
                player.y_speed = -5
            #Down Arrow
            elif e.key == K_DOWN:
                player.y_speed = 5
            #Left Arrow
            elif e.key == K_LEFT:
                player.x_speed = -5
            #Right Arrow
            elif e.key == K_RIGHT:
                player.x_speed = 5
            #Shooting
            elif e.key == K_SPACE:
                player.fire()
        #Key release
        elif e.type == KEYUP:
            #Up Arrow release
            if e.key == K_UP:
                player.y_speed = 0
            #Down Arrow release
            elif e.key == K_DOWN:
                player.y_speed = 0
            #Left Arrow release
            elif e.key == K_LEFT:
                player.x_speed = 0
            #Right Arrow release
            elif e.key == K_RIGHT:
                player.x_speed = 0

    #Check if game was finished
    if finish != True:
        #Sprite & background display
        for object in objects:
            object.reset()
        #Showing player and updating position    
        player.reset()
        player.update()
        #Showing and moving enemy
        enemies.update()
        enemies.draw(window)
        #Showing bullets
        bullets.update()
        bullets.draw(window)
        #Collision handling
        #Check if game finished
        if sprite.collide_rect(player, objects[3]):
            finish = True
            win.reset()

    #Delay & update window
    time.delay(50)        
    display.update()