##Question

# Write a program to print twin primes less than 1000. 
# If two consecutive odd numbers are both prime then they are known as twin primes

###### Solution

def prime(x):
    for i in range(2,x):
        if x%i==0:
            alp=False
            break 
    else:
        alp=True
    return alp
    
print("(2,3)")
for i in range(3,1000,2):
    if prime(i):
        if prime(i+2):
            print("({},{})".format(i,i+2))
        else:
            i+=4


