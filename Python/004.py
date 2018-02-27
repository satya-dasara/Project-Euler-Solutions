#Find the largest 6 Digit Palindrome which is the product of two 3 digit numbers

n,n1=2,3
mul_11=[i for i in range(10**n,10**n1) if i%11==0]

empty=[]
for i in range(10**n,10**n1):
    empty.append(list(map(lambda x: x*i,mul_11)))
for i in range(0,len(empty)):
    empty[i]=list(filter(lambda x: str(x)==str(x)[::-1],empty[i]))

flat=[i for k in empty for i in k]
print(max(flat))
