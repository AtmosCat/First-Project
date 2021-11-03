from typing import Dict


def popular_words(txt, txt_list):
    txt = txt.lower()
    word_list = txt.split(" ")

    word_dict = {}
    for i in txt_list:
        cnt = word_list.count(i)
        word_dict[i] = cnt
        if i not in word_list:
            word_dict[i] = 0
    
    print(word_dict)

popular_words(" When I was One I has just begun When I was Two I was nearly new", ['i', 'was', 'three', 'near'])


# 정답
 
def popular_words_answer(txt, words):
    txt = txt.lower()
    splitted_words = txt.split()
    answer = {}

    for word in words:
        answer[word] = splitted_words.count(word)

    print(answer)

popular_words_answer(" When I was One I has just begun When I was Two I was nearly new", ['i', 'was', 'three', 'near'])













