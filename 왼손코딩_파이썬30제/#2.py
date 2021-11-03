def first_word(sentence):
    lst = sentence.split(' ')
    # print(lst[0])
    if "," in lst[0]:
        lst[0] = lst[0].replace(",", "")
    elif "." in lst[0]:
        lst[0] = lst[0].replace(".", "")
    print(lst[0])

#정답
def first_word_answer(text:str):
    text = text.replace('.', ' ').replace(',', ' ').strip()
    text = text.split()

    print(text[0])

a = 'ashe, is a boy'
first_word(a)
first_word_answer(a)













