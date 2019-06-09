# Sample
# 12
# DDUUDDUDUUUD


def countingValleys(n, s):
    count = 0
    valleys = 0

    for i in s:

        if i == "U":
            count += 1
        elif count == 0 and i == "D":
            valleys += 1
            count -= 1
        else:
            count -= 1

    return valleys


if __name__ == "__main__":

    n = int(input())
    s = input()

    print(countingValleys(n, s))
