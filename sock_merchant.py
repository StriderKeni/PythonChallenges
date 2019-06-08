from collections import Counter


def pairs():
    n = int(input())
    ar = Counter(list(map(int, input().rstrip().split())))
    result = sum([v//2 for k, v in ar.items() if v > 1])

    return result


if __name__ == "__main__":

    print(pairs())
