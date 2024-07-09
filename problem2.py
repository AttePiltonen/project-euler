def sum_even_fibonacci(limit):
    a, b = 1, 2
    sum_even = 0

    while a <= limit:
        if a % 2 == 0:
            sum_even += a
        a, b = b, a + b

    return sum_even

def main():
    limit = 4_000_000
    print(sum_even_fibonacci(limit))

if __name__ == '__main__':
    main()