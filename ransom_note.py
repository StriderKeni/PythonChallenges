from collections import Counter


def checkMagazine(magazine, note):

    check = (Counter(note) - Counter(magazine)) == {}
    return "Yes" if check else "No"

    #
    # for i in note:
    #     print(i)
    #     if i in magazine:
    #         magazine.remove(i)
    #         note.remove(i)


if __name__ == "__main__":

    mn = input().split()

    m = int(mn[0])
    n = int(mn[1])

    magazine = list(input().rstrip().split())
    note = list(input().rstrip().split())

    print(checkMagazine(magazine, note))
