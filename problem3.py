from math import sqrt

def isPrime(num):
    for x in range(2,int(sqrt(num))+1): #biggest divisor it can be is sqrt(num)
        if num%x==0:
            return False
    return True

num = 600851475143;
largest = 0;
for x in range(2, int(sqrt(num))+1): # the largest can only be up to sqrt(x)
    if isPrime(x): # Needs to be prime
        if num%x==0: # Needs to be a factor of our given number
            if x > largest: # Check if it's the largest prime factor
                largest = x

print(f"Largest prime is {largest}")
