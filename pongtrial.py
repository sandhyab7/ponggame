
import pygame

pygame.init()    #initialize




#initializing
xscr=600
yscr=500

player_A_score =0
player_B_score =0
screen = pygame.display.set_mode((600,500))  #(x(width),y(height))
black = (0,0,0)
white = (255,255,255)

Ax=520
Ay=250
Asizex=30
Asizey=100
Amove=0

Bx = 50
By =yscr/2
Bsizex = 30
Bsizey = 100
Bmove =0

ballx = int(xscr/2)
bally =int(yscr/2)
 
ballradius = 10
over = False

clock =  pygame.time.Clock()

ballspeed = 10
ballmovex = -ballspeed
ballmovey = -ballspeed



def writeToScreen(text,color,posx,posy):
                  text = str(text)
                  font = pygame.font.SysFont('arial',30)
                  textWrite = font.render(text,True,color)
                  screen.blit(textWrite,(posx,posy))




#game loop

while not over:
    screen.fill((white))  # changes background color
    pygame.draw.rect(screen, black, [Bx, By, Bsizex, Bsizey])
    pygame.draw.rect(screen, black, [Ax, Ay, Asizex, Asizey])
    pygame.draw.circle(screen, black, [ballx, bally], ballradius)
    writeToScreen(player_B_score, black, 200, 20)
    writeToScreen(player_A_score,black, 350, 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Bmove = -10
            if event.key == pygame.K_DOWN:
                Bmove =  +10
            if event.key == pygame.K_u:
                Amove =-10
            if event.key == pygame.K_d:
                Amove = +10;





        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
               Bmove = 0
            if event.key == pygame.K_DOWN:
               Bmove = 0
            if event.key == pygame.K_u:
               Amove = 0
            if event.key == pygame.K_d:
               Amove = 0




#game logic
    if By <= 0:
       By=0
    if By + Bsizey >=yscr:
       By =yscr - Bsizey
    if Ay <= 0:
       Ay=0
    if Ay +Asizey >= yscr:
        Ay =yscr - Asizey

#ball movement and score
    if ballx <=0:  #hitting playgoal
        ballmovex = +ballspeed
        player_A_score += 1
    if ballx >=xscr:  #hitting the computer
        ballmovex = -ballspeed
        player_B_score+= 1
    if bally <= 0:
        ballmovey = +ballspeed
    if bally >= yscr:
        ballmovey = -ballspeed


    if ballx <= Bx + Bsizex and ballx + ballradius >= Bx:
        if bally >= By  and bally + ballradius <= By +Bsizey:
            ballmovex = +ballspeed


#computer collision detection

    if ballx + ballradius >= Ax and ballx < Ax + Asizex:
         if bally >= Ay and bally + ballradius <= Ay + Asizey:
             ballmovex = -ballspeed

    By +=Bmove
    Ay += Amove
    ballx += ballmovex
    bally += ballmovey
    pygame.display.flip()  #updates the screen
    clock.tick(15)


pygame.quit()
quit()
