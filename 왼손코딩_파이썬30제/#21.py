def checkio(pw):
    if len(pw) < 10:
        # print("글자 수 부족")
        print("False")
        return
    cond_upper = 0
    cond_lower = 0
    cond_num = 0
    for i in range(0, len(pw)):
        if pw[i].isupper() == True:
            cond_upper += 1
        if pw[i].islower() == True:
            cond_lower += 1
        if pw[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            cond_num += 1

    cond_list = [cond_upper, cond_lower, cond_num]
    # print(cond_list)
    for j in cond_list:
        if j == 0:
            # print("조건 미충족")
            print("False")
            return
        else: 
            pass
    
    print("True")
    return


checkio("A1213pokl")
checkio("bAse730onE")
checkio("ascascascascasc")
checkio("QWERTYqwerty")
checkio("123ABCabdcbd")

print("#"*100)
# 정답

def checkio_answer(data):
    if len(data) < 10:
        print("False")
        return
    if data.upper() == data :
        print(False)
        return
    if data.lower() == data:
        print(False)
        return
    print(any(c.isdigit() for c in data))
    return

checkio_answer("A1213pokl")
checkio_answer("bAse730onE")
checkio_answer("ascascascascasc")
checkio_answer("QWERTYqwerty")
checkio_answer("123ABCabdcbd")


