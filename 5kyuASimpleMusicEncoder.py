def add_to_result(res, rve, st, abs_int):
    if st == 1:
        res.append(f"{rve.pop(0)}")
    elif st == 2:
        res.append(f"{rve[-1]}*{len(rve)}")
    elif st == 3:
        if abs_int == 1:
            res.append(f"{rve[0]}-{rve[-1]}")
        else:
            res.append(f"{rve[0]}-{rve[-1]}/{abs_int}")
    return


def compress(raw):
    # State  1: no pattern candidate now, 2: sequence two, 3: sequence 3
    state = 1
    result = []
    reserve = []
    for n in raw:
        if state == 1:
            reserve.append(n)
            if len(reserve) == 2:
                if reserve[0] == reserve[1]:
                    state = 2
                else:
                    interval = reserve[1] - reserve[0]
            elif len(reserve) == 3:
                if reserve[2] == reserve[1]:
                    add_to_result(result, reserve, state, abs(interval))
                    state = 2
                elif reserve[2] - reserve[1] == interval:
                    state = 3
                else:
                    add_to_result(result, reserve, state, abs(interval))
                    interval = reserve[1] - reserve[0]
            else:
                interval = 0

        elif state == 2:
            if n == reserve[-1]:
                reserve.append(n)
            else:
                add_to_result(result, reserve, state, abs(interval))
                reserve = [n]
                state = 1
        elif state == 3:
            if n - reserve[-1] == interval:
                reserve.append(n)
            else:
                add_to_result(result, reserve, state, abs(interval))
                reserve = [n]
                state = 1

    if state == 1:
        for x in reserve:
            result.append(f"{x}")
    else:
        add_to_result(result, reserve, state, abs(interval))

    return ",".join(result)


print(compress([0, 2, 4, 5, 7, 6, 5, 5, 5, 5, 5])) # "0-4/2,5,7-5,5*4"
print(compress([1, 1, 2, 3, 4, 5, 7, 9]))
print(compress([1,2,2,3])) # "1,2*2,3
print(compress([1,3,4,5,7])) # "1,3-5,7"
print(compress([1,5,4,3,7])) # "1,5-3,7"
print(compress([1,10,8,6,7])) # "1,10-6/2,7"
