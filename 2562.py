num_list = []
for i in range(9):
    num_list.append(int(input()))

big = max(num_list)
idx = num_list.index(big)   #���� �ٸ�
print(big)
print(idx+1)