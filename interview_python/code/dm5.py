a = [1, 2, 3, 4, 5]


def cal_s(num):
    return num * num


res1 = map(cal_s, a)
res2 = [i for i in res1 if i > 10]
print(res2)
