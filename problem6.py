def main(n):
    sumSquares = n*(n+1)*(2*n+1)/6
    squareOfSum = (n*(n+1)/2)**2

    print(int(squareOfSum - sumSquares))

main(100)