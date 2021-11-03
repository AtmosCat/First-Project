def all_the_same(words):
    indexx = []
    for i in range(len(words)-1):
        if words[i] == words[i+1]:
            indexx.append(0)
        else:
            indexx.append(1)
        if 1 in indexx:
            print(False)
            return
        else:
            print(True)
            return

all_the_same([1,1,1])
all_the_same([1,2,1])
all_the_same(['a','a','a'])


# 정답
def all_the_same_answer(elements):
    return len(set(elements)) <= 1    # set는 중복된 값들 제거했을 때 개수가 1 이하면 True일 것