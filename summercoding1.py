code='012345'
day='20190620'
data=["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]
def solution(code,day,data):
    answer = []
    data.sort(key=lambda x:int(x[-10:]))
    for d in data:
        _price, _code, _time = d.split(' ')
        if code == _code[-6:] and day == _time[-10:-2]:
            #print(_time[-10:-2], _code[-6:])
            answer.append(int(_price.split('=')[1]))
    return answer

print(solution(code,day,data))