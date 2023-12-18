import random

w, h, mines  = 10, 5, 8


#gene field
field=[[0 for y in range(h)]for x in range (w)]
  
for i in range(mines):
    while True:
     rx = random.randint(0, w - 1)
     ry = random.randint(0, h - 1)
     if field[rx][ry] != "M":
      field[rx][ry] = "M"
     break
for y in range (h):
    for x in range (w):
      print(field[x][y], end='')
    print() 
    






