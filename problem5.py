import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def divisible(limit):
    multiple = 1
    for i in range(1, limit + 1):
        multiple = lcm(multiple, i)
    return multiple

def main():
    limit = 20
    print(divisible(limit))

main()
