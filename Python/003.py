#Find the largest prime factor of a number

from math import sqrt

def prime_factor(n):
    k=[]
    flag=True
    n1=n
    for f in range(2,int(sqrt(n))+1): 
        if int(n1%f):
            continue
        else:
            k.append(f)
            n1=n1/f
        if f>=n:
            break
    return max(k)
        
        
print(prime_factor(600851475143))
