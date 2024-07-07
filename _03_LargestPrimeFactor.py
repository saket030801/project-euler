import math

n = 600851475143

n = math.ceil(math.sqrt(n))




def isPrime(number):
    i=2
    while i<=math.ceil(math.sqrt(number)):
        if number%i==0:
            return False
        i+=1

    return True


number = n
n=600851475143
while number > 0:
    if n % number == 0 and isPrime(number):
        print(number)
        break
    number-=1