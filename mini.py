import random

w, h, mines  = 10, 5, 3


#gene field
field=[[0 for y in range(h)]for x in range (w)]
if mines > w * h:
  mines=0
  print(" Error: too many mines")
for i in range(mines):
    while True:
     rx = random.randint(0, w - 1)
     ry = random.randint(0, h - 1)
     if field[rx][ry] != "M":
      field[rx][ry] = "M"
     break

deltas=((-1,-1),(0,-1),(1,-1), (-1,0),(1,0),(-1,1),(0,1),(1,1))
for y in range(h):
      for x in range (w):
         if field[x][y]=="M":
        
          #print("mina na [{},{}]".format (x,y))
          for delta in deltas:
             nx = x + delta[0]
             ny = y + delta[1]
             if nx >= 0 and nx<w and ny >= 0 and ny< h and field [nx][ny] !="M":
                field[nx][ny] +=1
           
            
        
            
for y in range (h):
    for x in range (w):
      print(field[x][y], end='')
    print() 
    






