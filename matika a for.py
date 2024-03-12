numbers=[4,8,3,1,2,5,6]
print(numbers)
for i in range(len(numbers)-1):
    if numbers[i]>numbers[i+1]:
        #numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
        tmp = numbers[i]
        numbers[i] = numbers[i+1]
        numbers[i+1] = tmp
print(numbers)

import math
player = [2,5]
enemy= [3,3]

a=abs(player[0] - enemy[0])
b=abs(player[1] - enemy[1])
c=math.sqrt (a**b + b**2)
print(c)
