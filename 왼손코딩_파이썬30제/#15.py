def checkio(num):
    k = 1
    num = str(num)
    for i in range(0, len(num)):
        if num[i] == "0":
            print(1)
            return
        k = k*int(num[i])
    print(k)
    return

checkio(828)
checkio(1245)
        

# 정답
def checkio_answer(num):
    res = 1
    for d in str(num):
        if int(d):
            res *= int(d)
    print(res)
    return

checkio_answer(828)
checkio_answer(10245)














