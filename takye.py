cisla = [23,3,14,11,25,65,8,3,65,0]
bee = 0

for i in cisla:
    if(i>bee):
        bee = i
x=[i for i in cisla if i==bee]
print("Největší číslo je",bee,"a objevi se",len(x),"krat")