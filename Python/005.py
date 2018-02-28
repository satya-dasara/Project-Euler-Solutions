# Least smallest multiple of n numbers 

# You can always create the list and brute force it.

# This algorithm finds the max power for each prime number to find the LCM.

n=20

numbers=[i for i in range(2,n+1)]
numbers1=numbers

total=set(numbers)
set1=set()
set1_noprimes=set()
set2=set()
key={}

for i in numbers1:
    for j in numbers1[0:numbers1.index(i)]:
        if i%j==0:
            set1.add(j)
            set1_noprimes.add(i)
            
set2=total-set1

primes=set1^(set1_noprimes^set2)

prime_dic={}
for i in primes:
    prime_dic[i]=0
    
count=0
for i in primes:
    for j in numbers:
        count=0
        if j%i==0:
            trial=j
            while not(trial%i):
                count+=1
                trial/=i
            if prime_dic[i]<count:
                prime_dic[i]=count

mul=1
for i in primes:
    mul*=i**prime_dic[i]

print(mul)


