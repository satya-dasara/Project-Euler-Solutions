#Sum of all even Fibonacci numbers

y,x=0,0
final=[0,]
sum1=0
while x<=4000000:
    if x==0:
        x,y=y,x+1
        final.append(y)
        continue
    if x==1:
        x,y=y,x+y
        final.append(y)
        if(y%2==0):
            sum1+=y
        continue
    x,y=y,x+y
    if(y%2==0):
        sum1+=y
    final.append(y)
print(sum1)
