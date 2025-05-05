import pygame
import random
import time


pygame.init()


window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('PennysColorGame')

cyan = (255,255,0)
deeppink = (255,20,147)
yellow = (0,255,255)

list_colorvalue = [cyan, deeppink, yellow]
list_colorname = ['Cyan', 'Pink', 'Gelb']

font = pygame.font.SysFont('Cooper Black', 40)
text_points = font.render('0 Punkte', False, (0,0,0))
playtime = font.render('30 s', False, (0,0,0))

randomnumber_background = random.randrange(0,3,1)
randomnumber_colorname = random.randrange(0,3,1)
randomnumber_colorvalue = random.randrange(0,3,1)

text_color = font.render(list_colorname[randomnumber_colorname],False,list_colorvalue[randomnumber_colorvalue])

running = True
clock = pygame.time.Clock()

rectangle = pygame.Surface((200,200))
pygame.draw.rect(rectangle, (255,255,255), rectangle.get_rect())

points = 0
starttime = time.time()
remaining_time = 30


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1 and randomnumber_background != randomnumber_colorname:
                points += 1
            elif event.button==3 and randomnumber_background != randomnumber_colorname:
                points += 1
            else:
                points -= 1
            randomnumber_background = random.randrange(0,3,1)
            randomnumber_colorname = random.randrange(0,3,1)
            randomnumber_colorvalue = random.randrange(0,3,1)
            text_color = font.render(list_colorname[randomnumber_colorname],False,list_colorvalue[randomnumber_colorvalue])
            text_points = font.render(str(points) + ' Points', False, (0,0,0))

    if remaining_time > 0:
        endtime = time.time()
        remaining_time = round(30 - (endtime - starttime), 1)
        playtime = font.render(str(remaining_time) + ' s', False, (0,0,0))
    else:
        playtime = font.render('0 s', False, (0,0,0))

    window.fill(list_colorvalue[randomnumber_background])

    window.blit(rectangle,(225,140))
    window.blit(text_color, (277, 225))
    window.blit(text_points, (232,400))
    window.blit(playtime, (275,40))

    pygame.display.flip()

    clock.tick(60)


pygame.quit()

    
            

        









