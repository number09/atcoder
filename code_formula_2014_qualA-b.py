a, b = map(int, input().split())
li_p = list(input().split())
li_q = list(input().split())

answer = '1234567890'

for p in li_p:
    answer = answer.replace(p, '.')
for q in li_q:
    answer = answer.replace(q, 'o')

print(' '.join([a if a in ['.', 'o'] else 'x' for a in answer[6:]]))
print(' ' + ' '.join([b if b in ['.', 'o'] else 'x' for b in answer[3:6]]) + ' ')
print('  ' + ' '.join([c if c in ['.', 'o'] else 'x' for c in answer[1:3]]) + '  ')
print('   ' + ''.join([d if d in ['.', 'o'] else 'x' for d in answer[0:1]]) + '   ')

