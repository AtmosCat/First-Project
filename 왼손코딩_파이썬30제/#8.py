def checkio(num):
    if num % 3 == 0 and num % 5 != 0 :
        print("Fizz")
    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    else:
        print(num)

checkio(6)
checkio(10)
checkio(15)
checkio(7)

# 정답 동일
















