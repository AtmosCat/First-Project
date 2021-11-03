def most_frequent(num_list):
    freq_list = []
    for num in num_list:
        freq_list.append(num_list.count(num))
        k = freq_list.index(max(freq_list))
    print(num_list[k])

most_frequent(['a', 'a', 'a', 'b', 'b', 'c'])
most_frequent(['a', 'a', 'bi', 'bi' ,'bi'])


def most_frequent_answer(data):
    print(max(data, key = data.count))
    return











