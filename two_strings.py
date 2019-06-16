import os


def twoStrings(s1, s2):

    s1_arr = [i for i in s1]
    s2_arr = [i for i in s2]

    for i in s1:
        if i in s2:
            return True
    return False


if __name__ == "__main__":

    n = int(input())

    for _ in range(n):

        s1 = input()
        s2 = input()

        result = twoStrings(s1, s2)
        print(result)
