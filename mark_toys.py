def maximumToys(prices, k):
    sprices = sorted(prices)
    buys = 0

    for i in range(len(sprices)):
        if sprices[i] <= k and k >= 0:
            k = k - sprices[i]
            buys += 1
        else:
            return buys


if __name__ == "__main__":

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))

    print(maximumToys(prices, k))
