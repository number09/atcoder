h, m = map(int, input().split())

m_d = 360 / 60 * m
h_d = 360 / 12 * (h % 12) + (m_d / 12)

print(min(abs(h_d - m_d), 360 - abs(h_d - m_d)))


