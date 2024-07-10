import math

def sieve(n):
    A = [True] * (n + 1)
    A[0] = A[1] = False  # 0 and 1 are not primes

    for i in range(2, int(math.sqrt(n)) + 1):
        if A[i]:
            for j in range(i**2, n + 1, i):
                A[j] = False

    return [i for i in range(2, n + 1) if A[i]]

def getNthPrime(n):
    if n < 1:
        raise ValueError("n must be a positive integer")

    # Initial upper bound estimation
    s = 2 * n
    while True:
        primes = sieve(s)
        if len(primes) >= n:
            return primes[n - 1]
        s *= 2  # Double the upper bound and try again if not enough primes are found

def main():
    n = 1000000
    print(f"The {n}th prime number is: {getNthPrime(n)}")

main()
