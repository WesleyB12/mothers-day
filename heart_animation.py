import pygame,math
pygame.init()
screen=pygame.display.set_mode((1920,1080))
running=True
screen.fill((255,255,255))
heartcurve=(960,700)
movement=0
clock=pygame.time.Clock()
font=pygame.font.SysFont('Comic Sans MS',90)
while running:
    movement+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                running=False
    if movement<(900):
        heartcurve=(960+movement-((movement/30)**2),700-movement+((movement/110)**3))   
        pygame.draw.circle(screen,(220,50,50),heartcurve,30)
        pygame.draw.circle(screen,(220,50,50),(1920-heartcurve[0],heartcurve[1]),30)
    else:
        screen.blit(font.render('Happy Mothers day! :)',False,(0,0,0)),(400,700))
    clock.tick(180)
    pygame.display.flip()
pygame.quit()