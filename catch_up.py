from pygame import * 
from random import randint 
 
 
 
 
win_width = 500 
win_height = 500 
window = display.set_mode((win_width, win_height)) 
 
 
class GameSprite(sprite.Sprite): 
  
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (65, 65)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
  
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 


class Player(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 700 - 80: 
            self.rect.y += self.speed 
    def update2(self): 
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 700 - 80: 
            self.rect.y += self.speed 
fon = transform.scale(image.load("white.jpg"),(500,500)) 
plat = Player('pi.png', 5, win_width - 80,4) 
plat2 = Player('po.png', 435, win_width - 80,4) 
mach = transform.scale(image.load("balll.png"),(80,80)) 
 
 
 
 
 
 
run = True 
clock = time.Clock() 
FPS = 60 
while run: 
     
    for i in event.get(): 
        if i.type == QUIT: 
            run = False 
 
    mach.rect.x += speed_x
    mach.rect.y += speed_y

    window.blit(fon,(0,0))


    mach.reset()
    plat.update()
    plat.reset()
    plat2.update2()
    plat2.reset()    



    if mach.rect.y > win_height - 50 or mach.rect.y < 0:
        speed_y *= -1
        speed_x *= 1
    if mach.rect.y > win_height - -50 or mach.rect.y < 0:
        speed_y *= 1
        speed_x *= 1
    if sprite.collide_rect(plat,mach) or sprite.collide_rect(plat2,mach):
        speed_y *= 1
        speed_x *= -1


    if mach.rect.x >= 500:
        window.blit(smert,(250,0))
        mach.rect.y = 250
        mach.rect.x = 250


    if mach.rect.x <= -0:
        window.blit(smert,(0,0))
        mach.rect.y = 250
        mach.rect.x = 250
        
 
    display.update() 
    clock.tick(FPS)