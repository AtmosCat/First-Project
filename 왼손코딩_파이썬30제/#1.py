# 내 풀이
def correct_sentence(sentence):
    sent_list = sentence.split(" ")
    # print(sent_list)
    sent_list[0] = sent_list[0].capitalize()
    # print(sent_list[len(sent_list) - 1])
    if "." not in sent_list[len(sent_list) - 1]:
        sent_list[len(sent_list) - 1] = sent_list[len(sent_list) - 1] + "."
    # print(sent_list)
    complete_sent = ""
    for i in range(0, len(sent_list)):
        complete_sent += sent_list[i] + " "
        if i == (len(sent_list) - 1):
            pass
    print(complete_sent)
        
# # 정답
# def correct_sent_answer(text:str) -> str:
#     text = text[0].upper + text[1:]

#     if not text.endswith('.'):
#         text += '.'

#     return text

a = "i am a boy"
b = "what the fuck"
correct_sentence(a)
correct_sentence(b)
# correct_sent_answer(a)
# correct_sent_answer(b)


















