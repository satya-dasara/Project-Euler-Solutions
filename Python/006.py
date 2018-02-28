# Difference of Square of sum of n numbers and their sum of individual squares

dic1={}
n=100
for i in range(1,n+1):
    dic1[i]=i**2

keys=list(dic1.keys())
values=list(dic1.values())

diff=(int(sum(keys))**2)-sum(values)

print(diff)

