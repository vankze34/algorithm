def solution(priorities, location):
    order = list()
    out_order = [0] * (len(priorities))
    cnt = 1

    for i in range(len(priorities)):
        order.append(i)

    print(order)
    print(priorities)
    print(out_order)
    print("")
    while True:
        now_p = priorities.pop(0)
        now_o = order.pop(0)
        
        if now_p >= max(priorities):
            priorities.append(0)
            out_order[now_o] = cnt
            cnt += 1
        else:
            priorities.append(now_p)

        order.append(now_o)

        print("o  : ", order)
        print("p  : ", priorities)
        print("out: ", out_order, "fixed")
        print("")

        if min(out_order)>0:
            break

    return out_order[location]

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))