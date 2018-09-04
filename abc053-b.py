str_s = input()

# print(str_s[str_s.find("A"):str_s.rfind("Z") + 1])
print(str_s.rfind("Z") - str_s.find("A") + 1)
