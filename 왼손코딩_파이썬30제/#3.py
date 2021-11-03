# 문장과 알파벳 입력 시 입력한 문장에서 두 번째에 해당하는 알파벳의 인덱스 반환하는 함수 

# bet_list = []
# index_list = []
# def second_index(txt:str, k:str):
#     if k not in txt:
#         print("No k in txt")
#     else:
#         bet_cnt = txt.count(k)
#         if bet_cnt <= 1:
#             print("None")
#         else:
#             kk = txt.index(k)
#             txt = txt.replace(txt[kk][0],"?")
#             print(txt)

# second_index("my name", 'm')

# 정답
def second_index_answer(txt, symbol):
    if txt.count(symbol) < 2:
        return None
    
    first = txt.find(symbol)

    print(txt.find(symbol, first+1))

second_index_answer('apple', 'p')












