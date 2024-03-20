def cnt_sum(start,count):
    if start % 2 ==0:
        start+=1
    sum=0
    n= start
    while n <start +(count * 2):
        sum+= n 
        n+=2
    return sum
print(cnt_sum (3,4))
