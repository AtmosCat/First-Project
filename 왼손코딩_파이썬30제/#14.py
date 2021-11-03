def left_join(words:tuple):
    words = list(words)
    for i in range(0, len(words)):
        words[i] = words[i].replace("right", "left")
        if "right" not in words[i]:
            pass
    print(",".join(words))


t1 = ("left", "right", "left", "stop")
t2 = ("bright aright", "ok")
left_join(t1)
left_join(t2)

# 정답
def left_join_answer(phrases:tuple):
    print((",".join(phrases)).replace("right", "left"))
    return

left_join_answer(t1)
left_join_answer(t2)







