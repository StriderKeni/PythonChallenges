import datetime 

def time_delta(t1, t2):
    diff = t1 - t2
    return int(diff.total_seconds())

if __name__ == '__main__':

    arr_times = []

    for t_itr in range(int(input())):
        t1 = datetime.datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
        t2 = datetime.datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
        arr_times.append(time_delta(t1, t2))

    print("\n".join(str(x) for x in arr_times))