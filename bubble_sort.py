def countSwaps(a):
    swaps = 0
    while a != sorted(a):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps += 1
            else:
                continue

    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))


if __name__ == "__main__":

    n = int(input())

    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
