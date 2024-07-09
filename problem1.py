def main(limit):

    sum = 0

    for i in range(1, limit):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i

    print(sum)

if __name__ == "__main__":
    main(1000)