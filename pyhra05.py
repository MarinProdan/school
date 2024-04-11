import pygame


pygame.init()


width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hra")

x1 = 50  
x2 = 50  
direction = 1  
r = 50  
ball1 = {"x": 200, "y": 200, "r": 50}
ball = {"x": 300, "y": 300, "r": 50} 
vector = {"dx": -0.2, "dy": 0.3}  
vector1 = {"dx": -0.2, "dy": 0.2}  


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))



    ball["x"] += vector["dx"]
    ball["y"] += vector["dy"]
    if ball["x"] < r or ball["x"] > width - r:
        vector["dx"] *= -1
    if ball["y"] < r or ball["y"] > height - r:
        vector["dy"] *= -1
    pygame.draw.circle(window, (255, 255, 0), (ball["x"], ball["y"]), ball["r"])

   

    ball1["x"] += vector1["dx"]
    ball1["y"] += vector1["dy"]
    if ball1["x"] < r or ball1["x"] > width - r:
        vector1["dx"] *= -1
    if ball1["y"] < r or ball1["y"] > height - r:
        vector1["dy"] *= -1
    pygame.draw.circle(window, (200, 55, 100), (ball1["x"], ball1["y"]), ball1["r"])

    distance = ((ball1["x"] - ball["x"]) ** 2 + (ball1["y"] - ball["y"]) ** 2) ** 0.5
    if distance <= ball1["r"] + ball["r"]:
        vector1["dx"], vector["dx"] = vector["dx"], vector1["dx"]
        vector1["dy"], vector["dy"] = vector["dy"], vector1["dy"]
   
    pygame.display.update()

pygame.quit()


