numbers=[4,5,8,7,1,-5,-6] 
cnt=0
for n in numbers:
    if n%2==1 and n<0:
        cnt+=1
print("pocet=",cnt)    
