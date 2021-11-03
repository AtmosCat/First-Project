def checkio(numlist):
    max_num = max(numlist)
    min_num = min(numlist)
    diff = max_num - min_num 
    print(diff)

checkio([1, 2, 3])
checkio([5, -5])
checkio([10.1, -2.2, 1.1, 0.5])


# 정답
def checkio_answer(*args):      # *args : 개수 상관없이 받아옴
    if args:
        print(max(args) - min(args))
    else:
        print("")

checkio_answer(1, 2, 3)
checkio_answer(5, -5)
checkio_answer(10.1, -2.2, 1.1, 0.5)













