def checkio(array):
    print(sorted(array, key = abs))
    return

k = [-3, 5, -4, 6, -10, 9]
checkio(k)


# 정답
def checkio_answer(array):
    print(tuple(sorted(array, key = abs)))
    return

checkio_answer(k)





