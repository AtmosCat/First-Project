def find_message(txt):
    lst = txt.split()
    k = ""
    for i in lst:
         k += i[0].upper()
    print(k)

find_message("Hi, my name is Alex")


# 정답
def find_message_answer(txt):
    return ''.join(filter(str.isupper, txt))    











