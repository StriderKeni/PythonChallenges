import math

def isPrime(num):
    sq = int(math.sqrt(num))

    if num == 1:
        return "Not prime"

    for i in range(2, sq+1):
        if num%i==0:
            return "Not prime"
    return "Prime"


if __name__ == '__main__':
    t = int(input())
    arr = []

    for i in range(t):
        arr.append(int(input()))

    for i in arr:
        print(isPrime(i))