stock_dict = {'CAC' : 10.0, 'ATX' : 390.2, 'WIG' : 18.2, 'TASI' : 0}

def best_stock(dict):
    stock_keys = list(dict.keys())
    stock_values = list(dict.values())
    max_value= max(stock_values)
    max_index = stock_values.index(max_value)
    max_key = stock_keys[max_index]
    print(max_key)

best_stock(stock_dict)


# 정답

def best_stock_answer(data):
    max_price = 0
    answer = " "

    for s in data:
        if data[s] > max_price:
            max_price = data[s]
            answer = s
    
    print(answer)

best_stock_answer(stock_dict)









