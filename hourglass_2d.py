"""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
"""


def hourglassSum(arr):

    max = -999999  # for test case 3 and 5
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            middle = arr[i+1][j+1]
            first = sum(arr[i][j:j+3])
            last = sum(arr[i+2][j:j+3])

            print(f"{first}\n{middle}\n{last}")
            total = (first + middle + last)

            max = total if max < total else max

    return max


if __name__ == "__main__":

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(hourglassSum(arr))
