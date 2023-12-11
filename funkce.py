#def hello(n):
 #   print("hello " * n)

#hello(5)


def hello_str(n):
    return



#def abs(n):
    if n< 0:
        n= n * -1
        #n *= -1
        return n
#print(abs (-65) +5)      
   
     
def max (x, y):
    if x > y:
        return x
    #else:
    return y
        #max==y          
 

def amount(proc, total):
 #return proc *(100-total) * 0.01           
 return total/100 * proc 

print(amount(30, 450))


#def money (deposit, monthly_income ,tax, years):
   #money += 12 * monthly_income
  # money += money/100 * tax
 #  return 
#print(str(int(money(20000,500,5,20))))




def fact(n):
    if n < 2:
        return 1
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact

print(fact(3))