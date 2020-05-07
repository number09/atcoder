s = input()

print(sorted([{'key': w, 'count': s.count(w)} for w in ['a', 'b', 'c']], key=lambda x: x['count'], reverse=True)
      [0]['key'])
