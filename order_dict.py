list2conv = ['Key1', 'Key2']
d_fromList = dict.fromkeys(list2conv)

for i in d_fromList:
    d_fromList[i] = [0, 0]

outList = []

print(d_fromList)

for i in range(0, 3):
    d_fromList['Key1'][0] = d_fromList['Key1'][0] + 10
    d_fromList['Key2'][1] = d_fromList['Key2'][1] + 20

    print(d_fromList)

    outList.append(d_fromList['Key1'])
    outList.append(d_fromList['Key2'])
    print(outList)


print(outList)
