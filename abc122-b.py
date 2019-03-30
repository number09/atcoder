import re
s = input()

result = re.sub('[^ACGT]', ',', s).split(',')

print(max([len(r)for r in result]))



