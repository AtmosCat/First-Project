# 정답
def checkio_answer(str_number, radix):
    try:
        print(int(str_number, radix))
    except ValueError:
        print(-1)
        return

checkio_answer("AF", 16)
checkio_answer("101", 2)
checkio_answer("101", 5)
checkio_answer("Z", 36)
checkio_answer("AB", 10)









