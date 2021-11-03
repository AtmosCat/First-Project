def checkio(num_list):
    freq_list = []
    for i in num_list:
        freq_list.append(num_list.count(i))
    for j in range(0, len(freq_list)):
        if freq_list[j] == 1:
            num_list[j] = "#"
    print(num_list)
    if "#" in num_list:
        for k in num_list:
            if k == str("#"):
                num_list.remove(k)
    print(num_list)
    return

checkio([1, 2, 3, 1, 3])
checkio([1, 2, 3, 4, 5])
checkio([5, 5, 5])
checkio([10, 9, 8, 10, 9])














