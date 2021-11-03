def index_power(num_list : list, k:int):
    if k >= len(num_list):
        print(-1)
        return 
    print(int(num_list[k])**k)

lst = [1, 2, 3, 4, 5]
index_power(lst, 2)
index_power(lst, 5)

# 정답
def index_power_answer(array, n):
    if n < len(array):
        return array[n] ** n
    else:
        return -1

index_power_answer(lst, 3)



