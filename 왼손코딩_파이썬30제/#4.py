
def between_markers(txt, first, second):
    if first == second:
        print("impossible")
    else:
        first_index = txt.find(first)
        second_index = txt.find(second)
        txt = txt.replace(txt[:first_index+1], "").replace(txt[second_index:], "")
        if first not in txt and second in txt:
            txt = txt.replace(txt[second_index:], "")
            print(txt)
        elif second not in txt and first in txt:
            txt = txt.replace(txt[:first_index+1], "")
            print(txt)
        elif first not in txt and second not in txt:
            print(txt)
        elif first >= second:
            print("")

        
between_markers("What is >apple<", ">", "<")
between_markers('No[/b] hi', '[b]', '[/b]')
between_markers('Hi guys', '>', '<')

# 정답
def between_markers_answer(txt, begin, end):
    if begin in txt:
        begin_index = txt.find(begin) + len(begin)
    else:
        begin_index = 0
    
    if end in txt:
        end_index = txt.find(end)
    else:
        end_index = len(txt)
    
    print(txt[begin_index:end_index])

between_markers_answer("What is >apple<", ">", "<")
between_markers_answer('No[/b] hi', '[b]', '[/b]')
between_markers_answer('Hi guys', '>', '<')






