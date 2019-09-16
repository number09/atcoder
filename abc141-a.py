s = input()

tenki = ['Sunny', 'Cloudy', 'Rainy']

today = tenki.index(s)
print(tenki[(today + 1) % 3])