import pygame

pygame.init()

x=50
smer=1
r=50
c1=20
c2=50
c3=150

w,h= 800,600
window = pygame.display.set_mode((w,h))
pygame.display.set_caption("color change/ball")

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    window.fill((0,0,0))

    x+=smer*0.5
    if x > w - r or x < r:
        smer *= -1
        c1+=50
        if c1 >250:
            c1=250
       

    pygame.draw.circle(window, (c1,c2,c3),(x,300),50)

    pygame.display.update()
pygame.quit()  