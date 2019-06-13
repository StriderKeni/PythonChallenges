"""
7
1 3 5 2 4 6 7
"""


def minimumSwaps(arr):
    temp = 0
    swaps = 0
    sorted_arr = sorted(arr)
    while (sorted_arr != arr):
        for i in range(0, len(arr)):
            if arr[i] == i+1:
                continue
            else:
                temp = arr[arr[i]-1]
                arr[arr[i]-1] = arr[i]
                arr[i] = temp
                swaps += 1
            print(arr, temp)

    return swaps


if __name__ == "__main__":

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(minimumSwaps(arr))
