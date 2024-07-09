def find_palindrome(digits):
    # Generate the largest number with the given number of digits
    max_num = int('9' * digits)
    min_num = 10 ** (digits - 1)
    max_palindrome = 0
    max_factors = (0, 0)

    for i in range(max_num, min_num - 1, -1):
        # Early exit if product of i with itself is smaller than current max_palindrome
        for j in range(i, min_num - 1, -1):
            product = i * j
            if product <= max_palindrome:
                # Since j is decreasing, further values of j will also yield smaller products
                break
            if str(product) == str(product)[::-1]:
                max_palindrome = product
                max_factors = (i, j)

    return max_palindrome, max_factors

def main():
    digits = 8  # Change this to the desired number of digits
    max_palindrome, max_factors = find_palindrome(digits)
    print("Largest palindrome:", max_palindrome)
    print("Factors:", max_factors)

main()
