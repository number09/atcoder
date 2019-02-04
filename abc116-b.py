s = int(input())

def myfnc(input):

    if input % 2 == 0:
        return input // 2
    else:
        return (3 * input) + 1

answer = list()
answer.append(s)
for i in range(2, 1000000):
    ret = myfnc(answer[-1])

    if ret in answer:
        print(i)
        exit(0)
    else:
        answer.append(ret)


