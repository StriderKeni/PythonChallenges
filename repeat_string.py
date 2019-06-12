

def repeatedString(s, n):

    repeat = s.count("a") * int(n/len(s))
    rest = s[:n % len(s)].count("a")
    return repeat + rest


if __name__ == "__main__":

    s = input()
    n = int(input())

    print(repeatedString(s, n))
