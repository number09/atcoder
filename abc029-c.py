n = int(input())

word = ""
def fc(word):
    temp = word
    if len(temp) < n:
        for w in ['a', 'b', 'c']:
            fc(temp + w)
    else:
        print(temp)
        return


fc(word)
