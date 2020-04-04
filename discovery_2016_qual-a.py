w = int(input())
s = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'

a = len(s) // w
if len(s) % w > 0:
    a += 1
for i in range(a):
    print(s[i * w: (i * w) + w])
