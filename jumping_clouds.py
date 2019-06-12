# example
# 6
# 0 0 0 1 0 0


def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c)-3:
        i += 2 if c[i+2] == 0 else 1
        jumps += 1
    return jumps + 1


if __name__ == "__main__":

    n = int(input())

    c = list(map(int, input().strip().split()))

    print(jumpingOnClouds(c))
