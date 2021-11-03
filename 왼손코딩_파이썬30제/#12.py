# def checkio(txt):
#     txt_list = txt.split()
#     num_list = ['0', '1','2','3','4','5','6','7','8','9']
#     for i in range(0, len(txt_list)-2):
#         for j in num_list:
#             if j not in txt_list[i]:
#                 if j not in txt_list[i+1]:
#                     if j not in txt_list[i+2]:
#                 pass
#         else:
#             print(False)
#     print(True)

# sample = "Hi, my 1 name is 1 Alex 1 and my hobby is 1 working out."
# # print(sample.split())
# # print(type(sample[7]*1))
# checkio(sample)

# 정답
def checkio_answer(words):
    count = 0
    numcnt = 0
    for word in words.split(" "):
        if word.isalpha():
            count += 1
            numcnt += 1
            if count >= 3:
                print("True")
                break
        else:
            count = 0
            numcnt += 1
    if numcnt == len(words):
        print("False")
    

sample = "Hello World 009 Hello"

checkio_answer(sample)
# print(sample.split())
# print(sample.split()[0].isalpha())


