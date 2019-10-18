sd = input()
t = input()
li_answer = list()
c_loop = len(sd) - len(t) + 1

for i in range(c_loop):
    if all((w_sd == "?" or w_sd == w_t) for w_sd, w_t in zip(sd[i:i + len(t) + 1], t)):
        s_tmp = str(sd[0:i] + t + sd[i + len(t):]).replace("?", "a")
        li_answer.append(s_tmp)

if li_answer:
    print(sorted(li_answer)[0])
else:
    print("UNRESTORABLE")

