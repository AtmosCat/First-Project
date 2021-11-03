def median(words):
    words = sorted(words)
    if len(words)/2 == 1:
        print(words[int(len(words)/2+0.5)])
        return
    else:
        print(words[int(len(words)/2)])
        return


median([1,2,3,4,5])
median([2,3,4,1,5])
median([1,300,2,344,500])

# 정답
def median_answer(data):
    data.sort()
    half = len(data) // 2

    print((data[half] + data[-half-1]) / 2)
    return