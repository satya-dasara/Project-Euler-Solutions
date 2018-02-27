#Find the sum of factors of 3 and 5

sum=0
n=1000

for i in range(0,n):
    if (i%3==0 or i%5==0):
        sum+=i
        
print(sum)
