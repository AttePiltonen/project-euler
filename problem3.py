import math

def primeFactors(n):
    maxPrime = -1

    while n % 2 == 0:
        n /= 2
    
    maxPrime = 2
    
    # Now n must be odd. So skip every other number.
    # Find prime factors until n becomes prime or 1.

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n /= i
            maxPrime = i

    if n > 2:
        maxPrime = n
    
    return maxPrime

def main():
    print(primeFactors(600851475143))

main()