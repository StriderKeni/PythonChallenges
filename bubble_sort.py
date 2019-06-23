def countSwaps(a):
    temp = 0
    swaps = 0
    while a != sorted(a):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i+1]
                a[i+1] = a[i]
                a[i] = temp
                swaps += 1
            else:
                continue
    return swaps, a[0], a[-1]


if __name__ == "__main__":

    n = int(input())

    a = list(map(int, input().rstrip().split()))
    print(countSwaps(a))
