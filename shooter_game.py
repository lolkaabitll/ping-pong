

from pygame import * 
from random import randint 
from time import time as timer



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


class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = Rect(x, y, width, height) #прямоугольник
      self.fill_color = color
  def color(self, new_color):
      self.fill_color = new_color
  def fill(self):
      draw.rect(window, self.fill_color, self.rect)
  def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)      
'''класс надпись'''
class Label(Area):
  def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
  def draw(self, shift_x=0, shift_y=0):
      self.fill()
      window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
class Enemy(GameSprite):
   direction = "left"
   def update(self):
       if self.rect.x <= 470:
           self.direction = "right"
       if self.rect.x >= win_width - 85:
           self.direction = "left"

       if self.direction == "left":
           self.rect.x -= self.speed
       else:
           self.rect.x += self.speed

fon = transform.scale(image.load("fon.jpg"),(500,500)) 
racket = Player('pi.png', 5, win_width - 80,4) 
racket2 = Player('po.png', 435, win_width - 80,4) 
ball = Player('balll.png',80,80,win_width - 34) 
smert = transform.scale(image.load("red.jpg"),(250,500))
score = 0 
lost = 0
font.init()
font = font.Font(None,35)
win = font.render("you win ",True,(255,215,0))
lose = font.render("you lose",True,(5,105,60))

text = font.render("Cчет: "+ str (score),1,(222,222,0))
window.blit(fon,(0,0))
window.blit(text,(10,20))
finish = False
speed_x = 3
speed_y = 2
run = True 
clock = time.Clock() 
FPS = 60 
while run: 

    for i in event.get(): 
        if i.type == QUIT: 
            run = False 

   

    window.blit(fon,(0,0))
    



    if finish != True:
        window.blit(fon,(0, 0))
         
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if score >= 5:
            window.blit(fon,(0,0))
            window.blit(win,(225,200))
            
        


        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
            speed_x *= 1
        if ball.rect.y > win_height - -50 or ball.rect.y < 0:
            speed_y *= 1
            speed_x *= 1
        if sprite.collide_rect(racket,ball) or sprite.collide_rect(racket2,ball):
            speed_y *= 1
            speed_x *= -1
        if ball.rect.x >= 500:
            window.blit(smert,(250,0))
            ball.rect.y = 250
            ball.rect.x = 250
        if ball.rect.x <= -0:
            window.blit(smert,(0,0))
            ball.rect.y = 250
            ball.rect.x = 250
        ball.reset()
        racket.update()
        racket.reset()
        racket2.update2()
        racket2.reset()  
    if ball.rect.x >= 455:
        window.blit(lose,(200,200))
        window.blit(smert,(500,500))
    

        finish = True

    display.update() 
    clock.tick(FPS)