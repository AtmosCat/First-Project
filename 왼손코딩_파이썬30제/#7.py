products_list = [
    {"name" : "bread", "price" : 100},
    {"name" : "wine", "price" : 138},
    {"name" : "meal", "price" : 15},
    {"name" : "water", "price" : 1}
]

def bigger_price(num, products):
    max_cnt = 0
    max_products = []
    max_price = 0
    for i in products:
        if i["price"] > max_price:
            max_products.append(i)
            max_price = 0
            max_cnt += 1
            if max_cnt == num:
                print(max_products)
                break

bigger_price(2, products_list)

    
# 정답

def bigger_price_answer(limit, data):
    print(sorted(data, key = lambda x : x['price'], reverse = True)[:limit]) # key를 지정해주면 그것에 따라 정렬해주는 함수 sorted / default : 오름차순, reverse : 내림차순

bigger_price_answer(2, products_list)












