import pygame
 
pygame.init()

x=50
y=300
r=50
smer=1
y2=200
r2=40
smer2=1

w, h = 800, 600
window = pygame.display.set_mode((w, h))
pygame.display.set_caption("hra koule")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0, 0, 0))

    x += smer * 0.2
    if x < r or x > w - r:
       smer*=-1         
    pygame.draw.circle(window, (150, 50, 200), (x, y), r)


    y2 += smer2 * 0.2
    if y2 < r2 or y2 > h - r2:
       smer2 *= -1          
    pygame.draw.circle(window, (100, 225, 5), (300, y2), r2)


    

    pygame.display.update()

