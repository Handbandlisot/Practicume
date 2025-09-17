n = int(input())
c = int(input())
num_rec = int(input()) - 1
colvo_rec = n * c
page_num = 1
col_num = 1
line_num = 1
while num_rec > colvo_rec:
    num_rec -= colvo_rec
    page_num += 1
while num_rec > c:
    num_rec -= c
    line_num += 1
col_num += num_rec
print(page_num, col_num, line_num)
