def count_words(sentence, wordlist):
    wordlist = list(wordlist)
    sentence = sentence.lower()
    cnt = 0
    for i in range(len(wordlist)):
        if wordlist[i] in sentence:
            cnt += 1
    print(cnt)

count_words("How are jihlsf you?", {"how", "are", "you", "hello"})
count_words("Bananas, give me bananas!", {"banana", "bananas"})
count_words("Lorem ipsum sit ampy, conces lseidf lsei elit", {"sum", "hamlet", "infinity", "anything"})

# 정답 코드
def count_words_answer(text, words):
    result = 0
    for word in words:
        if word in text.lower():
            result += 1
        
    return result




