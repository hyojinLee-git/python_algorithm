while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    if a <= 200:
        use = a / 2
    elif 200 < a <= 29900:
        use = ((a - 200) / 3) + 100
    elif 29900 < a <= 4979900:
        use = ((a - 29900) / 5) + 10000
    else:
        use = ((a - 4979900) / 7) + 1000000

    me = use // 2
    end = 0
    while True:

        you = use - me
        if me <= 100:
            me_money = 2 * me
        elif 100 < me <= 10000:
            me_money = (me - 100) * 3 + 200
        elif 10000 <= me < 1000000:
            me_money = (me - 10000) * 5 + 29900
        else:
            me_money = (me - 1000000) * 7 + 4979900

        if you <= 100:
            you_money = 2 * you
        elif 100 < you <= 10000:
            you_money = (you - 100) * 3 + 200
        elif 10000 <= you < 1000000:
            you_money = (you - 10000) * 5 + 29900
        else:
            you_money = (you - 1000000) * 7 + 4979900

        if abs(you_money - me_money) == b:
            break
        elif abs(you_money - me_money) < b:
            end = me
            me = end // 2
        elif abs(you_money - me_money) > b:
            me += (end - me) // 2

    print(int(me_money))