lst = [3, 30, 34, 5, 9]
lst = list(map(str, lst))


# 303 330
# 같은 자릿수면 큰수인데
# 3393<3933
# 3312>3123
# 2252<2522

def digit(a, b):
    if len(a) == len(b):
        return True
    else:
        return False


def first_max(lst):
    _max = lst[0][0]
    num = lst[0]
    global same
    for i in range(len(lst)):
        if lst[i][0] > _max:
            _max = lst[i][0]
            num = lst[i]
        elif lst[i][0] == _max:
            same.add(lst[i])
    print(same)
    # same=list(same)
    return num


answer = ''
same = set()

while lst:
    # print(lst)
    num = first_max(lst)
    if num is None:
        continue
    else:
        answer += num
        lst.remove(num)
print(answer)





