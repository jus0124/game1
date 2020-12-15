import pygame
import random
import sys
pygame.init()

try:
    pygame.joystick.init()    
    j = pygame.joystick.Joystick(0)
    j.init()
    print ("Enabled joystick: {0}".format(j.get_name()))
except pygame.error:
	 print ("no joystick found.")

def on_draw():
       while True: 
            jx = js.get_axis(0) 
            print('axis 0: '+ str(jx)) 
            window.clear() 

screen_width = 1180 
screen_height = 640 

WHITE = (255,255,255)
GREEN = (0, 255 ,0)
size = [screen_width,screen_height]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("이상한 이상한 게임?(게임은 아니지...)") 

x = 0
y = 0

ex = 0
ey = 0

rx = 0
ry = 0

distancex = 0
distancey = 0

lead_x=0
lead_y=0

gamepads = []


character = pygame.image.load("C:/Users/jus01/Desktop/rabbit.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

enemy = pygame.image.load("C:/Users/jus01/Desktop/cat.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

bush = pygame.image.load("C:/Users/jus01/Desktop/bush.png")
bush_size = bush.get_rect().size
bush_width = bush_size[0]
bush_height = bush_size[1]

clock= pygame.time.Clock()

running = True
count = 0

while running:   
    screen = pygame.display.set_mode(size)   
    clock.tick(10) 
    screen.fill(GREEN)
    block_size = 10
    
    if count == 0:
        ex = round(random.randrange(0,118))*10
        ey = round(random.randrange(0,64))*10

        rx = round(random.randrange(0,118))*10
        ry = round(random.randrange(0,64))*10
        
        count = 1
  
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:      
            running = False  

        
    screen.blit(character, (x, y))
    screen.blit(enemy, (ex, ey))
    screen.blit(bush, (rx, ry))



    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        x -= 10

    if key_event[pygame.K_RIGHT]:
        x += 10

    if key_event[pygame.K_UP]:
        y -= 10

    if key_event[pygame.K_DOWN]:
        y += 10

    if event.type == pygame.JOYAXISMOTION:
        if j.get_axis(0) >= 0.5:
            x += block_size
            y += 0
        if j.get_axis(0) <= -1:
            x += -block_size
            y += 0
        if j.get_axis(1) >= 0.5:
            x += 0
            y += block_size
        if j.get_axis(1) <= -1:
            x += 0
            y += -block_size



    if ex == x and ey == y :
        running = False
    else:
        if ex > x :
            ex -= 5
        elif x < ex :
            ex += 5
        
        if ey > y :
            ey -= 5
        elif y > ey :
            ey += 5

        if x == ex:
            if ey > y:
                ey -= 5
            elif y > ey:
                ey += 5

        if y == ey:
            if ex > x:
                ex -= 5
            elif x > ex:
                ex += 5
       



    if x < 0:
        x = 0
    elif x > screen_width - character_width:
        x = screen_width - character_width

    if y < 0 :
        y = 0
    elif y > screen_height - character_height:
        y = screen_height - character_height

    if x == rx and y == ry:
        count = 0



    
    pygame.display.update()

pygame.quit()