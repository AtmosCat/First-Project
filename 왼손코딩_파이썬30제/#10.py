def checkio(numlist):
    if len(numlist) == 0:
        print(0)
    sumthing = 0
    for i in range(0, len(numlist)):
        even_index = []
        if i % 2 == 0:
            even_index.append(i)
        for j in even_index:
            sumthing += numlist[j]
    lastnum = numlist[-1]
    print(sumthing * lastnum)


checkio([0, 1, 2, 3, 4, 5])
checkio([1, 3, 5])
checkio([6])
# checkio([])

#정답
def checkio_answer(array):
    if not array:
        print(0)
    
    print(sum(array[::2]) * array[-1])      #  ::2 에서 2 -> step 의미

checkio_answer([0,1, 2, 3, 4, 5])












