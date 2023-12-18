import random

w, h, mines = 10, 6, 6
# gene empty field
field = [[0 for y in range(h)] for x in range(w)]
# put mine on random position
mine_count = 0
while mine_count < mines:
    rx = random.randint(0, w - 1)
    ry = random.randint(0, h - 1)
    if field[rx][ry] != "M":
        field[rx][ry] = "M"
        mine_count += 1

    



# print field
for y in range(h):
    for x in range(w):
        print(field[x][y], end="")
    print()