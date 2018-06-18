array1 = [a for a in input()]
array2 = [b for b in input()]
ar = [array1, array2]

r_array1 = array1[::-1]

if array2 == r_array1:
    print("YES")
else:
    print("NO")




