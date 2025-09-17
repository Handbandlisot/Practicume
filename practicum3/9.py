p_att = int(input())
p_comp = int(input())
p_yds = int(input())
p_td = int(input())
p_int = int(input())
a = (p_comp / p_att - 0.3) * 5
b = (p_yds / p_att - 3) * 0.25
c = (p_td / p_att) * 20
d = 2.375 - ((p_int / p_att) * 25)
print(((a + b + c + d) / 6) * 100)
