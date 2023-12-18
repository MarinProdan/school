cisla = [23,3,14,11,25,65,8,3,65,0]
max = 0
biggest = 0
existuje = 0

for x in cisla:
    if (x>max):
        max = x
        biggest = max
    
for a in cisla:
    if(biggest == a):
        existuje += 1

print(max, existuje)