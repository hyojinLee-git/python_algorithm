from itertools import permutations
import copy


def solution(expression):
    num = ''
    lst = []
    for e in expression:
        if e.isdigit():
            num += e
        else:
            lst.append(num)
            lst.append(e)
            num = ''
    lst.append(num)
    print(lst)
    per = list(permutations(['*', '-', '+'], 3))
    arr = []
    for p in per:
        temp = copy.deepcopy(lst)
        for i in range(3):
            j = -1
            while len(temp) != 1:
                j += 1

                if temp[j] == p[i]:
                    num = str(eval(temp[j - 1] + temp[j] + temp[j + 1]))
                    del temp[j - 1:j + 2]
                    temp.insert(j - 1, num)
                    print(temp)
                    j = -1

                if j >= len(temp) - 1:
                    break
        arr.append(abs(int(temp[0])))

    return max(arr)